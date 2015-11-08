/**
 * Copyright (C) 2004 Fumitoshi UKAI <ukai@debian.or.jp>
 * All rights reserved.
 * This is free software with ABSOLUTELY NO WARRANTY.
 *
 * You can redistribute it and/or modify it under the terms of
 * the GNU General Public License version 2.
 */


/* to eliminate the error in bfd.h */
#if !defined PACKAGE
#define PACKAGE
#endif

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ptrace.h>
#include <sys/wait.h>
#include <sys/syscall.h>
#include <sys/mman.h>
#include <sys/user.h>
#include <bfd.h>
#include <elf.h>
#include <link.h>
#define _GNU_SOURCE
#include <getopt.h>

#define DEBUG(fmt,...)  do {if (G_opt_debug) printf(fmt, __VA_ARGS__);} while (0)
#define INFO(fmt,...) do {if (G_opt_verbose) printf(fmt, __VA_ARGS__);} while (0)
#define NOTICE(fmt,...) do {if (!G_opt_quiet) printf(fmt, __VA_ARGS__);} while (0)
#define ERROR(fmt,...) do { fprintf(stderr, fmt, __VA_ARGS__);} while (0)


/*****************/
#if defined(linux) && defined(i386)
/* sysdeps/i386/dl-machine.h */
/* The i386 never uses Elf32_Rela relocations for the dynamic linker.
 *    Prelinked libraries may use Elf32_Rela though.  */
#define ELF_MACHINE_PLT_REL 1
#else
#error Unsupported platform
#endif

/* glibc/elf/dl-runtime.c */
#if (!defined ELF_MACHINE_NO_RELA && !defined ELF_MACHINE_PLT_REL) \
    || ELF_MACHINE_NO_REL
# define PLTREL  ElfW(Rela)
#else
# define PLTREL  ElfW(Rel)
#endif

/* glibc/sysdeps/generic/ldsodefs.h */
#define ELFW(type) _ElfW (ELF, __ELF_NATIVE_CLASS, type)

// #define bfd_get_section_size_before_reloc(section) ((section)->rawsize)
#define bfd_get_section_size_before_reloc(section) bfd_get_section_size(section)


/* FIXME: too slow lookup, use hashtable or so */
struct symaddr {
    struct symaddr *next;
    char *name;
    int addr;
} *G_symaddrs;

struct memvar {
    struct memvar *next;
    char *name;
    long addr;
    struct symaddr *syms;
} *G_memvartab;

int G_opt_debug;
int G_opt_verbose;
int G_opt_quiet;


static int lookup_symaddr(char *name, struct symaddr *symaddr0)
{
    struct symaddr *sa;
    for (sa = symaddr0; sa != NULL && sa->name != NULL; sa = sa->next) {
        if (strcmp(name, sa->name) == 0) {
            return sa->addr;
        }
    }
    DEBUG("[symaddr %s not found]", name);
    return 0;
}

static void add_symaddr(const char *name, int addr, struct symaddr **symaddrp)
{
    struct symaddr *sa;

    if (*name == '\0')
        return;

    sa = (struct symaddr *)malloc(sizeof(struct symaddr));
    memset(sa, 0, sizeof(struct symaddr));
    sa->name = strdup(name);
    sa->addr = addr;
    sa->next = *symaddrp;
    *symaddrp = sa;
    return;
}

static int bfd_read_symbols(bfd *abfd, int offset, struct symaddr **symaddrp)
{
    long storage_needed;
    asymbol **symbol_table = NULL;
    long number_of_symbols;
    long i;
    int ret = 0;

    /* symbol table */
    DEBUG("%s\n","SYMBOL TABLE:");
    storage_needed = bfd_get_symtab_upper_bound (abfd);
    if (storage_needed < 0) {
        bfd_perror("bfd_get_symtab_upper_bound");
        ret = -1;
        goto dynsym;
    }
    if (storage_needed == 0) {
        DEBUG("%s\n", "no symbols");
        goto dynsym;
    }
    symbol_table = (asymbol **)malloc (storage_needed);
    number_of_symbols = bfd_canonicalize_symtab (abfd, symbol_table);
    if (number_of_symbols < 0) {
        bfd_perror("bfd_canonicalize_symtab");
        ret = -1;
        goto dynsym;
    }
    for (i = 0; i < number_of_symbols; i++) {
        asymbol *asym = symbol_table[i];
        const char *sym_name = bfd_asymbol_name(asym);
        int symclass = bfd_decode_symclass(asym);
        int sym_value = bfd_asymbol_value(asym) + offset;
        if (*sym_name == '\0')
            continue;
        if (bfd_is_undefined_symclass(symclass))
            continue;
        DEBUG(" %s=%p\n", sym_name, (void *)sym_value);
        add_symaddr(sym_name, sym_value, symaddrp);
    }
dynsym:
    if (symbol_table)
        free(symbol_table);
    symbol_table = NULL;

    DEBUG("%s\n", "DYNAMIC SYMBOL TABLE:");
    storage_needed = bfd_get_dynamic_symtab_upper_bound (abfd);
    if (storage_needed < 0) {
        bfd_perror("bfd_get_dynamic_symtab_upper_bound");
        ret = -1;
        goto out;
    }
    if (storage_needed == 0) {
        DEBUG("%s\n", "no symbols");
        goto out;
    }
    symbol_table = (asymbol **)malloc (storage_needed);
    number_of_symbols = bfd_canonicalize_dynamic_symtab (abfd, symbol_table);
    if (number_of_symbols < 0) {
        bfd_perror("bfd_canonicalize_symtab");
        ret = -1;
        goto out;
    }
    for (i = 0; i < number_of_symbols; i++) {
        asymbol *asym = symbol_table[i];
        const char *sym_name = bfd_asymbol_name(asym);
        int symclass = bfd_decode_symclass(asym);
        int sym_value = bfd_asymbol_value(asym) + offset;
        if (*sym_name == '\0')
            continue;
        if (bfd_is_undefined_symclass(symclass))
            continue;
        DEBUG(" %s=%p\n", sym_name, (void *)sym_value);
        add_symaddr(sym_name, sym_value, symaddrp);
    }
out:
    if (symbol_table)
        free(symbol_table);
    return ret;
}

static void* bfd_load_section(bfd *abfd, char *sect_name, int *sz)
{
    asection *sect;
    int size;
    char *buf;
    sect = bfd_get_section_by_name(abfd, sect_name);
    if (sect == NULL) {
        return NULL;
    }
    size = bfd_get_section_size_before_reloc(sect);
    buf = (char *)malloc(size);
    bfd_get_section_contents(abfd, sect, buf, 0, size);
    if (sz)
        *sz = size;
    return buf;
}

static void fixup(bfd *abfd, ElfW(Sym) *symtab, char *strtab, PLTREL *reloc,
      struct symaddr *symaddr0, char *outbuf, int outsize)
{
    ElfW(Sym) *sym;
    int rel_addr;
    int addr;
    char *sym_name;

    sym = &symtab[ELFW(R_SYM)(reloc->r_info)];
    rel_addr = reloc->r_offset;
    sym_name = &strtab[sym->st_name];
    INFO("%s @ %d 0x%x ", sym_name, rel_addr, rel_addr);
    addr = lookup_symaddr(sym_name, symaddr0);
    if (addr) {
        *(int *)(outbuf + rel_addr) = addr;
        INFO("= %p\n", (void *)addr);
    } else {
        INFO("= %s\n", "*UND*");
    }
    return;
}

static int fixups(bfd *abfd, struct symaddr *symaddr0, char *outbuf, int outsize)
{
    ElfW(Sym) *symtab;
    char *strtab;
    PLTREL *reloc, *reloc_end;
    int reloc_size;


    DEBUG("%s...\n", "fixups");
    symtab = (ElfW(Sym)*)bfd_load_section(abfd, ".dynsym", NULL);
    if (symtab == NULL) {
        ERROR("load error %s\n", ".dynsym");
        return -1;
    }
    strtab = (char *)bfd_load_section(abfd, ".dynstr", NULL);
    if (strtab == NULL) {
        ERROR("load error %s\n", ".dynstr");
        return -1;
    }
    reloc = (PLTREL *)bfd_load_section(abfd, ".rel.dyn", &reloc_size);
    if (reloc == NULL) {
        ERROR("load error? %s\n", ".rel.dyn");
        goto rel_plt;
    }
    reloc_end = (PLTREL *)((char *)reloc + reloc_size);
    DEBUG(".rel.dyn reloc_size = %d\n", reloc_size);
    for (; reloc < reloc_end; reloc++) {
        fixup(abfd, symtab, strtab, reloc, symaddr0, outbuf, outsize);
    }

rel_plt:
    reloc = (PLTREL *)bfd_load_section(abfd, ".rel.plt", &reloc_size);
    if (reloc == NULL) {
        ERROR("load error %s\n", ".rel.plt");
        return -1;
    }
    reloc_end = (PLTREL *)((char *)reloc + reloc_size);
    DEBUG(".rel.plt reloc_size = %d\n", reloc_size);
    for (; reloc < reloc_end; reloc++) {
        fixup(abfd, symtab, strtab, reloc, symaddr0, outbuf, outsize);
    }
    return 0;
}

static void bfd_map_section_alloc_size(bfd *abfd, asection *sect, void *obj)
{
    int *outsizep = (int *)obj;
    int vma = bfd_get_section_vma(abfd, sect);
    int size = bfd_get_section_size_before_reloc(sect);
    int flags = bfd_get_section_flags(abfd, sect);
    if ((flags & (SEC_ALLOC|SEC_LOAD)) != 0) {
        if ((vma + size) > *outsizep)
            *outsizep = align_power(vma + size,
                                    bfd_get_section_alignment(abfd, sect));
    }
}

static void bfd_map_section_buf(bfd *abfd, asection *sect, void *obj)
{
    char *outbuf = (char *)obj;
    int vma = bfd_get_section_vma(abfd, sect);
    int size = bfd_get_section_size_before_reloc(sect);
    int flags = bfd_get_section_flags(abfd, sect);
    if ((flags & (SEC_ALLOC|SEC_LOAD)) != 0) {
        DEBUG("section %s @ %p size %d flags 0x%0x\n",
              bfd_get_section_name(abfd, sect), (void *)vma, size, flags);
        bfd_get_section_contents(abfd, sect, outbuf + vma, 0, size);
    }
}

static int init_target_symbol(pid_t pid, char *filename)
{
    bfd *abfd;
    char buf[4096];
    FILE *fp;

    DEBUG("%s: pid %d filename %s\n", __func__, pid, filename);
    snprintf(buf, sizeof(buf), "/proc/%d/maps", pid);
    fp = fopen(buf, "r");
    if (fp == NULL) {
        perror("open /proc/$$/maps");
        return -1;
    }
    while (fgets(buf, sizeof(buf), fp) != NULL) {
        /* linux/fs/proc/task_mmu.c */
        int vm_start, vm_end, pgoff, major, minor, ino;
        char flags[5], mfilename[4096];
        if (sscanf(buf, "%x-%x %4s %x %d:%d %d %s",
                   &vm_start, &vm_end, flags, &pgoff, &major, &minor, &ino,
                   mfilename) < 7) {
            ERROR("E: invalid format in /proc/$$/maps? %s", buf);
            continue;
        }
        DEBUG("0x%x-0x%x %s 0x%x %s\n",
              vm_start, vm_end, flags, pgoff, mfilename);
        if (flags[0] == 'r' && flags[2] == 'x'
                && pgoff == 0 && *mfilename != '\0') {
            DEBUG("file %s @ %p\n", mfilename, (void *)vm_start);
            abfd = bfd_openr(mfilename, NULL);
            if (abfd == NULL) {
                bfd_perror("bfd_openr");                
                fprintf(stderr, "%s#%d: failed to call bfd_openr() on %s.\n",
                    __func__, __LINE__, mfilename);
                continue;
            }
            bfd_check_format(abfd, bfd_object);
            bfd_read_symbols(abfd, vm_start, &G_symaddrs);
            bfd_close(abfd);
        }
    }
    DEBUG("target file %s\n", filename);
    abfd = bfd_openr(filename, NULL);
    if (abfd == NULL) {
        bfd_perror("bfd_openr");
        fprintf(stderr, "%s#%d: failed to call bfd_openr() on %s.\n",
            __func__, __LINE__, filename);
        return -1;
    }
    bfd_check_format(abfd, bfd_object);
    bfd_read_symbols(abfd, 0, &G_symaddrs);
    bfd_close(abfd);
    return 0;
}

static int push_stack(pid_t pid, struct user_regs_struct *regs, long v)
{
    regs->esp -= 4;
    if (ptrace(PTRACE_POKEDATA, pid, regs->esp, v) < 0) {
        perror("ptrace poke stack");
        return -1;
    }
    return 0;
}

static long target_alloc(pid_t pid, size_t siz)
{
    struct user_regs_struct regs, oregs;
    char code[] = {0xcd, 0x80, 0xcc, 0x00}; /* int $0x80, int3,  */
    long lv;
    long raddr;

    if (ptrace(PTRACE_GETREGS, pid, NULL, &oregs) < 0) {
        perror("ptrace getregs");
        return 0;
    }

    regs = oregs;
    DEBUG("%%esp = %p\n", (void *)regs.esp);
    regs.esp -= sizeof(int);
    memcpy(&lv, code, 4);
    if (ptrace(PTRACE_POKEDATA, pid, regs.esp, lv) < 0) {
        perror("ptrace poke code");
        return 0;
    }
    regs.eip = regs.esp;  /* int $0x80 */
    raddr = regs.esp + 2; /* int3 */
    /*
     * mmap(NULL, siz, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
     */

    push_stack(pid, &regs, 0); /* arg 6 (offset) */
    push_stack(pid, &regs, -1);
    push_stack(pid, &regs, MAP_PRIVATE|MAP_ANONYMOUS);
    push_stack(pid, &regs, PROT_READ|PROT_WRITE);
    push_stack(pid, &regs, siz);
    push_stack(pid, &regs, 0);
    push_stack(pid, &regs, raddr);
    regs.ebx = regs.esp + 4; /* arg 1 (ptr to args) */
    regs.eax = SYS_mmap; /* system call number */
    /**
     * stack will be:
     *     %esp: return address
     *  4(%esp): arg 1 <- %ebx : pointer to args
     *  8(%esp): arg 2
     * 12(%esp): arg 3
     * 16(%esp): arg 4
     * 20(%esp): arg 5
     * 24(%esp): arg 6
     * 28(%esp): int $0x80  <- %eip jump address
     * 30(%esp): int3       <- return address
     * 31(%esp): --
     * 32(%esp): original esp
     *
     * glibc/sysdeps/unix/sysv/linux/i386/mmap.S
     */
    DEBUG("target_alloc %s\n", "set regs");
    if (ptrace(PTRACE_SETREGS, pid, NULL, &regs) < 0) {
        perror("ptrace set regs");
        return 0;
    }
    DEBUG("target_allloc %s\n", "mmap call");
    if (ptrace(PTRACE_CONT, pid, NULL, NULL) < 0) {
        perror("ptrace cont");
        return 0;
    }
    wait(NULL);
    DEBUG("target_alloc %s\n", "mmap done");
    if (ptrace(PTRACE_GETREGS, pid, NULL, &regs) < 0) {
        perror("ptrace get regs of mmap");
        return 0;
    }
    lv = regs.eax; /* return value */
    if ((void *)lv == MAP_FAILED) {
        DEBUG("target_alloc failed %p\n", (void *)0);
        return 0;
    }
    INFO("allocated = %p %d bytes\n", (void*)lv, siz);

    /* restore old regs */
    if (ptrace(PTRACE_SETREGS, pid, NULL, &oregs) < 0) {
        perror("ptrace restore regs");
        return 0;
    }
    return lv;
}

static int set_data(pid_t pid, int addr, void *val, int len_in_bytes)
{
    /* a function's address may not align at 4 bytes boundary */
    if (!addr || !val || len_in_bytes <= 0)
    {
        ERROR("%s: invalid parameter address %p, val %p, len %d.\n",
            __func__, (void*)addr, val, len_in_bytes);
        return -1;
    }

    int i;
    int addr0 = addr & ~3;     /* align at 4 bytes boundary */
    int *dst;                  /* an int is of size equal to a word */
    const int len_in_words = (len_in_bytes + addr - addr0 + 3) >> 2; /* round up */
    
    dst = malloc(len_in_words * sizeof(int));
    if (!dst) {
        ERROR("%s: failed to alloc memory.\n", __func__);
        return -1;
    }

    /* save the original data, in case of len_in_bytes is not aligned at word boundary */
    for (i = 0; i < len_in_words; ++i) {
        dst[i] = ptrace(PTRACE_PEEKDATA, pid, addr + i * sizeof(int), NULL);
        if (dst[i] == -1 && errno) {
            perror("PTRACE_PEEKDATA");
            return -1;
        }
    }

    /* overwrite the target */
    memcpy((char *)dst + addr - addr0, val, len_in_bytes);
    for (i = 0; i < len_in_words; ++i) {
        if (ptrace(PTRACE_POKEDATA, pid, addr0 + i * sizeof(int), dst[i]) < 0) {
            perror("PTRACE_POKEDATA");
            return -1;
        }
    }
    
    return 0;
}

static long lookup_memvar(char *name)
{
    struct memvar *mv;
    int namelen = strlen(name);
    char *sym = strchr(name, ':');
    if (sym) {
        namelen = sym - name;
        sym += 1;
    }
    // printf("lookup_memvar %s sym %s", name, sym);
    for (mv = G_memvartab; mv != NULL && mv->name != NULL; mv = mv->next) {
        if (strncmp(name, mv->name, namelen) == 0) {
            if (sym != NULL) {
                if (isdigit(*sym)) {
                    int offset = strtol(sym, NULL, 0);
                    return mv->addr + offset;
                } else if (mv->syms != NULL) {
                    return lookup_symaddr(sym, mv->syms);
                }
            } else {
                return mv->addr;
            }
        }
    }
    ERROR("memvar %s not found\n", name);
    return 0;
}

static void set_memvar(char *name, long addr, struct symaddr *syms)
{
    struct memvar *mv = (struct memvar *)malloc(sizeof(struct memvar));
    memset(mv, 0, sizeof(struct memvar));
    mv->name = strdup(name);
    mv->addr = addr;
    mv->syms = syms;
    mv->next = G_memvartab;
    G_memvartab = mv;
    DEBUG("memvar %s set to %p syms:%p\n", name, (void *)addr, syms);
    return;
}

static int lookup_addr(char *addrinfo) {
    int addr = 0;
    DEBUG("lookup_addr %s => ", addrinfo);
    if (*addrinfo == '$') {
        addr = lookup_memvar(addrinfo+1);
    } else if (isdigit(*addrinfo)) {
        addr = strtol(addrinfo, NULL, 0);
    } else {
        addr = lookup_symaddr(addrinfo, G_symaddrs);
    }
    DEBUG("%p\n", (void *)addr);
    return addr;
}

static void parse_data(char *type, char *p, void **vptr, int *vlenp)
{
    DEBUG("data type=%s\n", type);
    if (strcmp(type, "int") == 0) {
        *vptr = (int*)malloc(sizeof(int));
        *vlenp = sizeof(int);
        *(int *)*vptr = strtol(p, NULL, 0);
    } else if (strcmp(type, "str") == 0) {
        *vlenp = strlen(p);
        *vptr = malloc(*vlenp);
        memcpy(*vptr, p, *vlenp);
    } else if (strcmp(type, "addr") == 0) {
        *vptr = (int*)malloc(sizeof(int));
        *vlenp = sizeof(int);
        *(int *)*vptr = lookup_addr(p);
    } else if (strcmp(type, "hex") == 0) {
        int i;
        int v;
        *vlenp = (strlen(p) + 1)/2;
        *vptr = malloc(*vlenp);
        for (i = 0; i < *vlenp; i++) {
            sscanf(p+i*2, "%02x", &v);
            ((char *)*vptr)[i] = v;
        }
    }
    return;
}

static char* format_data(char *type, char *p, void *vptr, int vlen)
{
    static char databuf[4096]; /* XXX */

    if (strcmp(type, "int") == 0) {
        snprintf(databuf, sizeof(databuf)-1, "%d (%s)", *(int*)vptr, p);
    } else if (strcmp(type, "str") == 0) {
        snprintf(databuf, sizeof(databuf)-1, "\"%s\" [%d]",
                 (char *)vptr, vlen);
    } else if (strcmp(type, "addr") == 0) {
        snprintf(databuf, sizeof(databuf)-1, "@%p (%s)",
                 (void *)(*(int *)vptr), p);
    } else if (strcmp(type, "hex") == 0) {
        snprintf(databuf, sizeof(databuf)-1, "hex [%d]", vlen);
    }
    return databuf;
}

static void print_usage(char *prog)
{
    const char rcsid[] = "$Id: livepatch.c 351 2004-11-08 16:05:26Z ukai $";
    printf("Usage: %s [option] <pid> <target-binary>\n"
           "  apply binary patches to running process.\n"
           "  read stdin for patch instructions.\n"
           "  --help    help message.\n"
           "  --quiet   quiet mode.\n"
           "  --verbose verbose mode.\n"
           "  --debug   turn on debug message.\n"
           "\n"
           "%s\n"
           "Copyright (C) 2004 Fumitoshi UKAI <ukai@debian.or.jp>\n"
           "All rights reserved.\n"
           "This is free software with ABSOLUTELY NO WARRANTY.\n",
           prog, rcsid);
}

static void print_help(char *prog)
{
    print_usage(prog);
    printf("\npatch instructions:\n"
           "[instruction line]\n"
           "set <addr> <type> <value>     # set value to address\n"
           "new <memname> <size>          # allocate new memory space\n"
           "load <memname> <filename>     # load file in memory space\n"
           "dl <memname> <filename>       # load & symbol fixups.\n"
           "jmp <addr1> <addr2>           # set jmp to addr2 at addr1.\n"
           "\n"
           "[parameter]\n"
           "addr := <integer> | $<memname> | $<memname>:<symbol> | <symbol>\n"
           "type := int | str | hex | addr\n"
           "  int - integer parsed by strtol(i,NULL,0); size = 4\n"
           "  str - string until '\\n'\n"
           "  hex - ([0-9A-Fa-f]{2})*\n"
           "  addr - addr above\n");
}

static int parse_options(int argc, char* argv[])
{
    int ret = 0;
    int opt_index;
    int c;
    const struct option long_opts[] = {
        {"debug", no_argument, &G_opt_debug, 1},
        {"verbose", no_argument, &G_opt_verbose, 1},
        {"quiet", no_argument, &G_opt_quiet, 1},
        {"help", no_argument, NULL, 'h'},
        {NULL, 0, NULL, 0},
    };    

    while (1) {
        c = getopt_long(argc, argv, "dvqh", long_opts, &opt_index);
        if (c == -1)
            break;
        switch (c) {
        case 0: /* long options */
            break;
        case 'd':
            G_opt_debug = 1;
            break;
        case 'v':
            G_opt_verbose = 1;
            break;
        case 'q':
            G_opt_quiet = 1;
            break;
        case 'h':
            print_help(argv[0]);
            break;
        case '?': /* FALLTHROUGH */
        default:
            print_usage(argv[0]);
            ret = -1;
        }
    }
    
    if (G_opt_quiet) {
        G_opt_debug = G_opt_verbose = 0;
    }

    if (argc < optind + 2) {
        print_usage(argv[0]);
        ret = -1;
    }

    return ret;
}

int main(int argc, char *argv[])
{
    #define BUF_ARG_MAX_LEN 1024
    pid_t target_pid;
    char *target_image_path;
    char buf_usr_input[4096];
    char buf_arg1[BUF_ARG_MAX_LEN];
    char buf_arg2[BUF_ARG_MAX_LEN];


    if (parse_options(argc, argv)) {
        return -1;
    }
    
    bfd_init();
    target_pid = strtol(argv[optind], NULL, 0);
    target_image_path = argv[optind + 1];
    init_target_symbol(target_pid, target_image_path);

    if (ptrace(PTRACE_ATTACH, target_pid, NULL, NULL)) {
        perror("ptrace attach");
        return -1;
    }
    
    NOTICE("Attached to process %d.\n", target_pid);
    wait(NULL);

    /* process patching commands */
    while (fgets(buf_usr_input, sizeof(buf_usr_input), stdin)) {
        /* set addr type value */
        if (0 == strncmp(buf_usr_input, "set ", 4)) {
            char buf_arg3[BUF_ARG_MAX_LEN];
            int addr;
            void *v;
            int vlen;

            if (sscanf(buf_usr_input, "set %s %s %s\n", buf_arg1, buf_arg2, buf_arg3)
                != 3) {
                ERROR("E: invalid set line: %s", buf_usr_input);
                continue;
            }
            
            addr = lookup_addr(buf_arg1);
            parse_data(buf_arg2, buf_arg3, &v, &vlen);
            INFO("set addr %p = value %s\n", (void *)addr,
                format_data(buf_arg2, buf_arg3, v, vlen));
            
            if (set_data(target_pid, addr, v, vlen) < 0) {
                ERROR("E: failed to set %p = %s\n", (void *)addr, buf_arg3);
                continue;
            }
            NOTICE("set %p %s %s\n", (void *)addr, buf_arg2, buf_arg3);
        } 
        /* new memname size */
        else if (0 == strncmp(buf_usr_input, "new ", 4)) {
            int siz;
            int addr;

            if (sscanf(buf_usr_input, "new %s %s\n", buf_arg1, buf_arg2) != 2) {
                ERROR("E: invalid new command: %s", buf_usr_input);
                continue;
            }
            
            siz = strtol(buf_arg2, NULL, 0);
            if (errno || siz <= 0) {
                ERROR("E: invalid size %d of new command.\n", siz);
                continue;
            }
            
            addr = target_alloc(target_pid, siz);
            if (addr == 0) {
                ERROR("E: failed to alloc memory of size %d.\n", siz);
                continue;
            }
            
            set_memvar(buf_arg1, addr, NULL);
            NOTICE("new %s @%p of size %d.\n", buf_arg1, (void *)addr, siz);
        }
        /* load memname filename */
        else if (0 == strncmp(buf_usr_input, "load ", 5)) {
            struct stat st;
            char *p;
            long addr;
            FILE *fp;

            if (sscanf(buf_usr_input, "load %s %s\n", buf_arg1, buf_arg2) != 2) {
                ERROR("E: invalid load command: %s", buf_usr_input);
                continue;
            }
            
            if (stat(buf_arg2, &st) < 0) {
                perror("stat");
                continue;
            }
            
            INFO("load memvar=%s buf_arg2=%s size=%ld\n",
                 buf_arg1, buf_arg2, st.st_size);
            // TODO: mmap on file in target?

            /* load the file into my address space */
            p = malloc(st.st_size);
            if (!p) {
                ERROR("E: malloc failed. size=%ld\n", st.st_size);
                continue;
            }
            fp = fopen(buf_arg2, "r");
            if (!fp) {
                ERROR("E: fopen %s error\n", buf_arg2);
                continue;
            }
            if (fread(p, st.st_size, 1, fp) == 0) {
                ERROR("E: fread error. %ld\n", st.st_size);
                continue;
            }
            fclose(fp);

            /* copy the file to target process address space */
            addr = target_alloc(target_pid, st.st_size);
            if (addr == 0) {
                ERROR("E: target_alloc failed. pid=%d size=%ld\n",
                      target_pid, st.st_size);
                continue;
            }
            if (set_data(target_pid, addr, p, st.st_size) < 0) {
                ERROR("E: load %s @ %p failed.\n", buf_arg2, (void *)addr);
                continue;
            }
            set_memvar(buf_arg1, addr, NULL);
            NOTICE("Loaded %s to %s @%p of length %ld.\n", buf_arg2, buf_arg1,
                (void *)addr, st.st_size);
        }
        /* dl memname filename */
        else if (0 == strncmp(buf_usr_input, "dl ", 3)) {
            bfd *abfd;
            char *outbuf;
            int outsize;
            int addr;
            struct symaddr *symaddr0 = NULL;

            if (sscanf(buf_usr_input, "dl %s %s\n", buf_arg1, buf_arg2) != 2) {
                ERROR("E: invalid dl line: %s", buf_usr_input);
                continue;
            }
            
            INFO("dl pid %d, memvar = %s, buf_arg2 = %s.\n",
                 target_pid, buf_arg1, buf_arg2);

            abfd = bfd_openr(buf_arg2, NULL);
            if (abfd == NULL) {             
                fprintf(stderr, "%s#%d: failed to call bfd_openr() on %s.\n",
                    __func__, __LINE__, buf_arg2);
                bfd_perror("bfd_openr");
                continue;
            }
            
            bfd_check_format(abfd, bfd_object);
            outsize = 0;
            bfd_map_over_sections(abfd, bfd_map_section_alloc_size, &outsize);
            outbuf = (char *)malloc(outsize);
            if (outbuf == NULL) {
                ERROR("E: malloc failed. size=%d\n", outsize);
                continue;
            }
            memset(outbuf, 0, outsize);
            /* XXX: size parameter */
            bfd_map_over_sections(abfd, bfd_map_section_buf, outbuf);

            /* global */
            INFO("global symbol fixups %s\n", buf_arg2);
            fixups(abfd, G_symaddrs, outbuf, outsize);

            addr = target_alloc(target_pid, outsize);
            if (addr == 0) {
                ERROR("E: target_alloc failed. pid=%d size=%d\n",
                      target_pid, outsize);
                continue;
            }

            bfd_read_symbols(abfd, addr, &symaddr0);
            /* local */
            INFO("local symbol fixups %s offset %p\n", buf_arg2, (void *)addr);
            fixups(abfd, symaddr0, outbuf, outsize);
            bfd_close(abfd);

            if (set_data(target_pid, addr, outbuf, outsize) < 0) {
                ERROR("E: dl %s @ %p failed.\n", buf_arg2, (void *)addr);
                continue;
            }
            set_memvar(buf_arg1, addr, symaddr0);
            NOTICE("dl %s @ %p [%d] %s\n", buf_arg1, (void *)addr,
                   outsize, buf_arg2);
        } 
        /* jmp src_addr dst_addr */
        /* jump near, relative */
        else if (strncmp(buf_usr_input, "jmp ", 4) == 0) {
            int src_addr;
            int dst_addr;
            long jmp_relative;
            char jmp_code[5];

            if (sscanf(buf_usr_input, "jmp %s %s\n", buf_arg1, buf_arg2) != 2) {
                ERROR("E: invalid jmp command: %s", buf_usr_input);
                continue;
            }
            
            src_addr = lookup_addr(buf_arg1);
            dst_addr = lookup_addr(buf_arg2);
            jmp_relative = dst_addr - (src_addr + 5);
            INFO("jmp from %p to %p, relative %ld.\n", 
                (void*)src_addr, (void*)src_addr, jmp_relative);

            jmp_code[0] = 0xe9;   /* the code of the x86 JMP instruction */
            memcpy(jmp_code + 1, &jmp_relative, sizeof(int));
            if (set_data(target_pid, src_addr, jmp_code, sizeof(jmp_code)) < 0) {
                ERROR("E: jmp %p %p failed.\n", (void *)src_addr, (void *)dst_addr);
                continue;
            }
            
            NOTICE("jmp %p %p\n", (void *)src_addr, (void *)dst_addr);
        }
        else if (0 == strncmp(buf_usr_input, "exit", 4) || 0 == strncmp(buf_usr_input, "quit", 4)){
            break;
        }
        else {
            ERROR("E: unknown command %s\n", buf_usr_input);
        }
    }
    
    ptrace(PTRACE_DETACH, target_pid, NULL, NULL);
    DEBUG("Detached pid %d.\n", target_pid);
    
    return 0;
}

