#include <string.h>
#include <errno.h>
#include <stdio.h>
#include "interfaces.h"

/* search for the specified keyword(s) in one file, line by line */
int search(const char * filename, const char * keyword)
{
        FILE *fp = NULL;
        char buffer[LINELENGTH] = { '\0' };
        long lineno = 1;
  	int error_code = 0;

        if (NULL == (fp = fopen(filename, "r"))) {
				error_code = errno;
                fprintf(stderr, "failed to open file %s: %s\n", filename, strerror(error_code));
                return error_code;
        }
		
#ifdef _DEBUG
		fprintf(stdout, "searching file %s\n", filename);
#endif

		/* avoiding too many decisions to improve performance */
		if (is_case_sensitive) {
        	while (!feof(fp)) {
    	            fgets(buffer, sizeof(buffer), fp);
	                if (strstr(buffer, keyword)) {
                    	    fprintf(stdout, "%s line# %ld: %s", filename, lineno, buffer);        
                	}
            	    ++lineno;
        	}
		}

		else {
        	while (!feof(fp)) {
    	            fgets(buffer, sizeof(buffer), fp);
	                if (strcasestr(buffer, keyword)) {
                    	    fprintf(stdout, "%s line# %ld: %s", filename, lineno, buffer);        
                	}
            	    ++lineno;
        	}
		}

        ++file_counter;
        return fclose(fp);
}
