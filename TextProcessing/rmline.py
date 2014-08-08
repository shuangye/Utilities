# remove certain lines from a file

import sys
import re

def func(src_path, pattern):
    if (None == src_path or None == pattern):
        return -1
    
    try:
        file_in = open(src_path)
        file_out = open(src_path + ".rm", mode = 'w')
    except OSError as e:
        print("Failed to open file {0}: {1}".format(src_path, e.strerror), file = sys.stderr)
        return -1

    found = re.compile(pattern, re.IGNORECASE)
    for line in file_in:
        if (None == found.search(line)):
            print(line, end = '', file = file_out)

    file_in.close()
    file_out.close()


if ("__main__" == __name__):
    if (len(sys.argv) > 2):
        func(sys.argv[1], sys.argv[2])