#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:51:31 2024

@author: ahmetcolak
"""
nums = range(1000)
for a in nums:
    for b in nums:
        for c in nums:
            if a < b and b < c:
                if (a**2 + b**2 == c**2) and a + b + c == 1000:
                    print('a = ',a)
                    print('b = ',b)
                    print('c = ',c)
                    print(a*b*c)