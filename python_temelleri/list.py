# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:28:45 2023

@author: calik
"""

# %% List

list_int = [1, 2, 3, 4, 5]

type(list_int)
print(list_int[0], list_int[1])

# (-) li degerlerde sondan sayarak liste elemanlarina bakar
print(list_int[-1])

# liste elemanlarini bu sekilde bolebiliriz
list_devide = list_int[0:3]

# Console ekranina "dir(list)" yazarak liste ile kullanilabilecek builtin fonksiyonlara bakabilirsin
# ['__add__',
#  '__class__',
#  '__class_getitem__',
#  '__contains__',
#  ...
#  ...
#  'pop',
#  'remove',
#  'reverse',
#  'sort']

# listeye eklema yapar
list_int.append(7)

# listeden çıkarma yapar
list_int.remove(7)

# listeyi kucukten buyuge dogru siralar
list2 = [8, 1, 4, 2, 5]
list2.sort()
print(list2)

# bir liste farkli veri turleri tutabilir
list3 = [1, 2, "rabia", "kopkop"]

# %% Tuple

t = (1, 2, 3, 4, 5)

# %% Dictionary

dictionary = {"ali":12, "ayse":15, "mehmet":30}
# keys = ali, ayse, mehmet
# value = 12, 15, 30

print(dictionary.keys())
print(dictionary.values())

# %% Conditionals
# if else statement

var1 = 10
var2 = 20

if (var1 > var2):
    print("var1, var2 den buyuktur")
elif (var1 < var2):
    print("var1, var2 den kucuktur")
else:
    print("var1, var2 ye esittir")


liste = [1, 2, 3, 4, 5]

if 6 in liste:
    print("evet, 6 degeri icerisinde")
else:
    print("hayir, 6 degeri icerisinde degil")


















