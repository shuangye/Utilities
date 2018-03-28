#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Dec 7, 2017.


import re
import sys


"""
address           perms offset  dev   inode       pathname
00400000-00452000 r-xp 00000000 08:02 173521      /usr/bin/dbus-daemon
"""
def parse(path):
    try:        
        maps_file = open(path, mode = "r", encoding = "utf8")
    except OSError as e:
        print("Failed to open file for writing: " + str(e.errno) + e.strerror) 

    used_mem = 0;
    pattern = r'^([0-9a-fA-F]+)-([0-9a-fA-F]+)\s+(\S+)\s+([0-9a-fA-F]+)\s+(\d+:\d+)\s+(\d+)\s*(.*)$'
    field_separator = ' ' * 4;
    for line in maps_file:
        match = re.match(pattern, line, re.IGNORECASE);
        if None == match:
            continue;
        addr_begin_hex = match.group(1);
        addr_end_hex   = match.group(2);
        addr_begin     = int(addr_begin_hex, 16);
        addr_end       = int(addr_end_hex, 16);
        perms          = match.group(3);
        offset         = match.group(4);
        dev            = match.group(5);
        inode          = match.group(6);
        pathname       = match.group(7);
        print('{0}'.format(addr_begin_hex).ljust(16), end = '-');
        print('{0}'.format(addr_end_hex).rjust(16), end = field_separator);
        print('{0}'.format(perms).ljust(5), end = field_separator);
        print('{0}'.format(offset).ljust(8), end = field_separator);
        print('{0}'.format(dev).ljust(5), end = field_separator);
        print('{0}'.format(inode).ljust(10), end = field_separator);
        print('{0}'.format(pathname), end = '\n');
        used_mem += addr_end - addr_begin;

    maps_file.close();
    used_mem = used_mem / 1024 / 1024;
    print('\n' * 2 + 'USED MEMORY = {0}MB.'.format(used_mem), end = '\n' * 2);
    
    
if '__main__' == __name__:
    if len(sys.argv) > 1:
        path = sys.argv[1];
        if path.isdigit(): path = '/proc/{0}/maps'.format(path);
        parse(path);
    else:
        print('Usage: {0} path', sys.argv[0]);
