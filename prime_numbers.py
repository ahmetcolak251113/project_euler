#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:25:13 2024

@author: ahmetcolak
"""
def prime_numbers(mn, mx):
    prime_list = []
    for i in range(mn, mx + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if (i % j) == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# 1 ile 100 arasındaki asal sayıları listeleyelim
primes = prime_numbers(1, 1000000)
print(primes[10000])
