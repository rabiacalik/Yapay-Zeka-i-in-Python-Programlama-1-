# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:26:25 2023

@author: calik
"""
#----Class----

class Calisan:
    zam_orani = 1.18
    calisan_counter = 0
    
    def __init__(self, isim, soyisim, maas): #Constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas;
        self.mail = soyisim + isim + "@gmail.com"
    
        Calisan.calisan_counter = Calisan.calisan_counter + 1;
        
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
    
    def zam_yap(self):
        self.maas = self.maas + self.maas * self.zam_orani
    
isci = Calisan("rabia", "calik", 20000)

print(isci.isim)
print(isci.soyisim)
print(isci.maas)
print(isci.mail)

print(isci.giveNameSurname())
        
isci.zam_yap()
print(isci.maas)