# parses REQ text to PDB format:
# MAGVAR        LATITUDE    LONGITUDE
#  (DEG)        (DEG)       (DEG)
# -24.7948      -84.3750    .0000
# -22.0360      -78.7500    .0000
# ...           ...         ...
# -3.2892       84.3750     .0000
# -29.7402      -84.3750    5.6250
# -26.5415      -78.7500    5.6250
# 1.3585        84.3750     5.6250
# ...           ...         ...
# -34.7337      -84.3750    11.2500
# -31.1327      -78.7500    11.2500
#   ...           ...           ...
# # TO:
# MAGVARTBL[row,col] =       MAGVAR    ;  (   LATITUDE       LONGITUDE)
# MAGVARTBL[ 0, 0] =         -24.7948  ;  (   -84.3750       0.0000   )
# MAGVARTBL[ 0, 1] =         -22.0360  ;  (   -78.7500       0.0000   )
#   ...           ...              ...
# MAGVARTBL[ 0,30] =          -3.2892  ;  (    84.3750       0.0000   )
# 
# MAGVARTBL[ 1, 0] =         -29.7402  ;  (   -84.3750       5.6250   )
# MAGVARTBL[ 1, 1] =         -26.5415  ;  (   -78.7500       5.6250   )
#   ...           ...              ...
# MAGVARTBL[ 1,30] =           1.3585  ;  (    84.3750       5.6250   )
# 
# MAGVARTBL[ 2, 0] =         -34.7337  ;  (   -84.3750      11.2500   )
# MAGVARTBL[ 2, 1] =         -31.1327  ;  (   -78.7500      11.2500   )
#   ...           ...              ...

import sys
import re

def func(src_path):
    if (None == src_path):
        return -1
    
    try:
        file_in = open(src_path)
        file_out = open("db.dat", mode = 'w')
    except OSError as e:
        print("Failed to open file {0}: {1}".format(src_path, e.strerror), file = sys.stderr)
        return -1
    
    row = 0
    col = -1    
    col_val = 0.0000
    for line in file_in:
        if (None != re.search(r'\d+', line)):
            splits = line.strip("\n ").split(maxsplit = 3)
            if (len(splits) < 3):
                continue
            
            # if one section is end
            if (abs(col_val - float(splits[2])) > 1):
                col_val = float(splits[2])
                row += 1
                col = 0
                print(file = file_out)
            else:
                col += 1
            
            print("MAGVARTBL[{row:2},{col:2}] = {val:16,.4f}  ;  ({lat:11,.4f}{lon:13,.4f}   )".format(\
                  row = row, col = col, val = float(splits[0]), lat = float(splits[1]), lon = float(splits[2])), file = file_out)


if ("__main__" == __name__):
    if (len(sys.argv) > 1):
        func(sys.argv[1])