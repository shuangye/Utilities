#!env python3

import sys
import os
import re

cul_collection_file_name = "CUL_COLLECTION.TXT"


# writes all contents in upper case
def parse_cul_file(cul_file_path, file_cul_collection):
    if (None == cul_file_path or None == file_cul_collection):
        return
        
    file_cul = open(cul_file_path)
    pattern_cul_entry = re.compile(r"(\w+)\.(ADA|C|CPP)")
    for line in file_cul:
        if ("#" in line):
            continue
        line = line.upper()
        match = pattern_cul_entry.match(line)
        if (None != match):
            print("{cul_base_name}; {cul_entry}".format(
                    cul_base_name = os.path.splitext(os.path.basename(cul_file_path))[0].upper(),
                    cul_entry = line),
                    file = file_cul_collection, end = ""
                 )
        

def collect_cul(cul_dir_path):
    if (None == cul_dir_path):
        return
    
    try:
        file_cul_collection = open(cul_collection_file_name, "w")
    except OSError as e:
        return
    
    for root, dirs, files in os.walk(cul_dir_path):
        for file in files:
            base, ext = os.path.splitext(file)
            if (".CUL" == ext.upper()):
                parse_cul_file(os.path.join(cul_dir_path, file), file_cul_collection)
                
    file_cul_collection.close()

    
##########################################################################################
    
    
def trace_tst(code_file_name, file_cul_collection, file_out):
    if (None == code_file_name or None == file_cul_collection or None == file_out):
        return
        
    file_cul_collection.seek(0)
    for line in file_cul_collection:
        if (code_file_name in line):
            print("{code}, {tst}".format(code = code_file_name, tst = line.split(";")[0]), file = file_out)


def work(file_in_path, file_out_path):            
    try:
        file_cul_collection = open(cul_collection_file_name)            
        file_in = open(file_in_path)
        file_out = open(file_out_path, "w")
    except OSError as e:
        return
        
    pattern_code_name = re.compile(r"(\w+)\.(ADA|SRC|C|H|CPP)", re.IGNORECASE)
    for line in file_in:
        match = pattern_code_name.search(line)
        if (None != match):
            trace_tst(match.group(1).upper(), file_cul_collection, file_out)
    
    file_cul_collection.close()   
    file_in.close()
    file_out.close()


##########################################################################################    
    
# program cul_dir_path file_in file_out
    
if ("__main__" == __name__):
    if (len(sys.argv) > 3):
        if (not os.path.isfile(cul_collection_file_name)):
            collect_cul(sys.argv[1])
        work(sys.argv[2], sys.argv[3])
    else:
        print("Usage: {0} cul_dir_path file_in file_out".format(sys.argv[0]), file = sys.stderr)
