# /usr/bin/env python3
# checks if the .RPT/.RST files are consistent

import sys
import subprocess

def func(old_path, new_path):
    if (None == old_path or None == new_path):
        return -1
    
    try:
        old_file = open(old_path)
        new_file = open(new_path)
    except OSError as e:
        print("Failed to file for comparing".format(src_path, e.strerror), file = sys.stderr)
        return -1
    
    consistent = True
    old_file_line = old_file.readline()
    new_file_line = new_file.readline()
    while ('' != old_file_line and '' != new_file_line):
        # get the first 3 lines
        for i in range(0, 2):
            old_file_line += old_file.readline()
            new_file_line += new_file.readline()
            
        if ('RESULTS FILE' in old_file_line.upper()):        
            # .RST files
            # allowed differences
            if ('TEST START TIME' in old_file_line.upper()):
                continue
            if ('TEST END TIME' in old_file_line.upper()):
                continue
            if ('USERID:' in old_file_line.upper()):
                continue
            # reached the end
            if ('CURRENT PROGRAM LIBRARY' in old_file_line.upper() or 'CURRENT BUILD' in old_file_line.upper()):
                break
            
        else:
            # .RPT files
            # skip the first 9 lines
            for i in range(0, 6):
                old_file_line = old_file.readline()
                new_file_line = new_file.readline()
            if ('Win32 Host:' in old_file_line):
                continue
            if ('Current Dir:' in old_file_line):
                continue
            if ('.PTH' in old_file_line.upper()):
                continue
            if ('.CUL' in old_file_line.upper()):
                continue
            if ('.XIN' in old_file_line.upper()):
                continue
            if ('Date of report' in old_file_line.upper()):
                for i in range(0, 3):
                    old_file_line = old_file.readline()
                    new_file_line = new_file.readline()
            if ('Current Directory:' in old_file_line.upper()):
                for i in range(0, 3):
                    old_file_line = old_file.readline()
                    new_file_line = new_file.readline()
            # how about src code path?
        
        # other differences are not allowed
        if (old_file_line.upper() != new_file_line.upper()):
            consistent = False
            break
        old_file_line = old_file.readline()
        new_file_line = new_file.readline()
                        
    old_file.close()
    new_file.close()
    if (consistent):
        return 0
    else:
        return 1

        
def call_diff(old_file, new_file):
    if (None == old_file or None == new_file):
        print('Bad parameter.', file = sys.stderr)
        return None
    
    # command = ['D:/Program Files/Git/bin/diff.exe', " --unchanged-line-format=''" + " --old-line-format=''" + \
    #           " --new-line-format='(%dn) %L'", old_file, new_file]
    command = ['diff.exe', old_file, new_file]
    result = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)    
    differences = []
    for line in result.stdout:
        LINE = str(line).upper()
        if (('TEST START TIME' in LINE) or               \
            ('TEST END TIME' in LINE) or                 \
            ('USERID:' in LINE) or                       \
            ('CURRENT PROGRAM LIBRARY' in LINE) or       \
            ('CURRENT BUILD' in LINE) or                 \
            ('WIN32 HOST:' in LINE) or                   \
            ('CURRENT DIR' in LINE) or                   \
            ('DATE OF REPORT' in LINE) or                \
            ('.PTH' in LINE) or                          \
            ('.CUL' in LINE) or                          \
            ('.XIN' in LINE)):        
            continue
        else:
            differences.append(line)
            
    return differences

if ("__main__" == __name__):
    if (len(sys.argv) > 2):
        # func(sys.argv[1])        
        retval = call_diff(sys.argv[1], sys.argv[2])
        if (None == retval):        
            print('Missing comparison operand.')
        else:
            for line in retval:
                print(line, file = sys.stdout)