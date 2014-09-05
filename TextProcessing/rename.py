#!/usr/bin/python3

import sys
import os
import re
import shutil



def rename(src_path, dest_path):
    if (None == src_path or None == dest_path):
        print("Invalid path", file = sys.stderr)
        return -1
    
    for root, dirs, files in os.walk(src_path):        
        for item in files:            
            basename, extension = os.path.splitext(item)
            components = basename.split("-", 2)
            if (".XLSM" == extension.upper() and "BLD_922RL101001" == components[1].upper()):                
                shutil.copyfile(os.path.join(src_path, item), os.path.join(dest_path, components[0] + extension))
        
    return 0
    
def copy(list_file_path, src_path, dest_path):
    if (None == list_file_path or None == src_path or None == dest_path):
        print("Invalid path", file = sys.stderr)
        return -1
    
    processed_file_count = 0
    list_file = open(list_file_path, 'r')
    for line in list_file:
        line = line.strip()
        src_file = os.path.join(src_path, line)
        if (os.path.isfile(src_file)):
            # shutil.copy2(src_file, dest_path)
            processed_file_count += 1
        else:
            print(line + "does not exist.", file = sys.stderr)
    list_file.close()
    return processed_file_count

if (len(sys.argv) > 3):
    print("Processed file count: " + str(copy(sys.argv[1], sys.argv[2], sys.argv[3])), file = sys.stdout)
else:
    print("usage: python {me} src_path dest_path".format(me = sys.argv[0]))
                        

