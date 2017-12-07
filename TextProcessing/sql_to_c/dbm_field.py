#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.

from enum import IntEnum


class CtypesEnum(IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)    
    
class DbKeyType(CtypesEnum):
    Nothing                               = 0
    PlainKey                              = 1
    PrimaryKey                            = 2
    ExternalKey                           = 3
    
class ValueType(CtypesEnum):
    Nothing                               = 0
    Date                                  = 1
    Datetime                              = 2
    UUID                                  = 3
    Flag                                  = 4
    Sync                                  = 5
    
class ValueProvider(CtypesEnum):
    Nothing                               = 0
    UserProvided                          = 1
    Auto_On_Creation                      = 2
    Auto_On_Update                        = 3
    No_Update                             = 4    
    
class FieldAttribute:
    def __init__(self):
        self.db_key_attr                  = DbKeyType.PlainKey;        
        self.value_type                   = ValueType.Nothing;
        self.value_provider               = ValueProvider.UserProvided;
        self.filling_expression           = '';           # the expression for providing value for this field


class Field:
    def __init__(self):
        self.name                         = '';
        self.db_set_func                  = '';           # database API for set a field's value
        self.db_type                      = '';
        self.c_type                       = '';
        self.c_format_spec                = '';
        self.python_type                  = '';           # for Python.ctypes
        self.comment                      = '';
        self.length                       = 0 ;           # e.g., the size for an array        
        self.attributes                   = [];           # [FieldAttribute]
  
