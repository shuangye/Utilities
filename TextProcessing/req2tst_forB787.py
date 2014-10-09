#!/usr/bin/python3
# trace SRD/SDD to test by searching for .TRT files

import sys
import os
import re

FILE_NAME_OF_COLLECTED_TRT_ANCHORS = 'TRT.txt'

# output as this format: TRT_FILE_NAME; ANCHOR;
def collect_trt_anchors(trt_dir):
    if (None == trt_dir):
        print("Invalid .TRT path.", file = sys.stderr)
        return False
    
    try:
        file_out = open(FILE_NAME_OF_COLLECTED_TRT_ANCHORS, 'w')
    except OSError as e:
        print("Cannot open TRT.txt for writing." + e.strerror, file = sys.stderr)
        return False

    # B787	SDD  PERF_TEST_198936  PERF_SDD_253469
    pattern = re.compile(r"(B787)\s+(\w+)\s+(\w+)\s+(\w+)")
    
    for root, dirs, files in os.walk(trt_dir):
        for file in files:
            basename, extension = os.path.splitext(file)
            if (".TRT" == extension.upper()):
                trt = open(os.path.join(trt_dir, file), 'r')
                for line in trt:
                    match = pattern.match(line.strip())
                    if (None != match):
                        print('{file_name}; {anchor};'.format(file_name = file.upper(), anchor = match.group(4)), file = file_out)
                trt.close()
                
    file_out.close()
    return True

# anchor is in upper case
def req2trt(anchor, collected_anchor_list_file):
    result = ""
    if (None == anchor or None == collected_anchor_list_file):
        print("Invalid SRD path or trt list file.", file = sys.stderr)
        return result
    
    # BITE_B717_BITE_HISTORY.TRT; BITE_SRD_5501;
    pattern = re.compile(r'(\S+\.TRT);\s(\S+);', re.IGNORECASE)
    
    collected_anchor_list_file.seek(0)    
    for line in collected_anchor_list_file:
        match = pattern.match(line)
        if (None != match):
            if (anchor == match.group(2).upper()):
                result += match.group(1) + ", "
    
    return result.strip(', ')
    

def work(input_anchor_list, trt_dir):
    if (None == input_anchor_list or None == trt_dir):
        print("Invalid input anchor list or .TRT path.", file = sys.stderr)
        return False
        
    try:
        input_anchor_list_file = open(input_anchor_list)
        # avoid opening multiple times
        collected_anchor_list_file = open(FILE_NAME_OF_COLLECTED_TRT_ANCHORS, 'r')          
    except OSError as e:
        print("Cannot open necessary files.", file = sys.stderr)
        return False
        
    # an anchor per line
    pattern = re.compile(r'\S+')    
    for line in input_anchor_list_file:
        match = pattern.match(line)
        if (None != match):
            anchor = match.group().upper()
            print("{anchor}; {trt};".format(
                anchor = anchor,
                trt = req2trt(anchor, collected_anchor_list_file)))                
        
    input_anchor_list_file.close()
    collected_anchor_list_file.close()   


if ("__main__" == __name__):  
    if (2 < len(sys.argv)):
        # conditional
        if (3 < len(sys.argv) or not os.path.isfile(FILE_NAME_OF_COLLECTED_TRT_ANCHORS)):   
            if (not collect_trt_anchors(sys.argv[2])):
                print('Failed to collect trt anchors', file = sys.stderr)                
        
        work(sys.argv[1], sys.argv[2])
    else:
        print("usage: python {me} input_anchor_list_path trt_dir".format(me = sys.argv[0]))
                        

