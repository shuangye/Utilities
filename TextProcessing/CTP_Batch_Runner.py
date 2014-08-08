# 
# input file line format: CTP_NAME.TDF[, CTP_NAME.ZIP] [, TDF_GEN]
# If CTP_NAME.ZIP is not present, the same base file name with CTP_NAME.TDF is assumed;
# If TDF_GEN is not present, the newest generation is assumed.
# ZIP_GEN is always assumed to be the newest generation.

import sys
import re
import os
import multiprocessing

EID = 'E817739'
PWD = 'Work99999'

def parse_input_file(src_path, fetch_base_path):
    if (None == src_path or None == fetch_base_path):
        print('Invalid parameter.', file = sys.stderr)
        return None
    
    try:
        file_in = open(src_path)
        file_out = open(src_path + ".bat", mode = 'w')
    except OSError as e:
        print("Failed to open file {0}: {1}".format(src_path, e.strerror), file = sys.stderr)
        return None

    ctp_path_list = []
    ctp_base_name = None   
    tdf_gen = 0
    # CTP_NAME.TDF, CTP_NAME.ZIP, 8
    pattern1 = re.compile(r'([a-zA-Z0-9_]+\.TDF)\s*,\s*([a-zA-Z0-9_]+\.ZIP)\s*,\s*(\d+)', re.IGNORECASE)
    # CTP_NAME.TDF, 8
    pattern2 = re.compile(r'([a-zA-Z0-9_]+\.TDF)\s*,\s*(\d+)', re.IGNORECASE)
    # CTP_NAME.TDF
    pattern3 = re.compile(r'[a-zA-Z0-9_]+\.TDF', re.IGNORECASE)
    
    for line in file_in:
        match = pattern1.match(line.strip())
        if (None != match):
            tdf_name = match.group(1)
            zip_name = match.group(2)
            tdf_gen = int(match.group(3))
            ctp_base_name = tdf_name.upper().rstrip('.TDF')
        else:
            match = pattern2.match(line.strip())
            if (None != match):
                tdf_name = match.group(1)
                zip_name = tdf_name.upper().rstrip('TDF') + 'ZIP'
                tdf_gen = int(match.group(2))
                ctp_base_name = tdf_name.upper().rstrip('.TDF')
            else:
                match = pattern3.match(line.strip())
                if (None != match):
                    tdf_name = match.group()
                    zip_name = tdf_name.upper().rstrip('TDF') + 'ZIP'
                    tdf_gen = 0
                    ctp_base_name = tdf_name.upper().rstrip('.TDF')
        
        # if the line is not in proper format
        if (None == ctp_base_name):
            continue

        target_fetch_path = os.path.join(fetch_base_path, ctp_base_name)        
        if (not os.path.exists(target_fetch_path)):
            os.makedirs(target_fetch_path)
        if (target_fetch_path not in ctp_path_list):
            ctp_path_list.append(target_fetch_path)
        
        # construct CM21 commands
        print('set default ' + target_fetch_path, file = file_out)
        if (0 == tdf_gen):
            print('fetch ' + tdf_name, file = file_out)
        else:
            print('fetch {tdf_name}/gen={tdf_gen}'.format(tdf_name = tdf_name, tdf_gen = tdf_gen), file = file_out)        
        print('fetch ' + zip_name, file = file_out, end = '\n\n')
                            
    file_in.close()
    file_out.close()
    return ctp_path_list


def gen_exe_script(ctp_path_list):
    if (None == ctp_path_list):
        return
        
    try:
        file_out = open("run.bat", mode = 'a')
    except OSError as e:
        print('Failed to open file run.bat for writting:' + e.strerror, file = sys.stderr)
        
    # for (ctp_path in ctp_path_list):
    ctp_path = ctp_path_list
    print('cd /d ' + ctp_path, file = file_out)
    print('call {0}.bat'.format(ctp_path.basename()), file = file_out)

    
if ("__main__" == __name__):
    if (len(sys.argv) > 2):
        ctp_path_list = parse_input_file(sys.argv[1], sys.argv[2])
        gen_exe_script(*ctp_path_list)