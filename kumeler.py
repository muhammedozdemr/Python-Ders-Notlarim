"""
Metodlar:
----------> Öğe Ekle   add
----------> Fark       difference
----------> Öğe Sil    discard
----------> Öğe Sil    remove
----------> Kesişim    intersection
"""
#discard kullanılırsa eğer eleman var ise elemanı çıkarır.eleman yoksa hata vermez.
#remove kullanılırsa eğer eleman var ise elemanı çıkarır.eleman yoksa hata verir.
#kume=set(liste,sozluk,demet kullanılabilir ama sayı oluşturulamaz.)
#bir öğe sadece bir kez eklenebilir.

kume=set([1,2,3,4])

kume.add("deneme")
kume.discard(3)
print(kume)
print(30*"=")

a=set([1,2,4,5])
b=set([2,4,5,6,7,8])

print("a kümesi :",a)
print("b kümesi :",b)

print(25*"=")

print("b'nin a'dan farkı: ",b.difference(a))
print("a'nın b'den farkı: ",a.difference(b))

print(30*"=")

b.difference_update(a)

print("b kümesi güncellendi:",b)

print(30*"=")

c=set([1,2,3,4,5,6,7,8,9])
d=set([2,4,6,7,10,12,0])
print("c kümesi:",c)
print("d kümesi:",d)

print("C ve d'nin kesişimi: ",c.intersection(d))
