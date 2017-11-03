#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Created by Papillon. Oct 31, 2017.

import dbm_field


class Entity:
    def __init__(self):
        self.name                      = '';
        self.singular_name             = '';
        self.plural_name               = '';
        self.fields                    = [];       # a list of `Field`s
        
    def print(self, file):
        print('name = ' + self.name, file = file);
