#!/usr/bin/python3
# remove "BLD_922RL101001" from a file name

import sys
import os
import re
import shutil



def work(src_path, dest_path):
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
    

if (len(sys.argv) > 2):
    work(sys.argv[1], sys.argv[2])
else:
    print("usage: python {me} src_path dest_path".format(me = sys.argv[0]))
                        

