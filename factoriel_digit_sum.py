#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:04:28 2024

@author: ahmetcolak
"""
liste = []
def factoriel_digit_sum(n):
    # factoriel:
    mult = 1
    j = 1
    while j<=n:
        mult = mult * j
        j = j + 1
    print(mult)
    # factoriel digit sum:
    strm = str(mult)
    for i in strm:
        liste.append(int(i))
    print(sum(liste))
        
    
factoriel_digit_sum(100)


    