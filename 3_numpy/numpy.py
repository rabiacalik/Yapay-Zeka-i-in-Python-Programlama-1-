# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:27:36 2023

@author: calik
"""

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(array.shape) #array matrisini bize veriyor

a = array.reshape(3, 5) #matrisi tekrar boyutlandırdık
print(a.shape)
print(a);

print("type : ", type(a)) #array

print("dimention : ", a.ndim) #kaç boyutlu bir dizi oldugunu döner

print("data type : ", a.dtype.name) #dizinin hangi tipte veri tuttugunu döner

print("size : ", a.size) 


array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #bu şekilde tanımlayarak, boyutlu dizi oluşturulabilir
print("array1 : ")
print(array1)

zeros = np.zeros((3, 4)) #sıfırlardan oluşan bir matris oluşturur. yer ayırır
print("zeros : ")
zeros[0][0] = 5
print(zeros)

ones = np.ones((3, 4)) #birlerden oluşan bir matris üretir
print("ones : ")
print(ones)

empty = np.empty((2, 4))
print("empty :")
print(empty)

a = np.arange(10, 50, 5) #10 ile 50 arasındaki sayıları 5er 5er ayır. 50 dahil degildir
print("ayrılmış sayılar : ", a)

b = np.linspace(10, 50, 20) #10 ile 50 arasında 20 tane sayı üretti
print("rastgele sayı uretildi : ", b)

# %% Numpy basic operation

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a**2) #karesini alıyor
print(a**3) #kupunu alıyor

print(np.sin(a)) # a arrayin in sin degerleri

print(a < 2) # 2 den kucuk olanlara 'true', büyük olanlara 'false' donecek

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[7, 8, 9], [10, 11, 12]])

#element wise prodcut
print(c * d) 

#matris prodcut
print(a.dot(b.T))

a = np.random.random((5, 5)) #0 ile 1 arasında random 
print(a)

# %% İndex and Slicing

import numpy as np #spyder ı açıp kapatınca bu tanımlamayı unutuyormus o yuzden tekrar tanımladım

array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(array)

reverse_array = array[::-1] #tamamen ters çevirdik
print(reverse_array)

array1 = np.array([[1, 2, 3], [4, 5, 6]])

print(array1)
print(array1[1, 1])

print(array1[:, 1])

print(array1[1, 1:4])

# %% Shape Manipulation

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("array :")
print(array)

#flatten / arrayi düz tek bir dizi haline getiriyor / çözülme
a = array.ravel()
print("array.ravel :")
print(a)

array2 = a.reshape((3, 3))
print("reshape array 3,3 :")
print(array2)

array_transpose = array2.T
print("array transpose : ")
print(array_transpose)

# %% Stacking Array

array_positive = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array_negative = np.array([[-1, -2, -3, -4], [-5, -6, -7, -8]])

print("array_positive : ")
print(array_positive)

print("array_negative : ")
print(array_negative)

#horizontal combining
array_horizontal = np.hstack((array_positive, array_negative))
print("horizontal combining array_positive and array_negative : ")
print(array_horizontal)

#vertical combining
array_vertical = np.vstack((array_positive, array_negative))
print("vertival combining array_positive and array_negative : ")
print(array_vertical)

# %% Convert and Copy

liste = [1, 2, 3, 4] #list
print("liste = ", liste)

array = np.array(liste) #donuşum yapıldı
print("conversion from list to array : ",array)

liste2 = list(array)
print("conversion from array to list : ", liste2)

























