import sys
import os
import shutil

def separate_to_dir(dir_path):
    count = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            base, ext = os.path.splitext(file)
            if (".DOCX" == ext.upper()):
                sub_dir_path = os.path.join(dir_path, base)
                if (not os.path.exists(sub_dir_path)):
                    os.makedirs(sub_dir_path)
                shutil.move(os.path.join(dir_path, file), os.path.join(sub_dir_path, "new.docx"))
                count += 1
                
    return count
                
                
                
if "__main__" == __name__:
    if (len(sys.argv) > 1):
        count = separate_to_dir(sys.argv[1])
        print("Processed {count} file(s).".format(count = count))
    else:
        print("Usage: {me} dir_path".format(me = sys.argv[1]), file = sys.stderr)