# dir fonksiyonu

liste=["deneme1","deneme2"]
"""
for i in dir(liste):
    print(i,end=",") # dir fonksiyonunda kullanılan parametreleri ekrana yazdırma
"""

liste.append("deneme3") #append kullanılarak listeye ekleme yapıldı
print(liste)

liste.remove("deneme1") #remove kullanılarak listedeki belirtilen içeriği silme işlemi
print(liste)
