#!/usr/bin/python3
# search SRD files and then trace to TRT files
# SRD_FILE_NAME; ANCHOR; ALLOCATION; TRT1, TRT2, TRT3 ...; 

import sys
import os
import re
import shutil


def srd_2_tst(srd_anchor, tst_path):
    result = ""
    if (None == srd_anchor or None == tst_path):
        print("Invalid SRD path or tst path.", file = sys.stderr)
        return result
    
    # 
    for root, dirs, files in os.walk(tst_path):
        for file in files:
            tst_file = open(os.path.join(tst_path, file), 'r')
            if (srd_anchor in tst_file.read().upper()):
                result += file + ","
            tst_file.close()
    
    return result.strip(', ')


# srd_anchor is in upper case
def srd_2_trt(srd_anchor, trt_list_file):
    result = ""
    if (None == srd_anchor or None == trt_list_file):
        print("Invalid SRD path or trt list file.", file = sys.stderr)
        return result
    
    # BITE_B717_BITE_HISTORY.TRT; B717; BITE_SRD_5501
    pattern = re.compile(r'(\S+\.TRT);\s(.+);\s(\S+)', re.IGNORECASE)
    
    trt_list_file.seek(0)
    
    for line in trt_list_file:
        match = pattern.match(line)
        if (None != match):
            if (srd_anchor == match.group(3).upper()):
                result += match.group(1) + ", "
    
    return result.strip(', ')
    

def setup_trace(srd_list_path, trt_list_path):
    if (None == srd_list_path or None == trt_list_path):
        print("Invalid SRD path or output file.", file = sys.stderr)
        return False
            
    try:
        srd_list_file = open(srd_list_path)
        trt_list_file = open(trt_list_path, 'r')  # avoid opening multiple times
        file_out = open('SRD_TO_TST.txt', 'w')
    except OSError as e:
        print("Cannot open at least one file.", file = sys.stderr)
        return False
        
    # SRD_FILE_NAME; ANCHOR; ALLOCATION
    # AMI_ACCESS_MDXX.SRD; AMIOPC_SRD_1633; MD10, MD11, 717-C1;
    pattern = re.compile(r'(\S+\.SRD);\s(\S+);\s(.+)', re.IGNORECASE)
    
    for line in srd_list_file:
        match = pattern.match(line)
        if (None != match):
            print("{srd_file_name}; {anchor}; {alloc}; {trt}".format(
                srd_file_name = match.group(1), anchor = match.group(2), alloc = match.group(3),
                trt = srd_2_tst(match.group(2).upper(), os.path.dirname(trt_list_path))),
                file = file_out, end = '\n')
        
    trt_list_file.close()
    srd_list_file.close()
    file_out.close()


if ("__main__" == __name__):
    if (len(sys.argv) > 2):
        setup_trace(sys.argv[1], sys.argv[2])
    else:
        print("usage: python {me} srd_list_path trt_list_path".format(me = sys.argv[0]))
                        

