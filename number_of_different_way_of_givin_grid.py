#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:29:07 2024

@author: ahmetcolak
"""

from math import factorial
def different_way(x,y):
    sonuc = factorial(x+y)/(factorial(x)*factorial(y))
    print(int(sonuc))
different_way(20,20)