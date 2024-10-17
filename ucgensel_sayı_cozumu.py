#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:23:26 2024

@author: ahmetcolak
"""

import math

# Bölen sayısını hesaplamak için fonksiyon
def bolen_sayisi(sayi):
    sayac = 0
    # 1'den sqrt(sayi)'ye kadar olan sayılara bakarak bölenlerini buluruz.
    for i in range(1, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            if i == sayi // i:
                sayac += 1  # Eğer tam kare bir sayı ise, çift saymamalıyız
            else:
                sayac += 2  # Hem i hem de sayi // i birer bölen
    return sayac

# 500'den büyük böleni olan en küçük üçgensel sayıyı bulmak
def ucgensel_bul(bolen_limiti):
    n = 1
    while True:
        ucgensel_sayi = int(n * (n + 1) / 2)  # n'inci üçgensel sayı
        bolen_sayisi_ucgensel = bolen_sayisi(ucgensel_sayi)  # Bu sayının bölen sayısı
        if bolen_sayisi_ucgensel > bolen_limiti:
            return ucgensel_sayi, n, bolen_sayisi_ucgensel
        n += 1

# 500'den büyük bölen sayısına sahip olan en küçük üçgensel sayıyı bulalım
ucgensel_sayi, n, bolen_sayisi_ucgensel = ucgensel_bul(500)
ucgensel_sayi, n, bolen_sayisi_ucgensel
