#!/usr/bin/python3
# search SRD files and then trace to TRT files
# ANCHOR; TRT1, TRT2, TRT3 ...; ALLOCATION

import sys
import os
import re
import shutil


def req2tst_trace(req_anchor, trt_path, file_out):
    if (None == req_anchor or None == trt_path):
        print("Invalid TRT path or REQ anchor.", file = sys.stderr)
        return -1

    for root, dirs, files in os.walk(trt_path):        
        for file in files:            
            basename, extension = os.path.splitext(file)
            components = basename.split("-", 2)
            if (".TRT" == extension.upper()):
                # search this .TRT file
                file_trt = open(os.path.join(trt_path, file), "r")
                for line in file_trt:
                    if ('!' in line):
                        continue
                    if (req_anchor.upper() in line.upper()):
                        print(file, file = file_out, end = ", ")
                        break
                file_trt.close()
                
    print("; ", file = file_out, end = '')
                    
                
                

def parse_srd(srd_path, trt_path, file_out):
    if (None == srd_path or None == file_out):
        print("Invalid SRD path or output file.", file = sys.stderr)
        return False
      
    # ANCHOR :<Tab>PERF_SRD_23155
    # ALLOCATION:<Tab>A340, A320
    pattern_anchor = re.compile(r"ANCHOR\s*:\s*(<Tab>)*\s*(\w+){1}", re.IGNORECASE)
    pattern_alloc = re.compile(r"ALLOCATION\s*:\s*(<Tab>)*\s*(.+)", re.IGNORECASE)
    
    success = True
    file_srd = open(srd_path)
    
    try:
        for line in file_srd:
            match = pattern_anchor.search(line)
            if (None != match):
                print(os.path.basename(srd_path), file = file_out, end = '; ')
                print(match.group(2), file = file_out, end = '; ')
                #req2tst_trace(match.group(2), trt_path, file_out)
                
            match = pattern_alloc.search(line)
            if (None != match):
                print(match.group(2), file = file_out, end = ';\n')
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError in " + srd_path, file = sys.stderr)
        success = False
    
    file_srd.close()
    return success


def work(srd_path, trt_path):
    if (None == srd_path or None == trt_path):
        print("Invalid path", file = sys.stderr)
        return -1
    
    try:
        file_out = open("result.txt", mode = "w")
    except OSError as e:
        print("Failed to open result file for writing: {1}".format(e.strerror), file = sys.stderr)
        return -2
    
    parsed_file_count = 0
    for root, dirs, files in os.walk(srd_path):        
        for file in files:            
            basename, extension = os.path.splitext(file)
            components = basename.split("-", 2)
            if (".SRD" == extension.upper()):
                if (parse_srd(os.path.join(srd_path, file), trt_path, file_out)):
                    parsed_file_count += 1
                else:
                    print("Failed to process " + file)
    
    file_out.close()
    return parsed_file_count

if ("__main__" == __name__):
    if (len(sys.argv) > 2):
        print("Processed file count: " + str(work(sys.argv[1], sys.argv[2])), file = sys.stdout)
    else:
        print("usage: python {me} srd_path trt_path".format(me = sys.argv[0]))
                        

