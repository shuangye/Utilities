#!/usr/bin/python3
# calc running duration from .VER or .RST files.

import sys
import os
import re
import time
import datetime


def parse_time(time_str):
    if (None == time_str):
        return None

    time_struct = None
    time_str_clean = time_str.strip("\n\" ")    
    
    try:                            
        time_struct = time.strptime(time_str_clean, "%b %d %H:%M:%S %Y")
    except ValueError:
        try:
            time_struct = time.strptime(time_str_clean, "%m/%d/%Y %a %H:%M:%S")
        except ValueError:
            try:
                time_struct = time.strptime(time_str_clean, "%m-%d-%y %a %H:%M:%S")
            except ValueError:
                try:
                    # Wed 10/15/2014 15:39:10
                    time_struct = time.strptime(time_str_clean, "%a %m/%d/%Y %H:%M:%S")
                except ValueError:
                    # I have tried my best
                    return None;
                
    return time_struct
 
 
def parse_file(file_path):
    start_time = None
    end_time = None
    
    try:
        file_in = open(file_path)
    except OSError as e:
        print("Failed to open file " + file_path + "for reading: " + str(e.errno) + e.strerror, file = sys.stderr)
        return None, None
        
    try:
        for line in file_in:
            if (re.match("Test Start Time:", line)):                
                start_time = parse_time(line.split(":", 1)[1])                
            elif (re.match("Test End Time:", line)):                
                end_time = parse_time(line.split(":", 1)[1])
                
    except UnicodeDecodeError:
        print("There are unrecognized characters in " + file_path, file = sys.stderr)
        
    finally:
        file_in.close()
        return start_time, end_time


def main(path, result_path):
    print("main")
    if (None == path or None == result_path):
        print("Invalid path", file = sys.stderr)
        return -1

    try:
        file_out = open(result_path, "w")
    except OSError as e:
        print("Failed to open file " + result_path + "for writing: " + str(e.errno) + e.strerror, file = sys.stderr)
        return -1    

    total_count = 0;  # how many files parsed
    failure_count = 0

    for root, dirs, files in os.walk(path):        
        for item in files:
            file_path = os.path.join(path, item)
            fileName, extension = os.path.splitext(file_path)
            if (".RST" == extension.upper() or ".VER" == extension.upper()):                
                print("Parsing " + file_path)
                start_time, end_time = parse_file(file_path)
                if (None == start_time or None == end_time):
                    print("Test Start/End Time not retrieved from " + file_path, file = sys.stderr)
                    failure_count += 1
                else:                
                    # delta_time = datetime.fromtimestamp(mktime(end_time)) - datetime.fromtimestamp(mktime(start_time))
                    # year and month ignored
                    delta_minutes = (end_time.tm_mday - start_time.tm_mday) * 24 * 60 + \
                                    (end_time.tm_hour - start_time.tm_hour) * 60 + \
                                    (end_time.tm_min - start_time.tm_min) + \
                                    1  # seconds count as 1 minute
                    print(item + ", " + str(delta_minutes), file = file_out)
                total_count += 1
    
    file_out.close()
    print("Parsed {count} file(s), {fail} failure(s).\nTime measured in minutes. Year and month are ignored.".format(count = total_count, fail = failure_count))
    return 0
    

if ("__main__" == __name__):
    if (len(sys.argv) > 2):        
        main(sys.argv[1], sys.argv[2])
    else:
        print("usage: python {me} path result".format(me = sys.argv[0]))
                        

