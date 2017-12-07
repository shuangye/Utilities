#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.

import sys
import os
import codecs
import string
import re
import dbm_field
import dbm_entity
import dbm_config

G_sqlQuote = '`'
G_namespace_PREFIX = dbm_config.G_namespace_PREFIX;
G_namespace_prefix = dbm_config.G_namespace_prefix;



# supid plurality to singular converter, not reliable
def plurality_to_singular(thestring):    
    # if thestring.endswith('es'):
    #     return thestring[:-len('es')]    
    if thestring.endswith('s'):
        return thestring[:-len('s')]
    else:
        return thestring


######################################## parse SQL ############################################

G_sql_types = { 
#   SQLite data type  : [C data type,     C format specifier, SQLite3 bind          , Python.ctypes]
    "TEXT"            : ["Char",          "%s",               "sqlite3_bind_text"   , "ctypes.c_char" ], 
    "CHAR"            : ["Char",          "%s",               "sqlite3_bind_text"   , "ctypes.c_char" ], 
    "VARCHAR"         : ["Char",          "%s",               "sqlite3_bind_text"   , "ctypes.c_char" ], 
    "DATE"            : ["Char",          "%s",               "sqlite3_bind_text"   , "ctypes.c_char" ], 
    "DATETIME"        : ["Char",          "%s",               "sqlite3_bind_text"   , "ctypes.c_char" ], 
    "TINYINT"         : ["Int8",          "%d",               "sqlite3_bind_int"    , "ctypes.c_char" ], 
    "SMALLINT"        : ["Int16",         "%d",               "sqlite3_bind_int"    , "ctypes.c_short"], 
    "INT"             : ["Int32",         "%d",               "sqlite3_bind_int"    , "ctypes.c_int"  ], 
    "FLOAT"           : ["Float32",       "%f",               "sqlite3_bind_double" , "ctypes.c_float"], 
}


def detect_field_attributes(field):
    def detect_value_type(str_value_type):
        result = (dbm_field.ValueType.Nothing, '');
        if   ("DATE"        == str_value_type.upper()):    
            result = (dbm_field.ValueType.Date    , "Char val_of_{field_name}[DBM_MAX_DATE_STR_LEN];  OSA_datetimeGetCurrent(OSA_DATE_FORMAT_ISO8601, val_of_{field_name}, sizeof(val_of_{field_name}));");
        elif ("DATETIME"    == str_value_type.upper()):   
           result = (dbm_field.ValueType.Datetime, "Char val_of_{field_name}[DBM_MAX_DATETIME_STR_LEN];  OSA_datetimeGetCurrent(OSA_DATETIME_FORMAT_ISO8601, val_of_{field_name}, sizeof(val_of_{field_name}));");
        elif ("UUID"        == str_value_type.upper()):   
           result = (dbm_field.ValueType.UUID    , "Char val_of_{field_name}[64];                        DBM_utlGenUuid(val_of_{field_name}, sizeof(val_of_{field_name}));");
        elif ("FLAG"        == str_value_type.upper()):    
            result = (dbm_field.ValueType.Flag    , "Int32 val_of_{field_name} = DBM_DATA_OPERATION_C;");
        elif ("SYNC"        == str_value_type.upper()):    
            result = (dbm_field.ValueType.Sync    , "Int32 val_of_{field_name} = DBM_DATA_SYNC_UNSYNCED;");
        else:
           print('Unrecognized value type ' + str_value_type);
        return result;

    attr_pattern   = r'ATTR\s*:\s*(.+)\s*;'                   # e.g., ATTR:AUTO_ON_C(DATETIME), NO_U();
    auto_c_pattern = r'AUTO_ON_C\s*\(\s*([A-Z]+)\s*\)'        # e.g., AUTO_ON_C(DATETIME)
    auto_u_pattern = r'AUTO_ON_U\s*\(\s*([A-Z]+)\s*\)'        # e.g., AUTO_ON_U(DATETIME)
    no_u_pattern   = r'NO_U\s*\(\s*([A-Z]+)\s*\)'             # e.g., NO_U(DATE)
    attributes     = []

    # determine if the comment contains attributes
    match = re.search(attr_pattern, field.comment, re.IGNORECASE)
    if (None == match):
        return attributes;

    attributes_str = match.group(1)
    
    # AUTO_ON_C(DATETIME)
    match = re.search(auto_c_pattern, attributes_str, re.IGNORECASE)
    if (None != match):
        str_value_type                    = match.group(1);
        (value_type, filing_expression)   = detect_value_type(str_value_type);
        attribute                         = dbm_field.FieldAttribute();
        attribute.value_provider          = dbm_field.ValueProvider.Auto_On_Creation;
        attribute.value_type              = value_type;
        attribute.filling_expression      = filing_expression.format(field_name = field.name);
        attributes.append(attribute);
            
    # NO_U()
    match = re.search(no_u_pattern, attributes_str, re.IGNORECASE)
    if (None != match):
        str_value_type                    = match.group(1);
        (value_type, filing_expression)   = detect_value_type(str_value_type);
        attribute                         = dbm_field.FieldAttribute();
        attribute.value_provider          = dbm_field.ValueProvider.No_Update;
        attribute.value_type              = value_type;
        attribute.filling_expression      = filing_expression.format(field_name = field.name);
        attributes.append(attribute);
    
    # AUTO_ON_U(DATETIME)
    match = re.search(auto_u_pattern, attributes_str, re.IGNORECASE)
    if (None != match):
        str_value_type                    = match.group(1);
        (value_type, filing_expression)   = detect_value_type(str_value_type);
        attribute                         = dbm_field.FieldAttribute();
        attribute.value_provider          = dbm_field.ValueProvider.Auto_On_Update;
        attribute.value_type              = value_type;
        attribute.filling_expression      = filing_expression.format(field_name = field.name);
        attributes.append(attribute);
            
    return attributes;



def parse_sql_file(ddl_path):
    field = None;
    entity = None;
    entities = [];

    try:
        file_in = open(ddl_path, mode = "r", encoding="utf8")
    except OSError as e:
        print("Failed to open file " + ddl_path + "for parsing: " + str(e.errno) + e.strerror)    
        return entities;
    
    is_within_fields = False
    table_begin_pattern = r'\s*CREATE\s+TABLE\s+(\w+)\s*'                             # matches 'CREATE TABLE G_entity_name'
    table_end_pattern = r'\s*\)\s*;'                                                  # matches ');'
    field_pattern = r'([a-zA-Z_]+\w*)\s+([a-zA-Z]+)\s*\(?(\d*)\)?([^-]*)([-]{2,})?\s*(.*)?$'  # matches sth. like 'reluuid CHAR(32) NOT NULL -- comments' or 'sync TINYINT -- comments'
    # field_pattern = re.compile(field_pattern, re.IGNORECASE)
    # match = re.search(field_pattern, line, flags = re.IGNORECASE)

    for line in file_in:
        line = line.strip()
        if (len(line) == 0):
            continue
        if (line.startswith("--")):  # skip comments
            continue
        
        # determine if table definition ends
        match = re.match(table_end_pattern, line, re.IGNORECASE)
        if (None != match):
            is_within_fields = False;
            entities.append(entity);
            continue;
        
        # determine if table definition starts
        match = re.match(table_begin_pattern, line, re.IGNORECASE)
        if (None != match):
            is_within_fields = True            
            entity                    = dbm_entity.Entity();
            entity.plural_name        = match.group(1);
            entity.singular_name      = plurality_to_singular(entity.plural_name)
            continue
        
        # determine if within table definition
        if (is_within_fields):
            match = re.match(field_pattern, line, re.IGNORECASE)
            if (None == match):
                continue
            field = dbm_field.Field();
            field.name             = match.group(1);
            field.db_type          = match.group(2);
            if (len(match.group(3)) > 0): field.length = int(match.group(3));
            else: field.length = 0;
            G_mModifier            = match.group(4);
            # match.group(5) is the `--` prefix of comment
            field.comment          = match.group(6);            
            field.attributes       = detect_field_attributes(field);

            if (field.db_type in G_sql_types.keys()):
                field.c_type             = G_sql_types[field.db_type][0];
                field.c_format_spec      = G_sql_types[field.db_type][1];
                field.db_set_func        = G_sql_types[field.db_type][2]
                field.python_type        = G_sql_types[field.db_type][3];
                if   ("DATE"     == field.db_type.upper()): field.length = 16     # format 20171020
                elif ("DATETIME" == field.db_type.upper()): field.length = 32     # format 20171020080930                
                        
            # foreign_pattern = r'FOREIGN\s+KEY\s+\((\w+)\)\s+REFERENCES\s+(\w+)\((\w+)\)'
            # match = re.search(foreign_pattern, line, re.IGNORECASE)                           
                  
            # print("Unrecognized SQL data type " + G_mTypeSql)
            entity.fields.append(field);
            continue            

    file_in.close();
    return entities;


######################################## generate code ############################################


def gen_sql_INSERT_statement(entity, file_out):
    global G_sqlQuote
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_name;
    count = len(entity.fields);    

    print("static int {PREFIX}_sqlGenInsertStatementFor{entity_name}({entity_type} *p{entity_name}, const Char *pTableName, Char *pSqlStatement, const size_t length)"
          .format(PREFIX = G_namespace_PREFIX, entity_name = entity_name, entity_type = entity_type), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')    
    
    # construct the C format string
    print("".ljust(4) + r'const Char *pFormat = "INSERT INTO {G_sqlQuote}%s{G_sqlQuote} ('.format(G_sqlQuote = G_sqlQuote), file = file_out, end = '')
    for i in range(0, count):
        field = entity.fields[i];
        separator = ", ";
        if (i == count - 1): separator = "";    # the last field has no `,` separator        
        print("{G_sqlQuote}{field_name}{G_sqlQuote}{separator}".format(G_sqlQuote = G_sqlQuote, field_name = field.name, separator = separator), file = file_out, end = '');
    print(r') "', file = file_out, end = '\n');

    print("".ljust(8) + r'"VALUES(', file = file_out, end = '');
    for i in range(0, count):
        field = entity.fields[i];
        escape = "";
        separator = ", ";
        if (i == count - 1): separator = "";    # the last field has no `,` separator
        if ("%s" == field.c_format_spec): escape = r"\"";
        print("{escape}{c_format_spec}{escape}{separator}".format(escape = escape, c_format_spec = field.c_format_spec, separator = separator), file = file_out, end = '');
    print(r')";', file = file_out, end = '\n');
    
    # check field attributes
    for i in range(0, count):
        field = entity.fields[i];
        field_value = r'{instance}->{field_name}'.format(instance = instance, field_name = field.name);
        for attr in field.attributes:
            if (dbm_field.ValueProvider.Auto_On_Creation == attr.value_provider):            
                if (dbm_field.ValueType.Flag == attr.value_type):
                    print(''.ljust(4) + '{field_value} = DBM_DATA_OPERATION_C;'.format(field_value = field_value), file = file_out, end = '\n');
                elif (dbm_field.ValueType.Sync == attr.value_type):                
                    print(''.ljust(4) + '{field_value} = DBM_DATA_SYNC_UNSYNCED;'.format(field_value = field_value), file = file_out, end = '\n');
                else:  # for date, time, datetime, UUID
                    print(''.ljust(4) + attr.filling_expression, file = file_out, end = '\n');
                    print(''.ljust(4) + 'OSA_strncpy({instance}->{field_name}, val_of_{field_name});'.format(instance = instance, field_name = field.name), file = file_out, end = '\n');
    
    # print to the string buffer
    print("".ljust(4) + r'snprintf(pSqlStatement, length, pFormat, pTableName,', file = file_out, end = '\n');
    for i in range(0, count):
        field = entity.fields[i];
        field_value = r'{instance}->{field_name}'.format(instance = instance, field_name = field.name);
        separator = ",";
        if (i == count - 1): separator = "";    # the last field has no `,` separator 
        # some DBMS do not allow empty string for datetime (please define `DBM_INVALID_DATETIME` in your code)
        if ('DATE' == field.db_type.upper() or 'DATETIME' == field.db_type.upper()):  
            print("".ljust(8) + r'OSA_strIsEmpty({field_value}) ? DBM_INVALID_DATETIME : {field_value}'.format(field_value = field_value), file = file_out, end = '');
        else:
            print("".ljust(8) + field_value, file = file_out, end = '');
        print(separator, file = file_out, end = '\n');
    print("".ljust(4) + ');', file = file_out, end = '\n');
    print("".ljust(4) + 'return OSA_STATUS_OK;', file = file_out, end = '\n');
    
    print('}', file = file_out, end = '\n');
    print('', file = file_out, end = '\n' * 2)
    
    
    
def gen_sql_UPDATE_statement(entity, file_out):
    global G_sqlQuote
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_name;
    count = len(entity.fields);    

    print("static int {PREFIX}_sqlGenUpdateStatementFor{entity_name}({entity_type} *p{entity_name}, const Char *pTableName, Char *pSqlStatement, const size_t length)"
          .format(PREFIX = G_namespace_PREFIX, entity_name = entity_name, entity_type = entity_type), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')    
    
    # construct the C format string
    print("".ljust(4) + r'const Char *pFormat = "UPDATE {G_sqlQuote}%s{G_sqlQuote} SET "'.format(G_sqlQuote = G_sqlQuote), file = file_out, end = '\n')
    for i in range(0, count):
        field = entity.fields[i];
        separator = ", ";
        escape = "";
        if (i == count - 1): separator = "";    # the last field has no `,` separator
        if ("%s" == field.c_format_spec): escape = r"\"";
        print(''.ljust(26) + r'"{G_sqlQuote}{field_name}{G_sqlQuote} = {escape}{c_format_spec}{escape}{separator}"'
              .format(G_sqlQuote = G_sqlQuote, field_name = field.name, escape = escape, c_format_spec = field.c_format_spec, separator = separator), 
            file = file_out, end = '\n');
    print(''.ljust(26) + r';', file = file_out, end = '\n');
    
    # print to the string buffer
    print("".ljust(4) + r'snprintf(pSqlStatement, length, pFormat, pTableName,', file = file_out, end = '\n');
    for i in range(0, count):
        field = entity.fields[i];
        field_value = r'{instance}->{field_name}'.format(instance = instance, field_name = field.name);
        separator = ",";
        if (i == count - 1): separator = "";    # the last field has no `,` separator
        print("".ljust(8) + field_value, file = file_out, end = '');
        print(separator, file = file_out, end = '\n');
    print("".ljust(4) + ');', file = file_out, end = '\n');
    print("".ljust(4) + 'return OSA_STATUS_OK;', file = file_out, end = '\n');
    
    print('}', file = file_out, end = '\n');
    print('', file = file_out, end = '\n' * 2)
    

    
def gen_sql(entities, path):
    try:        
        file_out = open(path, mode = "w+", encoding = "utf8")
    except OSError as e:
        print("Failed to open file for writing: " + str(e.errno) + e.strerror) 

    print('#pragma region SQL INSERT statements', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_sql_INSERT_statement(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n' * 3);
        
    print('#pragma region SQL UPDATE statements', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_sql_UPDATE_statement(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n' * 3);

    file_out.close();


def main(entities, path):
    gen_sql(entities, path);