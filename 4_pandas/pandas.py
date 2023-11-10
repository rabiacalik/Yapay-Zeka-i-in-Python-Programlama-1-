# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:00:14 2023

@author: calik
"""

# 1- pandas dataframe kullanmak için hızlı ve etkilidir
# 2- CSV ve text dosyalarını açıp inceleyip sonuclarımızı bu dosya tiplarine rahat bir şekilde kayıt edebilir
# 3- pandas bizim işimizi kolaylastırıyor for missing data 
# 4- reshape yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5- slicing ve indexing kolay
# 6- time series data analizinde çok yardımcı
# 7- pandas hız açısından optimize edilmiş hızlı bir kütüphanedir

import pandas as pd

dictionary = {"NAME" : ["ali", "veli", "kenan", "osman", "mert"],
              "AGE" :  [20, 10, 30, 4, 19],
              "MAAS":  [100, 200, 300, 400, 500]}

# dictionary için data frame yaratmıs oluyoruz
dataFrame1 = pd.DataFrame(dictionary)

# datanın içerisindeki ilk 5 elemanı verir / daha cok datanın içeriginde ne oldugunu ogrenmek için kullanırız
head = dataFrame1.head()

# sondan 5 elemanını gösterir
tail = dataFrame1.tail()

# tail ve head içerisine parametre olarak sayı girdigimizde bastan yada sondan girilen parametre kadar deger gosterir

# %% Pandas Basic Method

# sutunları gosterir AGE NAME MAAS gibi
columns = dataFrame1.columns

# data hakkında bilgiler verir
info = dataFrame1.info()

# herbir columns un data type nı verir
columns_type = dataFrame1.dtypes



# caunt = eleman sayısı
# mean = degerlerin ortalama degeri
# std = 
# min = min degeri
# 25% = 
# 50% =
# 75% = 
# max = max degeri
describe = dataFrame1.describe()
#              AGE        MAAS
# count   5.000000    5.000000
# mean   16.600000  300.000000
# std     9.989995  158.113883
# min     4.000000  100.000000
# 25%    10.000000  200.000000
# 50%    19.000000  300.000000
# 75%    20.000000  400.000000
# max    30.000000  500.000000





















