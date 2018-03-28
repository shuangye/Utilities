#!/usr/bin/env python3
#coding=utf-8

"""
Created by Liu Papillon on Jan 8, 2018.
This tool is used to generate code review for git.
"""

"""
Before using the tool, please:
1. Configure your git user name and email:
    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com
    
2. Make sure Gitlab is configured with SSH protocol support, and setup an SSH key pair:
    1. run `ssh-keygen -t rsa` to generate an SSH key pair.
    2. copy the private key to ~/.ssh/ directory.
    3. import the public key to GitLab: User Profile - SSH Keys.
    
3. Make sure your can pull/push with remote git repository via the SSH protocol without a password.

4. Before running `git commit`, your can run this tool within your git working tree to generate code review. 
   The files are put in a directory named code_review_<your_git_name>
"""

import os
import sys
import time
import shutil
import getpass
from enum import IntEnum


G_comment_prefix = '#'
G_repo_fetch_url = '';
G_relative_path_in_repo = '';
G_code_review_dir = 'code_review';
G_old_files_dir = '';
G_new_files_dir = '';
G_editor = 'vim';
G_log_path = 'README.txt';
G_review_record_template = '/home/workspace/review_record.xlsx'


################# types #################

"""About enum in Python http://www.chriskrycho.com/2015/ctypes-structures-and-dll-exports.html"""
class CtypesEnum(IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)

class GitFileStatus(CtypesEnum):
    NONE                      = 0
    ADDED                     = 1
    MODIFIED                  = 2
    DELETED                   = 3
    RENAMED                   = 4
    UNTRACKED                 = 5
    

class GitFile:
    def __init__(self):
        self.relative_path             = '';
        self.status                    = GitFileStatus.NONE;


################# methods #################
        
def check_env():
    ret = shutil.which('git');
    if 0 == len(ret):
        print('git command line is not found.');
        return False;
        
    ret = os.popen('git rev-parse --is-inside-work-tree').read().strip();
    if 'true' != ret: 
        print('Current directory \'{0}\' is not a git working directory.'.format(os.getcwd()));
        return False;
    
    ret = shutil.which(G_editor);
    if 0 == len(ret):
        print('Editor {0} is not found.'.format(G_editor));
        return False;
        
    return True;
   
    
def setup():
    def get_repo_fetch_url():
        repo_fetch_url = None;
        ret = os.popen('git remote -v').read();
        for line in ret.splitlines():
            if 'fetch' in line:
                repo_fetch_url = line.split()[1].rstrip('.git');
                break;
        # print('repo fetch URL = ' + repo_fetch_url);
        return repo_fetch_url;    
    
    def get_relative_path_in_repo():
        return os.popen('git rev-parse --show-prefix').read().strip();

    global G_code_review_dir, G_repo_fetch_url, G_relative_path_in_repo;
    global G_old_files_dir, G_new_files_dir;
    
    user_name = os.popen('git config user.name').read().strip();
    if 0 == len(user_name):
        print("[WARNING] git user name is not configured.");
        user_name = getpass.getuser().strip();
        
    G_repo_fetch_url = get_repo_fetch_url();
    G_relative_path_in_repo = get_relative_path_in_repo();
        
    G_code_review_dir = '{0}_{1}'.format(G_code_review_dir, user_name);
    if os.path.exists(G_code_review_dir):
        shutil.rmtree(G_code_review_dir);    # old contents should be deleted
    os.mkdir(G_code_review_dir);
    
    G_old_files_dir = os.path.join(G_code_review_dir, 'old');
    G_new_files_dir = os.path.join(G_code_review_dir, 'new_' + time.strftime("%Y%m%d%H"));
    os.mkdir(G_old_files_dir);
    os.mkdir(G_new_files_dir);

    
def write_log_file(content):
    global G_log_path;
    G_log_path = os.path.join(G_code_review_dir, G_log_path);
    try:        
        file_out = open(G_log_path, mode = "w+", encoding = "utf8")
    except OSError as e:
        print("Failed to open file {0} for writing: {1}".format(G_log_path, e.strerror)); 
        return -1;
    
    print('{comment} The following file(s) will be generated for code reviewing. You may remove unwanted files. {comment}'
        .format(comment = G_comment_prefix * 4), file = file_out);
    print(content, file = file_out);
    print('\n' * 2, file = file_out);
    print('{comment} Do NOT modify the follwing {comment}'.format(comment = G_comment_prefix * 4), file = file_out);
    print('{comment} Git URL = {url}'.format(comment = G_comment_prefix * 4, url = G_repo_fetch_url), file = file_out);
    print('{comment} Current working dir in repo = {url}'
        .format(comment = G_comment_prefix * 4, url = os.path.join(G_repo_fetch_url, G_relative_path_in_repo)), file = file_out);
    print(file = file_out);
    print('{comment} N O T E : lines start with \'\?\' means the files are not tracked by git. They will not be exported for code review. {comment}'
        .format(comment = G_comment_prefix * 4), file = file_out);
    print('{comment} If you do not want to include a file, please remove the corresponding line.'
        .format(comment = G_comment_prefix * 4), file = file_out);
    print('\n' * 2, file = file_out);
        
    file_out.close();
    
    
def parse_repo_status(path):
    try:        
        file = open(path, mode = "r", encoding = "utf8")
    except OSError as e:
        print("Failed to open file {0} for reading: {1}".format(path, e.strerror)); 
        return -1;
        
    git_files = [];
    for line in file:
        if len(line.strip()) == 0: continue;
        if line.lstrip().startswith(G_comment_prefix): continue;
        fields = line.split();
        if (len(fields) < 2): continue;
        git_file = GitFile();
        git_file.relative_path = fields[1];
        git_file.status = GitFileStatus.NONE;
        status = fields[0];
        if   'A' in status: git_file.status = GitFileStatus.ADDED;
        elif 'M' in status: git_file.status = GitFileStatus.MODIFIED;
        elif 'D' in status: git_file.status = GitFileStatus.DELETED;
        elif 'R' in status: git_file.status = GitFileStatus.RENAMED;
        elif '?' in status: git_file.status = GitFileStatus.UNTRACKED;
        git_files.append(git_file);
    
    file.close();
    return git_files;

    
"""
@param repo_url should be sth. like http://192.168.10.6/papillon/bsw, or http://192.168.10.6/papillon/bsw.git
@param git_path is the path to a file/dir relatives to the root of a repo.
@param dest_path is the path with deepest level of a dir where to put the fetched file.
"""
def fetch_git_file(repo_url, git_path, dest_path):
    def count_path_depth(path):
        return path.strip('/').count('/');

    # git archive --format=tar --remote=ssh://git@192.168.10.6/papillon/bsw.git HEAD osa/include/osa/ | tar -x --strip=2 -C include/
    repo = repo_url.replace('http://', 'ssh://git@');
    if not repo.endswith('.git'): repo = repo + '.git';
    dest_dir = os.path.dirname(dest_path);
    os.makedirs(dest_dir, exist_ok = True);
    cmd = 'git archive --format=tar --remote={url} HEAD {git_path} | tar -x --strip={depth} -C {dest_dir}'    \
        .format(url = repo, git_path = git_path, depth = count_path_depth(git_path), dest_dir = dest_dir);
    cmd = cmd.replace('\\', '/');    # normalize Windows path separator
    # print('Command = ' + cmd);
    print("Fetching {0}...".format(git_path));
    ret = os.system(cmd);
    if 0 != ret:
        print('Failed to fetch file {0} from remote git repo {1}'.format(git_path, repo_url));
        return -1;
    return 0;
    
    
def copy_file(src_path, dst_path):
    dir = os.path.dirname(dst_path);
    os.makedirs(dir, exist_ok = True);
    shutil.copy(src_path, dir);
    
    
def handle_files(git_files):
    print("Exporting files for review...");

    for git_file in git_files:
        should_handle_old = False;
        should_handle_new = False;
        if git_file.status == GitFileStatus.ADDED:
            # print('File {0} is added.'.format(git_file.relative_path));
            should_handle_new = True;
        elif git_file.status == GitFileStatus.MODIFIED:
            # print('File {0} is modified.'.format(git_file.relative_path));
            should_handle_old = True;
            should_handle_new = True;
        elif git_file.status == GitFileStatus.DELETED:
            # print('File {0} is deleted.'.format(git_file.relative_path));
            should_handle_old = True;
        elif git_file.status == GitFileStatus.RENAMED:
            # print('File {0} is remaned.'.format(git_file.relative_path));
            should_handle_old = True;
            should_handle_new = True;
        elif git_file.status == GitFileStatus.UNTRACKED:
            # print('File {0} is untracked.'.format(git_file.relative_path));
            should_handle_old = False;
            should_handle_new = False;
        if should_handle_old:
            fetch_git_file(G_repo_fetch_url, 
                os.path.join(G_relative_path_in_repo, git_file.relative_path), 
                os.path.join(G_old_files_dir, G_relative_path_in_repo, git_file.relative_path));
        if should_handle_new:
            copy_file(git_file.relative_path, 
                os.path.join(G_new_files_dir, G_relative_path_in_repo, git_file.relative_path));
    return 0;
    
    
def main():
    if not check_env():
        return -1;

    print('Preparing...');
    setup();
    
    print('Checking repository...');
    content = os.popen('git -c core.fileMode=false status -s').read();
    
    write_log_file(content);
    os.system('{editor} {file}'.format(editor = G_editor, file = G_log_path));
    
    git_files = parse_repo_status(G_log_path);
    handle_files(git_files);
    
    shutil.copy(G_review_record_template, G_code_review_dir);
    return 0;

    
if __name__ == '__main__':
    main();
