#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:24:48 2024

@author: ahmetcolak
"""
count = 0
for i in range(1,1001):
    count += i**i

str_count =str(count)

c = str_count[-10:]
print(c)
print(len(str(count)))