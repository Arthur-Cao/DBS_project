#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:55:44 2018

@author: Cris
"""

def split_5k (string, width):
    return [string[x:x+width] for x in range(0,len(string),width)]
