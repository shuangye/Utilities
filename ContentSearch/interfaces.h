#ifndef _CONTENT_SEARCH_INTERFACES_H_
#define _CONTENT_SEARCH_INTERFACES_H_

/* Macro definitions */
#define MAXPATH 1024
#define LINELENGTH 1024  			/* max length of one line */

/* global variables */
extern int is_case_sensitive;		/* boolean: is keywords case-sensitive? */
extern int is_recursive;			/* boolean: dive into sub-directories? */
extern long long file_counter; /* number of files visited */

/* APIs */
int traverse(const char * path, const char * keyword);
int search(const char * filename, const char * keyword);

#endif
