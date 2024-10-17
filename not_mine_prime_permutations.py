#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:45:30 2024

@author: ahmetcolak
"""

from itertools import permutations

# 4 basamaklı asal sayıları bulmak için bir fonksiyon
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tüm 4 basamaklı asal sayıları listeleyelim
primes = [i for i in range(1000, 10000) if is_prime(i)]

# Her asal sayı için permütasyonlarını kontrol edelim
for prime in primes:
    perm = set(int(''.join(p)) for p in permutations(str(prime)) if int(''.join(p)) in primes)

    # Eğer üç farklı asal sayı bir aritmetik dizi oluşturuyorsa
    if len(perm) >= 3:
        perm = sorted(perm)  # Küçükten büyüğe sırala
        for i in range(len(perm) - 2):
            for j in range(i + 1, len(perm) - 1):
                k = 2 * perm[j] - perm[i]
                if k in perm:
                    # Aritmetik diziyi bulduk, sayıları birleştirelim
                    result = str(perm[i]) + str(perm[j]) + str(k)
                    if perm[i] != 1487:  # 1487 örneğini dahil etmiyoruz
                        print(result)
