#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.

import dbm_field
import dbm_entity
import dbm_config


G_namespace_PREFIX = dbm_config.G_namespace_PREFIX;
G_namespace_prefix = dbm_config.G_namespace_prefix;


# OSA_info("%s = %s\n");
def gen_print_entity(entity, file_out):
    global G_namespace_PREFIX, G_namespace_prefix;
    entity_type = '{prefix}_{name}'.format(prefix = G_namespace_PREFIX, name = entity.singular_name); 
    entity_name = entity.singular_name;
    formal_var = "p" + entity_name;
    count = len(entity.fields);

    print("static void {prefix}_entityPrint{entity_name}(const {entity_type} *{formal_var})"
          .format(prefix = G_namespace_PREFIX, entity_name = entity.singular_name, entity_type = entity_type, formal_var = formal_var), 
          file = file_out, end = '\n')
    print("{", file = file_out, end = '\n')
    print("".ljust(4)
          + r'OSA_info("-- Printing all fields of {entity_type} at %p -- \n", '.format(entity_type = entity_type)
          + "{formal_var});".format(formal_var = formal_var), file = file_out, end = '\n')
    
    for i in range(0, count):
        field = entity.fields[i];
        print("".ljust(4)
              + "OSA_info(\"{field_name}".format(field_name = field.name).ljust(30)
              + "= {format_spec}\\n\", ".format(format_spec = field.c_format_spec).ljust(4)
              + "{formal_var}->{field_name}".format(formal_var = formal_var, field_name = field.name).ljust(40)
              + ");".ljust(4)
              + "/* [{counter}] */".format(counter = i),               
              file = file_out, end = '\n')    
    
    print("}", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')
    print("", file = file_out, end = '\n')


def gen(entities, path):
    try:        
        file_out = open(path, mode = "w+", encoding = "utf8")
    except OSError as e:
        print("Failed to open file for writing: " + str(e.errno) + e.strerror) 

    print('#pragma region Print Fields', file = file_out, end = '\n' * 3);
    for entity in entities:
        gen_print_entity(entity, file_out)
    print('#pragma endregion', file = file_out, end = '\n');
    
    file_out.close()


def main(entities, path):
    gen(entities, path)
