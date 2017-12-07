#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.


import re
import dbm_field
import dbm_entity
import dbm_config

G_sqlQuote = '`'
G_namespace_PREFIX = dbm_config.G_namespace_PREFIX;
G_namespace_prefix = dbm_config.G_namespace_prefix;


def gen_mysql_construct(entity, file_out):
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    count = len(entity.fields);
    pValue = 'pValue';
    
    print('static int {prefix}_entityConstruct{entity_name}(MYSQL_ROW *pRow, {entity_type} *p{entity_name})'
        .format(prefix = G_namespace_PREFIX, entity_name = entity.singular_name, entity_type = entity_type), file = file_out, end = '\n');
    print('{', file = file_out, end = '\n');
    print("".ljust(4) + 'const Char *{pValue} = NULL;'.format(pValue = pValue), file = file_out, end = '\n');
    
    for i in range(0, count):
        field = entity.fields[i];
        dest = "p{entity_name}->{field_name}".format(entity_name = entity.singular_name, field_name = field.name);
        src = "(const Char *) (*pRow)[{counter}]".format(counter = i)        
        print("".ljust(4) + '{pValue} = {src};'.format(pValue = pValue, src = src).ljust(36), file = file_out, end = '');
        print('if (NULL == {src}) {src} = ""; '.format(src = pValue).ljust(28), file = file_out, end = '');
        if ("CHAR" in field.c_type.upper()):
            print("OSA_strncpy({dest}".format(dest = dest).ljust(40), file = file_out, end = '');
            print(", {src})".format(src = pValue).ljust(34), file = file_out, end = '');
        elif ("INT" in field.c_type.upper()):
            print('{dest}'.format(dest = dest).ljust(40)
                  + '= ({field_c_type})strtol({src}, NULL, 0)'.format(field_c_type = field.c_type, src = pValue).ljust(34), 
                 file = file_out, end = '');
        elif ("FLOAT" in field.c_type.upper()):
            print('{dest}'.format(dest = dest).ljust(40)
                  + '= ({field_c_type})strtof({src}, NULL)'.format(field_c_type = field.c_type, src = pValue).ljust(34), 
                 file = file_out, end = '');
        else: 
            print("Cannot determine how to retrieve data fro C data type " + field_c_type)
        print(";".ljust(4) + "/* [{counter:02}] */".format(counter = i), file = file_out, end = '\n')
        
        # convert date time format
        if ('DATE' == field.db_type.upper()):
            print("".ljust(4) + "OSA_datetimeConvert({dest}, sizeof({dest}), OSA_DATE_FORMAT_ISO8601, OSA_DATE_FORMAT_COMPACT);"
                .format(dest = dest), file = file_out, end = '\n');
        elif ('DATETIME' == field.db_type.upper()):
            print("".ljust(4) + "OSA_datetimeConvert({dest}, sizeof({dest}), OSA_DATETIME_FORMAT_ISO8601, OSA_DATETIME_FORMAT_COMPACT);"
                .format(dest = dest), file = file_out, end = '\n');

    print("".ljust(4) + 'return OSA_STATUS_OK;', file = file_out, end = '\n')    
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n' * 2)
    


def gen(entities, path):
    try:        
        file_out = open(path, mode = "w+", encoding = "utf8")
    except OSError as e:
        print("Failed to open file for writing: " + str(e.errno) + e.strerror) 

    print('#pragma region Contruct Entities', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_mysql_construct(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n');

    file_out.close();


def main(entities, path):
    gen(entities, path);