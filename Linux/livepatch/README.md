Original post: http://ukai.jp/Software/livepatch/

README - livepatch
$Id: README 345 2004-11-04 11:12:24Z ukai $

'livepatch' is a command to apply binary patches on running process.
I wonder this is practical, but it seems to be required in teleco area,
according to Pannus project page (AVL.14.0 of OSDL CGL v3.0).  
I just wrote it just for learning and hacking with ptrace(2) and bfd 
library in a day. It was very fun!

"livepatch" is just a small userland program which provides functionalities
of dynamic loading and overwriting on-memory code & data in a running process.
We don't need any unofficial kernel patches and/or uncommon libraries.
While applying live patch, that is, overwriting on-memory code & data
in a target process, the target process will be in sleep status.
"livepatch" makes it possible to modify on-memory code & data and load
ELF shared object or arbitrary binary files in a running process.

Thus, "livepatch" may meet AVL.14.0 of OSDL CGL Availability
Requirements Definition - version 3.0 (public draft) in some level.

Note: it's not part of activities of OSDL nor OSDL Japan.

PREREQUISITE
 bfd library that comes with binutils.
 On Debian GNU/Linux, just install binutils-dev.
 (I used binutils-dev 2.15-4)

  # apt-get install binutils-dev

BUILD & INSTALL

You need at least livepatch.c and optionally Makefile.

 $ ls
 Makefile  README bfd.c fixup.c fixup.txt livepatch.c
 $ make
 cc -Wall -O2 -g -c -o livepatch.o livepatch.c
 cc -o livepatch livepatch.o -lbfd
 $

then, copy livepatch where you want to install.

USAGE

 - You should prepare target processes executable files with symbol tables,
   that is, not stripped version.  If stripped, 'livepatch' can't know
   the symbol values of the target process. Note that the running process may
   be a process invoked from stripped version of the binary file.

 - If you want to add code to the target, you should write it and compile
   with -fPIC and -shared, like followings

    $ cc -shared -fPIC -o foo.so foo.c

   If you want to refer a symbol in the target, you should declare it
   with "extern". 'livepatch' will try to resolve these symbols when the
   shared object file is loaded by "dl" instruction of 'livepatch'.

 - patch instructions that 'livepatch' supports are follows:

    - set <addr> <type> <value>

       set value that is specified by <type> and <value> to <addr> 
       in a target process.

    - new <memname> <size>

       allocate new memory space in a target process.
       you can refer this area with <memname> in the following instructions.

    - load <memname> <filename>

       load a file contents in new memory space in a target process.
       you can refer this area with <memname> in the following instructions.

    - dl <memname> <filename>

       load ELF shared object file in new memory space in a target process
       with resolving dynamic symbols.
       you can refer this area with <memname> in the following instructions,
       and symbols in this ELF shared object with <memname>:<symbol>.

    - jmp <addr1> <addr2>

       set jmp instruction to <addr2> at <addr1> in a target process, so
       that if the process comes (or calls) <addr1>, it will jump to
       <addr2>.


   In <addr>, you can use the followings
  
     - integer value
       It is interpreted as absolute address in a target process.
     - $<memname>
        start address of <memname> allocated by "new", "load" or "dl".
     - $<memname>:<symbol>
        address pointed by <symbol> in <memname> loaded by "dl".
     - $<memname>:intvalue
        start address + intvalue in <memname>
     - symbol
        address pointed by <symbol> in target.

  <type> <value>:
 
     - <type> is int
        <value> is interpreted as integer value 
        (using strtol(<value>, NULL, 0))
     - <type> is str
        <value> is interpreted as string. (until '\n')
     - <type> is hex
        <value> is hexadecimal representation.
        eg. <value>=686578 -> "hex"
     - <type> is addr
        <value> is interpreted as <addr> described as above.

 - 'livepatch' will read patch instructions from standard input.
   You can write them in a file or pass them through pipe.

EXAMPLES

 run a target process in some terminal
  $ ./target 

 apply patch with 'livepatch' in another terminal

  $ echo 'dl foo patch.so
  jmp func_J $foo:func1
  set str_P addr $foo:patch_message' | livepatch $(pidof target) ./target

Then, target's func_J function is replaced with func1 function in patch.so
and target's str_P pointer variable points to patch_message in patch.so.

FILES
 Makefile 	- makefile
 README   	- this file
 livepatch.c	- souce file of livepatch
 bfd.c		- bfd test program while hacking livepatch
 fixup.c	- fixuping test program while hacking livepatch
 fixup.txt	- fixup memo from glibc investigation
                  and http://ukai.jp/debuan/2002w/elf.txt 

AUTHOR
  Fumitoshi UKAI <ukai@debian.or.jp>

COPYING
 * Copyright (C) 2004 Fumitoshi UKAI <ukai@debian.or.jp>
 * All rights reserved.
 * This is free software with ABSOLUTELY NO WARRANTY.
 *
 * You can redistribute it and/or modify it under the terms of 
 * the GNU General Public License version 2.

TODO
- TLS
- symbol versioning
- GOT hooking (ltrace?)
- linux/i386 architecture only. 
  even if target_alloc() is ported, maybe unportable in some part 
  (data size, alignment, ...)
- changing a pointer variable may not work correctly, because its value
  is already copied in some other variables, stacks or registers
- changing non volatile pointer may not be reflected in process execution
  because its pointer may be stored in register.
- check regs/stack before patching.
- interactive mode with readline?
- dynamic shlib replacement? 
  (e.g. libc.so upgrading without restarting daemon)
- language binding (ruby?)
- undo modification?
- gdb script?

http://ukai.jp/Software/livepatch/
