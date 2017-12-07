#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.

import re
import dbm_field
import dbm_entity
import dbm_config

G_namespace_PREFIX = dbm_config.G_namespace_PREFIX;
G_namespace_prefix = dbm_config.G_namespace_prefix;


# INSERT INTO %s ("col1", "col2") VALUES(?, ?, );
def gen_sqlite3_INSERT_statement(entity, file_out):
    global G_namespace_PREFIX, G_namespace_prefix;
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_type;
    count = len(entity.fields);
    
    print("static const Char * {PREFIX}_getSqlStatementOfINSERT{entity_name}(void)"
        .format(PREFIX = G_namespace_PREFIX, entity_name = entity_name), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')
    print("".ljust(4) + "/* fields count = {count} */".format(count = count), file = file_out, end = '\n')
    print("".ljust(4) + "return", file = file_out, end = '\n');
    print("".ljust(4) + "\"INSERT INTO \\\"%s\\\" (", file = file_out, end = '');
        
    # for key, value in G_entity_fields.items():
    for i in range(0, count):     # range[ , )
        field = entity.fields[i];
        separator = ', '
        if (i == count - 1): separator = ''
        print("\\\"{field_name}\\\"{separator}".format(field_name = field.name, separator = separator), file = file_out, end = '')    
    print(") VALUES(", file = file_out, end = '')
    for i in range(0, count):
        separator = ', '
        if (i == count - 1):
            separator = ''
        print("?{separator}".format(separator = separator), file = file_out, end = '')    
    print(");\"", file = file_out, end = '\n')
    print("".ljust(4) + ";", file = file_out, end = '\n')
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')  # empty line
    print("", file = file_out, end = '\n')

    
# generate sqlite3_bind_xxx statements for all fields
# sqlite3_bind_text(pStatement, 1, pPerson->uuid, -1, NULL);# sqlite3_bind_int(pStatement, 33, DBM_DATA_OPERATION_C);
def gen_sqlite3_bind_all(entity, file_out):
    global G_namespace_PREFIX, G_namespace_prefix;
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_type;
    count = len(entity.fields);
        
    print("static int {prefix}_entityBind{entity_name}(DBM_DbStatement *pStatement, const {entity_type} *{instance})"
          .format(prefix = G_namespace_PREFIX, entity_name = entity_name, entity_type = entity_type, instance = instance), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')
    print("".ljust(4) + "int ret = 0;", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    
    for i in range(0, count):
        sqlite3_bind = G_sql_types[type_sql][2]
        print("".ljust(4)
              + "ret |= {sqlite3_bind}".format(sqlite3_bind = sqlite3_bind).ljust(28)
              + "(pStatement, "
              + "{param_index}, ".format(param_index = i + 1).ljust(4)
              + "{instance}->{field_name}".format(instance = instance, field_name = field.name).ljust(35),
              file = file_out, end = '')
        if ("sqlite3_bind_text" == sqlite3_bind):  
            print(", -1, NULL".ljust(10), file = file_out, end = '')
        else:
            print(" ".ljust(10), file = file_out, end = '')  # to make them align
        print(");".ljust(4), file = file_out, end = '')
        print("/* [{counter}] */".format(counter = i), file = file_out, end = '\n')
    
    print("", file = file_out, end = '\n')
    print("".ljust(4) + "return SQLITE_OK == ret ? OSA_STATUS_OK : OSA_STATUS_EINVAL;", file = file_out, end = '\n')
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    
    
# generate sqlite3_bind_xxx statements used for INSERTing or UPDATing database records
def gen_sqlite3_bind(entity, file_out):
    global G_namespace_PREFIX, G_namespace_prefix;
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_name;
    count = len(entity.fields);
    attr_pattern = r'ATTR\s*:\s*(.+)\s*;'                     # e.g., ATTR:AUTO_ON_C(DATETIME), NO_U();
    auto_c_pattern = r'AUTO_ON_C\s*\(\s*([A-Z]+)\s*\)'        # e.g., AUTO_ON_C(DATETIME)
    auto_u_pattern = r'AUTO_ON_U\s*\(\s*([A-Z]+)\s*\)'        # e.g., AUTO_ON_U(DATETIME)
    no_u_pattern   = r'NO_U\s*\(\s*\)'                        # e.g., NO_U()
    updating_allowed = True
        
    print("static int DBM_entityBind{entity_name}(const DBM_BindType bindType, DBM_DbStatement *pStatement, const {entity_type} *{instance})"
          .format(entity_name = entity_name, entity_type = entity_type, instance = instance), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')
    print("".ljust(4) + "int ret = 0;", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    
    for i in range(0, count):
        field = entity.fields[i];
        updating_allowed = True
        field_value = "{instance}->{field_name}".format(instance = instance, field_name = field.name)
        destructor = "NULL"
              
        # check field attributes
        for attr in field.attributes:
            if (dbm_field.ValueProvider.Auto_On_Creation == attr.value_provider):
                destructor = "SQLITE_TRANSIENT";
                if (dbm_field.ValueType.Flag == attr.value_type):
                    field_value = "DBM_BIND_TYPE_INSERT == bindType ? DBM_DATA_OPERATION_C : DBM_DATA_OPERATION_U";
                elif (dbm_field.ValueType.Sync == attr.value_type):
                    field_value = "DBM_BIND_TYPE_INSERT == bindType ? DBM_DATA_SYNC_UNSYNCED : " + field_value;
                else:  # for date, time, datetime, UUID
                    # "UUID"            : ["Char val_of_{field_name}[64];  DBM_utlGenUuid(val_of_{field_name}, sizeof(val_of_{field_name}));"],
                    field_value = "val_of_{field_name}".format(field_name = field.name);
            if (dbm_field.ValueProvider.No_Update == attr.value_provider):
                updating_allowed = False;
                print("".ljust(4) + "if (DBM_BIND_TYPE_INSERT == bindType) {    /* only generate on creation */", file = file_out, end = '\n')
                print("".ljust(8), file = file_out, end = '')  # ident
                print(attr.filling_expression, file = file_out, end = '\n');
                print("".ljust(4), file = file_out, end = '')  # deeper indet for next C statement
            if (dbm_field.ValueProvider.Auto_On_Update == attr.value_provider and dbm_field.ValueType.Flag != attr.value_type and dbm_field.ValueType.Sync != attr.value_type):
                destructor = "SQLITE_TRANSIENT"
                print("".ljust(4), file = file_out, end = '');
                print(attr.filling_expression, file = file_out, end = '\n');
         
        print("".ljust(4), file = file_out, end = '')  # ident
        aligned_len = 30
        if (not updating_allowed): aligned_len -= 4    # make them align
        print("ret |= {sqlite3_bind}".format(sqlite3_bind = field.db_set_func).ljust(aligned_len)              
              + "(pStatement, "
              + "{param_index}, ".format(param_index = i + 1).ljust(4)
              + "{field_value}".format(field_value = field_value).ljust(35),
              file = file_out, end = '')
        if ("sqlite3_bind_text" == field.db_set_func):  
            print(", -1, {destructor}".format(destructor = destructor).ljust(10), file = file_out, end = '')
        else:
            print(" ".ljust(10), file = file_out, end = '')  # to make them align
        print(");".ljust(4), file = file_out, end = '')
        print("/* [{counter}] */".format(counter = i), file = file_out, end = '\n')
        if (not updating_allowed):
            print("".ljust(4) + "}", file = file_out, end = '\n')        
    
    print("", file = file_out, end = '\n')
    print("".ljust(4) + "return SQLITE_OK == ret ? OSA_STATUS_OK : OSA_STATUS_EINVAL;", file = file_out, end = '\n')
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
      

def gen_sqlite3_construct(entity, file_out):
    global G_namespace_PREFIX, G_namespace_prefix;
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name);
    entity_name = entity.singular_name;
    instance = "p" + entity_name;
    count = len(entity.fields);
        
    print("static void {prefix}_entityConstruct{entity_name}(DBM_DbStatement *pStatement, {entity_type} *{instance})"
          .format(prefix = G_namespace_PREFIX, entity_name = entity_name, entity_type = entity_type, instance = instance), file = file_out, end = '\n')
    print("{", file = file_out, end = '\n');
    
    for i in range(0, count):
        field = entity.fields[i];
        dest = "{instance}->{field_name}".format(instance = instance, field_name = field.name)        
        should_assign = True
        if ("CHAR" in field.c_type.upper()):
            src = "(Char *)".ljust(10) + "sqlite3_column_text".ljust(22) + "(pStatement, ".ljust(10) + "{counter})".format(counter = i).ljust(4)
            should_assign = False   # strings should retrieve by copy, not assign
            print("".ljust(4) + "OSA_strncpy({dest}, ".format(dest = dest).ljust(40)
                  + "{src}".format(src = src).ljust(20)
                  + ");".ljust(4),
                  file = file_out, end = '')
        elif ("INT" in field.c_type.upper()):   sqlite3_column_xxx = "sqlite3_column_int64"
        elif ("FLOAT" in field.c_type.upper()): sqlite3_column_xxx = "sqlite3_column_double"
        else: print("Cannot determine how to retrieve data fro C data type " + field.c_type)
        if (should_assign):
            print("".ljust(4)
                  + "{instance}->{field_name} = ".format(instance = instance, field_name = field.name).ljust(40)
                  + "({field_type_c})".format(field_type_c = field.c_type).ljust(10)
                  + "{sqlite3_column_xxx}".format(sqlite3_column_xxx = sqlite3_column_xxx).ljust(22)
                  + "(pStatement, ".ljust(10)
                  + "{counter}".format(counter = i).ljust(4)
                  + ");".ljust(4),
                  file = file_out, end = '')
        print("/* [{counter:02}] */".format(counter = i), file = file_out, end = '\n')
    
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n' * 2)    


def gen_sqlite3(entities, path):
    try:        
        file_out = open(path, mode = "w+", encoding = "utf8")
    except OSError as e:
        print("Failed to open file for writing: " + str(e.errno) + e.strerror) 

    print('#pragma region SQLite3 INSERT Statements', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_sqlite3_INSERT_statement(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n' * 2);
    
    print('#pragma region SQLite3 bind', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_sqlite3_bind(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n');
    
    print('#pragma region SQLite3 construct entities', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_sqlite3_construct(entity, file_out);
    print('#pragma endregion', file = file_out, end = '\n' * 2);
            
    file_out.close()


def main(entities, path):
    gen_sqlite3(entities, path);