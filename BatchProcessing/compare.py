#!/usr/bin/env python3
# compare corresponding files under two directories

import sys
import os
import shutil
import subprocess


def work(old_dir, new_dir):
    if (None == old_dir or None == new_dir):
        print("Invalid path", file = sys.stderr)
        return -1
    
    old_file = None
    new_file = None
    for root, dirs, files in os.walk(old_dir):        
        for file in files:            
            old_file = os.path.join(old_dir, file)
            new_file = os.path.join(new_dir, file)
            if (os.path.isfile(new_file)):
                print('ECHO \"--------------------------- ' + file + ' --------------------------- \">> result.txt')
                #subprocess.Popen([r"D:\Program Files\Git\bin\diff.exe", "--unchanged-line-format=\"\"", "--old-line-format=\"\"", "--new-line-format=\"line %dn: %L\"", old_file, new_file])
                print("\"D:\\Program Files\\Git\\bin\\diff.exe\"" + ' --unchanged-line-format="" --old-line-format="" --new-line-format="(%%dn) %%L"' \
                + " " + old_file + " " + new_file + " >> result.txt")
            else:
                print('No corresponding file named ' + file + ' in ' + new_dir, file = sys.stderr)
        
    return 0
    

if ('__main__' == __name__):
    if (len(sys.argv) > 2):
        work(sys.argv[1], sys.argv[2])
    else:
        print("usage: python {me} old_dir new_dir".format(me = sys.argv[0]))
                        

