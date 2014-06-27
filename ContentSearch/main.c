#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include "interfaces.h"

/* global variable definitions */
int is_case_sensitive = 1;  /* boolean: is keywords case-sensitive? */
int is_recursive = 0;       /* boolean: dive into sub-directories? */
long long file_counter = 0; /* number of files visited */

void show_help(FILE *stream, const char * program_name)
{
    fprintf(stream, "How to use: %s [OPTIONS] dir_path keyword\n", program_name);
    fprintf(stream, "-h, --help: show this help message\n");
    fprintf(stream, "-i, --ignore-case: case-insensitive for keyword\n");
    fprintf(stream, "-r, -R, --recursive: dive into sub-directories recursively\n");
}

/* program [OPTIONS] dir_path keywords */
void parse_options(int argc, char * argv[])
{
    int next_option;
    const char * const short_options = "hirR";
    const struct option long_options[] = {
        { "help", 0, NULL, 'h' },
        { "ignore-case", 0, NULL, 'i' },
        { "recursive", 0, NULL, 'r' },
        { "recursive", 0, NULL, 'R' },
        {NULL, 0, NULL, 0}
    };
    
    do {
        switch (next_option = getopt_long(argc, argv, short_options, long_options, NULL)) {
        case 'h':
            show_help(stdout, argv[0]);
            exit(EXIT_SUCCESS);
            break;
        case 'i':
            is_case_sensitive = 0;
            break;
        case 'r':
        case 'R':
            is_recursive = 1;
            break;
        default:
            break;
        }
    } while ( next_option != -1 );
}

int main(int argc, char * argv[])
{
        parse_options(argc, argv);

        if (!argv[optind] || !argv[optind + 1]) {
                show_help(stderr, argv[0]);
                return -1;
        }

        if (0 == traverse(argv[optind], argv[optind + 1])) {
            fprintf(stdout, "Visited %lld file(s)\n", file_counter);
            return 0;
        }
        else {
            return -1;
        }
}
