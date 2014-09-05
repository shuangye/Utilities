import sys
import os
import re

def parse_trace(trace_file_path, file_out):
    if (None == trace_file_path or None == file_out):
        print("Invalid trace file path or output file.", file = sys.stderr)
        return -1
    
    # B717          SRD       717C2_CDCK_TEST_0380     CDCK_SRD_14560
    pattern = re.compile(r"(\w+)\s+(\w+)\s+(\w+)\s+(\w+)")
    
    file_trace = open(trace_file_path, "r")
    try:
        for line in file_trace:
            if ('!' in line):
                continue
            
            match = pattern.search(line)
            if (None != match):
                print('{file_name}; {alloc}; {srd}'.format(file_name = os.path.basename(trace_file_path),
                        alloc = match.group(1), srd = match.group(3)), file = file_out)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError in " + trace_file_path, file = sys.stderr)
        
    file_trace.close()
    
def work(trace_path):
    if (None == trace_path):
        print('Invalid trace path.', file = sys.stderr)
        return -1
        
    try:
        file_out = open("result.txt", mode = "a")
    except OSError as e:
        print("Failed to open result file for writing: {1}".format(e.strerror), file = sys.stderr)
        return -2
        
    parsed_file_count = 0
    for root, dirs, files in os.walk(trace_path):        
        for file in files:            
            basename, extension = os.path.splitext(file)            
            if (".TRR" == extension.upper()):
                parse_trace(os.path.join(trace_path, file), file_out)
                parsed_file_count += 1
    
    file_out.close()
    return parsed_file_count

if ("__main__" == __name__):
    if (len(sys.argv) > 1):
        print("Processed file count: " + str(work(sys.argv[1])), file = sys.stdout)
    else:
        print("usage: python {me} srd_path trt_path".format(me = sys.argv[0]))
                       