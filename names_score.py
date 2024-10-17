#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:20:32 2024

@author: ahmetcolak
"""

# İngiliz alfabesi ve harflerin sayısal değerlerini tanımlayalım
import string

alphabet_values = {letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)}

# Her ismin harflerinin sayısal toplamını hesaplayan fonksiyon
def name_value(name):
    return sum(alphabet_values[letter] for letter in name)

# Dosya yolunu belirtelim
file_path = 'names.txt'

# Dosyayı açıp, isimleri okuyalım ve işleyelim
with open(file_path, 'r') as file:
    # Dosyadaki isimleri alalım ve çift tırnaklardan temizleyelim
    content = file.read().replace('"', '')
    
    # İsimleri virgül ile ayırarak listeleyelim
    names = content.split(',')
    
    # İsimleri alfabetik sıraya göre sıralayalım
    names_sorted = sorted(names)

# İsimlerin sıralı hallerine göre her birinin sayısal değerini ve sırasını bulalım
total_score = 0
for i, name in enumerate(names_sorted):
    # İsmin sayısal değerini hesaplayalım
    name_score = name_value(name)
    
    # İsmin sıralamadaki yerini çarpalım (sıra numarası 1'den başlamalı, bu yüzden i+1)
    total_score += name_score * (i + 1)

# Toplam sonucu yazdıralım
print(total_score)
