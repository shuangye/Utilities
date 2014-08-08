# 

import sys
import re

def func(old_path, new_path):
    if (None == old_path or None == new_path):
        return -1
    
    try:
        old_file = open(old_path)
        new_file = open(new_path)
    except OSError as e:
        print("Failed to file for comparing".format(src_path, e.strerror), file = sys.stderr)
        return -1
    
    consistent = True
    old_file_line = old_file.readline()
    new_file_line = new_file.readline()
    while ('' != old_file_line and '' != new_file_line):
        if (old_file_line.upper() != new_file_line.upper()):
            consistent = False
            break
    
        old_file_line = old_file.readline()
        new_file_line = new_file.readline()
    
    
    pattern = re.compile(r"TESTID\s*:\s*\d+", re.IGNORECASE)  # TESTID: 2
    for line in file_in:
        if (None != pattern.match(line.strip())):
            print("TESTID: {ID}".format(ID = ID), file = file_out)
            ID += 1
        else:
            print(line, end = '', file = file_out)
            
    old_file.close()
    new_file.close()
    if (consistent):
        return 0
    else:
        return 1


if ("__main__" == __name__):
    if (len(sys.argv) > 1):
        func(sys.argv[1])