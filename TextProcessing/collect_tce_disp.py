#! /usr/bin/env python3
# parse .TCE files to collect these info:
# subunit, tce file name, disposition

import sys
import os
import re

def parse_tce_file(tce_file_path, file_out):
    if (None == tce_file_path or None == file_out):
        return False
    
    # SubUnit: CDK_EXT_DPKG.OUTPUT_FLIGHT_NUMBER
    pattern_subunit = re.compile(r"SubUnit:\s*(\S+)", re.IGNORECASE)
    # {inline}
    pattern_disp = re.compile(r"\s*({.+})\s*")            

    subunit = None
    disposition = None
    print('Processing ' + tce_file_path)
    
    file_in = open(tce_file_path, 'r')
    for line in file_in:        
        match = pattern_subunit.match(line)
        # meet a new subunit
        if (None != match):            
            # write prev result
            if (None != subunit):                
                print('{name}; {subunit}; {disp}'.format(name = os.path.basename(tce_file_path), \
                       subunit = subunit, disp = disposition), file = file_out)

            # reset parsed result
            disposition = ''
            subunit = match.group(1)            

        match = pattern_disp.match(line)
        if (None != match):
            disposition += match.group(1) + ', '
    
    # write the last match unconditionally
    print('{name}; {subunit}; {disp}'.format(name = os.path.basename(tce_file_path), \
                       subunit = subunit, disp = disposition), file = file_out)
    file_in.close()


def work(file_list, result):
    if (None == file_list or None == result):
        print('Bad parameter.', file = sys.stderr)
        return False

    try:
        file_out = open(result, 'w')
    except OSError as e:
        print('Failed to open file ' + result + ' for writting: ' + e.strerror, file = sys.stderr)
        return False

    base_dir = r'\\159.99.234.164\fms\MD-11\MD11_Coverage\TCR_NEW_0813\!100\Closed'
    for line in open(file_list, 'r'):
        tce_file_path = os.path.join(base_dir, line.strip())
        if (os.path.isfile(tce_file_path)):
            parse_tce_file(tce_file_path, file_out)
        else:
            print('File does not exist: ' + tce_file_path)

    file_out.close()


if ('__main__' == __name__):

    if (len(sys.argv) > 2):
        work(sys.argv[1], sys.argv[2])
    else:
        print('usage', file = sys.stderr)
