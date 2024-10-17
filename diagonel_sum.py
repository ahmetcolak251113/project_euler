#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:40:14 2024

@author: ahmetcolak
"""


diagonal_sum = 1
for n in range(3,1002,2):
    diagonal_sum += 4*n**2-6*(n-1)
print(diagonal_sum)