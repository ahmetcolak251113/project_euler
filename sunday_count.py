#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:12:42 2024

@author: ahmetcolak
"""

import datetime

# Başlangıç ve bitiş tarihlerini tanımlıyoruz
start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)

# 1'inin pazar olduğu ayların sayısı
sunday_count = 0

# 1901'den 2000'e kadar her ayın 1'ini kontrol edelim
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:  # 6 Pazar gününü temsil eder
            sunday_count += 1

print(sunday_count)
