#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import getpass
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# get SVN revision
get_svn_no = """svn info | sed -n '/.*-*:*:*+./{g;1!p;};h' | grep -oP "\d+" """
svn_no = os.popen(get_svn_no).read().strip()

# configure output dir
dest_dir = os.getcwd() + "/code.review/"
dest_svn_dir = dest_dir + "/OLD.SVN%s/" % svn_no
dest_v1_dir = dest_dir + "/NEW." + time.strftime("%Y%m%d%H%M") + "/"
back_path_dir = os.getcwd() + "/back.patch/"
patch_name = back_path_dir + time.strftime("%Y%m%d%H%M%S.patch")
month = string.atoi(time.strftime("%m"), 10)

commit_path = './'

local_encoding = ''
output_encoding = 'utf-8'
current_file_encoding = 'gb2312'  # make an assumption

added_file_list = []
deleted_file_list = []
modified_file_list = []

total_changed_file = 0
current_changed_file = 0

readme_file = dest_v1_dir + '/readme.txt'
temp_file = '.53238313156310'

svn_opt = " "


def get_local_encoding():
    return sys.getfilesystemencoding()
    
def xy_print(str):
    print str.decode(current_file_encoding).encode(local_encoding)
    
def check_vim_setting():
    user = getpass.getuser()
    if os.path.exists('/home/' + user + '/.vimrc') is False:
        cmd = r'find /usr/share/vim/ -name "vimrc_example.vim"'
        tmp = os.popen(cmd).read()
        for i in tmp.split('\n'):
            if len(i) > 0:
                vimrc_example = i
        cmd = 'sed "s/set mouse/\\\"set mouse/" ' + vimrc_example + " > ~/.vimrc"
        os.system(cmd)
        cmd = 'echo "set fileencodings=cp936,utf-8" >> ~/.vimrc'
        os.system(cmd)
        
def create_dir():
    xy_print('Creating destination dir...')
    os.system('rm -rf ' + dest_dir)
    os.mkdir(dest_dir)
    os.mkdir(dest_svn_dir)
    os.mkdir(dest_v1_dir)
    os.system('mkdir -p ' + back_path_dir)
    
def get_repo_status():
    xy_print("Determining revision status...")
    cmd = 'svn status ' + commit_path + svn_opt
    temp = os.popen(cmd).read()
    for i in temp.split('\n'):
        if len(i) == 0:
            continue
        file = i[1:].strip()
        if i[0] is 'D' and i[1] is ' ': deleted_file_list.append(file);
        if i[0] is 'A' and i[1] is ' ': added_file_list.append(file);
        if i[0] is 'M' and i[1] is ' ': modified_file_list.append(file);
    if deleted_file_list or modified_file_list or added_file_list:
        return 0
    else:
        xy_print('No SVN modifications under current dir.')
        return -1
        
def get_user_decision():
    xy_print("Generating files...")
    global total_changed_file
    added_file_list[:] = []
    deleted_file_list[:] = []
    modified_file_list[:] = []
    
    for line in open(readme_file):
        if not ':' in line:
            continue
        file = line.split(':')[1].strip()
        if line.startswith('Deleted'):
            deleted_file_list.append(file)
            total_changed_file += 1
        if line.startswith('Added'):
            added_file_list.append(file)
            total_changed_file += 1
        if line.startswith('Modified'):
            modified_file_list.append(file)
            total_changed_file += 1
    if deleted_file_list or modified_file_list or added_file_list:
        return 0
    else:
        xy_print('No SVN modifications under current dir.')
        return -1
        
'''
    SVN 的理念使得 checkout 出的至少是一个目录，故需要一个临时文件
    把版本库的文件复制到 dest,
    若 operation 是 delete, 则复制文件到 SVN 目录；
    若 operation 是 modify, 则复制原文件到 SVN 目录，修改后的文件到 dest;
    若 operation 是 new, 则复制新文件到 v1 目录。
'''


'''
    若 operation 是 new, 则复制新文件到 v1 目录。    
'''
def action(infile, op):
    global current_changed_file
    str1 = infile.replace('(', '\(')
    str2 = str1.replace(')', '\)')
    file = str2.replace(' ', '\ ')
    os.system('mkdir -p ' + dest_svn_dir + os.path.dirname(file))
    os.system('mkdir -p ' + dest_v1_dir + os.path.dirname(file))
    current_changed_file += 1
    cmd = "echo -e -n \r  " + str(current_changed_file) + ' / ' + str(total_changed_file)
    os.system(cmd)
    if op is 'delete':
        get_svn_url = """svn info %s | grep ^URL | cut -d " " "-f2" """
        svn_url = os.popen(get_svn_url % file).read().strip()
        os.system("svn export %s %s" % (svn_url, dest_svn_dir + file))
    if op is "new":
        os.system("cp %s %s" % (file, dest_v1_dir + os.path.dirname(file)))
    if op is "modify":
        get_svn_url = """svn info %s | grep ^URL | cut -d " " "-f2" """
        svn_url = os.popen(get_svn_url % file).read().strip()
        cmd = "svn export %s %s" % (svn_url, dest_svn_dir + file)
        # print 'SVN ' + svn_url + ' --> ' + dest_svn_dir + file
        # print 'SVN command: ' + cmd
        os.system(cmd)
        cmd = "cp %s %s" % (file, dest_v1_dir + os.path.dirname(file))
        # print 'Local file command: ' + cmd
        os.system(cmd)
        
def deal_backup_files():
    xy_print("Patching changed files...")
    cmd = "svn diff " + commit_path + " >> " + patch_name
    os.system(cmd)
    
def deal_delete_files():
    for file in deleted_file_list:
        action(file, "delete")
        
def deal_modify_files():
    for file in modified_file_list:
        action(file, "modify")
        
def deal_new_files():
    for file in added_file_list:
        action(file, "new")
        
def deal_lint():
    lint_dir = './lint'
    lint_new_dir = dest_v1_dir + lint_dir
    # copy currrent lint dir to new dir
    os.system("svn export --force %s %s" % (commit_path + lint_dir, lint_new_dir))
    # change time to lint dir
    os.system('stat %s | sed -n \"5p\" > %s' % (commit_path + lint_dir, lint_new_dir + 'date.txt'))
    # export lint dir on SVN to old dir    
    get_svn_url = """svn info %s | grep ^URL | cut -d " " "-f2" """
    svn_url = os.popen(get_svn_url % lint_dir).read().strip()
    os.system("svn export --force %s %s" % (svn_url, dest_svn_dir + "lint"))
    
def init_readme():
    readme = open(readme_file, "w")
    cmd = "svn info " + commit_path + "| grep ^URL | cut -d \" \" -f 2 "
    temp = os.popen(cmd).read()
    readme.write('---- The following file(s) will be generated for code reviewing. You may remove unwanted files. ----\n')
    for filename in added_file_list:
        newline = "Added: " + filename.decode(local_encoding).encode(output_encoding)
        readme.write(newline)
        readme.write('\n')
    for filename in deleted_file_list:
        newline = "Deleted: " + filename.decode(local_encoding).encode(output_encoding)
        readme.write(newline)
        readme.write('\n')
    for filename in modified_file_list:
        newline = "Modified: " + filename.decode(local_encoding).encode(output_encoding)
        readme.write(newline)
        readme.write('\n')
    readme.write('\n' * 2)
    readme.write('---- Do NOT modify the follwing ----')
    readme.write('\n' * 2)
    readme.write('---- SVN URL %s ----' % temp.strip())
    # readme.write(temp)
    newline = '''
---- Tips ----
---- Lines starts with "Added", "Deleted", or "Modified", the corresponding file will be generated for review.
---- If you do not want to include that/those file(s), please remove the line.
    '''
    readme.write(newline)
    
    
print 'svn review tool'
local_encoding = get_local_encoding()
check_vim_setting()
if len(sys.argv) > 1:
    j = 1;
    while j < len(sys.argv):
        if sys.argv[j][0] is '-' and sys.argv[j][1] is 'i': svn_opt = ' --ignore-externals'
        else: commit_path = commit_path + sys.argv[j]
        j += 1
if get_repo_status() == -1:
    sys.exit(-1)
create_dir()
xy_print('Creating "readme.txt"...')
init_readme()
os.system('vi ' + readme_file)
xy_print('Finished creating "readme.txt" file.')
get_user_decision()
if total_changed_file == 0:
    sys.exit(0)
xy_print('Working... Please do not interrupt...')
xy_print('Patch file is ' + patch_name)
deal_backup_files()
deal_delete_files()
deal_new_files()
deal_modify_files()
# deal_lint()
# os.system('cp /home/pub/docs/*.xlsx ' + dest_v1_dir)
xy_print('\nPlease modify ' + dest_dir + ', and copy to code review dir')
