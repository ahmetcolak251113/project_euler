#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:55:11 2024

@author: ahmetcolak
"""

def power_digit_sum(num,power):
    number = num**power
    number = str(number)
    liste = []
    for i in number:
        liste.append(i)
    print(sum(map(int,liste)))

power_digit_sum(2, 1000)
    