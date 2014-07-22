# re-orders TESTID numbers

import sys
import re

def func(src_path):
    if (None == src_path):
        return -1
    
    try:
        file_in = open(src_path)
        file_out = open(src_path + ".ordered", mode = 'w')
    except OSError as e:
        print("Failed to open file {0}: {1}".format(src_path, e.strerror), file = sys.stderr)
        return -1

    ID = 1  # TESTID starts from 1
    valid = re.compile(r"TESTID\s*:\s*\d+", re.IGNORECASE)  # TESTID: 2
    for line in file_in:
        if (None != valid.match(line.strip())):
            print("TESTID: {ID}".format(ID = ID), file = file_out)
            ID += 1
        else:
            print(line, end = '', file = file_out)


if ("__main__" == __name__):
    if (len(sys.argv) > 1):
        func(sys.argv[1])