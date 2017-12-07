#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# "C:\Program Files\Python36\python.exe" D:\Code\smartaccesscontrol_svn\dbmanager\tools\code_generator\dbm_main.py D:\Code\smartaccesscontrol_svn\dbmanager\doc\database_tables.sql D:\Code\smartaccesscontrol_svn\dbmanager\

# Created by Papillon. Oct 31, 2017.

import sys
import os
import dbm_field
import dbm_entity
import dbm_gen_entities_python
import dbm_gen_entities_h
import dbm_gen_entities_c
import dbm_sql
import dbm_mysql
import dbm_sqlite3
import dbm_config


G_namespace_PREFIX = dbm_config.G_namespace_PREFIX;
G_namespace_prefix = dbm_config.G_namespace_prefix;


def main(sql_path, out_dir):    
    if (not os.path.exists(out_dir)):
        print(out_dir + " does not exist");
        return -1;
    
    if (os.path.isdir(out_dir)):
        _out_dir = out_dir
    else:
        _out_dir = os.path.dirname(out_dir) 

    path_entities_py  = os.path.join(_out_dir, G_namespace_prefix + "_entities.py")
    path_entities_h   = os.path.join(_out_dir, G_namespace_prefix + "_entities.h")    
    path_entities_c   = os.path.join(_out_dir, G_namespace_prefix + "_entities.c")
    path_sql_c        = os.path.join(_out_dir, G_namespace_prefix + "_sql.c")
    path_sqlite3_c    = os.path.join(_out_dir, G_namespace_prefix + "_sqlite3.c")        
    path_mysql_c      = os.path.join(_out_dir, G_namespace_prefix + "_mysql.c")
      
    entities = dbm_sql.parse_sql_file(sql_path);

    # generate kinds of files
    dbm_gen_entities_python.main(entities, path_entities_py);
    dbm_gen_entities_h.main(entities, path_entities_h);
    dbm_gen_entities_c.main(entities, path_entities_c);
    dbm_sql.main(entities, path_sql_c);
    dbm_mysql.main(entities, path_mysql_c);
    dbm_sqlite3.main(entities, path_sqlite3_c);
    return 0;
    

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print("usage: {0} sql_path output_dir".format(sys.argv[0]));
        sys.exit(-1);
    else:
        main(sys.argv[1], sys.argv[2])
        