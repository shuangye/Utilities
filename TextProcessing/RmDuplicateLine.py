#!/usr/bin/env python3
# remove duplicate lines from a file

import sys
import os

def work(src_path, dest_path):
    if (None == src_path or None == dest_path):
        print("Invalid path", file = sys.stderr)
        return -1
    
    for root, dirs, files in os.walk(src_path):        
        for file in files:    
            basename, extension = os.path.splitext(file)
            if (".CUL" == extension.upper()):
                filename_in = os.path.join(src_path, file)
                filename_out = os.path.join(dest_path, file)
    
                lines_seen = set() # holds lines already seen
                file_out = open(filename_out, "w")
                for line in open(filename_in, "r"):
                    LINE = line.strip().upper()
                    if LINE not in lines_seen: # not a duplicate
                        # file_out.write(LINE)
                        print(LINE, file = file_out)
                        lines_seen.add(LINE)
                file_out.close()
    

if (len(sys.argv) > 2):
    work(sys.argv[1], sys.argv[2])
else:
    print("usage: python {me} src_path dest_path".format(me = sys.argv[0]))
                        

