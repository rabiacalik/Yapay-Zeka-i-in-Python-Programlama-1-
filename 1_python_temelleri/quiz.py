# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:14:35 2023

@author: calik
"""
# ----SORU----
# verilen listenin icerisindeki en kucuk elemani bul
# liste = [1, 3, 2, 20, -5, 6, 5]

liste = [1, 3, 2, 20, -5, 6, 5]
i = 0
small = 0
while(i < len(liste)):
    if (liste[i] < small):
        small = liste[i]
    i = i + 1

print(small)
        
