#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <stdio.h>
#include <errno.h>
#include "interfaces.h"

/* traverse the whole directory and/or all its (possible) sub-directories */
int traverse(const char * path, const char * keyword)
{
        DIR *dir = NULL;
        struct dirent * entry = NULL;
        struct stat status;        
  	char filename[MAXPATH] = { '\0' };
        
        if (NULL == (dir = opendir(path))) {
				fprintf(stderr, "failed to open dir %s\n", path);
                return -1;
        }

#ifdef _DEBUG
		fprintf(stdout, "traversing dir %s\n", path);
#endif
		
        while (entry = readdir(dir)) {
				snprintf(filename, sizeof(filename), "%s/%s", path, entry -> d_name);
                if (-1 == stat(filename, &status)) {      
						fprintf(stderr, "failed to get file %s 's information: %s\n", filename, strerror(errno));
                        continue;
				}

                /* regular file */
                if (S_ISREG(status.st_mode)) {
                        /* do business logics */						
                        search(filename, keyword);						
						/* one file cannot be a regular file and a dir at the same time */
						continue;
                }

                /* directory */
                if (is_recursive && S_ISDIR(status.st_mode)) {
					/* filter . and .. */
					if (0 == strcmp(entry -> d_name, ".") || 0 == strcmp(entry -> d_name, ".."))
                        continue;
					                    
                    /* recursive */
                    traverse(filename, keyword);
                }
        }

        return closedir(dir);
}
