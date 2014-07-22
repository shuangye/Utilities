# parses the .RST results and writes them to a CSV file

import sys
import string
import re

def is_number(string):
    try:
        float(string) or int(string)
        return True
    except ValueError:
        return False

def work(rst_path):    
    if (None == rst_path):
        print("Invalid argument")
        return -1

    try:
        file_in = open(rst_path)
    except OSError as e:
        print("Failed to open file " + rst_path + "for parsing: " + str(e.errno) + e.strerror)    
        return -1

    try:
        file_out = open(rst_path + ".out", mode = "a")
    except OSError as e:
        print("Failed to open file for writing result: " + str(e.errno) + e.strerror)    

    output_context = False
    splits = [10]
    for line in file_in:
        if (re.match("TESTID:", line)):
            print("\nTC " + re.findall(r'\d+', line)[0], end = ", ", file = file_out)
        if (re.match("INPUT", line)):
            output_context = False
            continue
        if (re.match("OUTPUT", line)):
            output_context = True
            continue
        if (re.match("====>", line)):
            output_context = False
            continue

        if (True == output_context):
            splits = line.strip("- \n").split()
            # print(splits)
            if (len(splits) > 3 and is_number(splits[-2])):  # filter
                print(splits[0] +", " + splits[-2], end = ", ", file = file_out)

    file_in.close()
    file_out.close()

    
    
if (len(sys.argv) < 2):
    print("usage: {0} .rst_path".format(sys.argv[0]))
    sys.exit(-1)
else:
    work(sys.argv[1])
    
