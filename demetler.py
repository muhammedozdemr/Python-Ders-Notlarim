"""
Demet(tuple), içeriğinde her türlü veri türünü tutabilir.
Listede ekleme çıkarma yapılabilir ama demetde ekleme ve çıkarma yapılamaz
Demetler listelerden daha hızlı çalışır.

"""
print("============================")
liste=["deneme"]
print(type(liste)) #veri tipini ekrana yazdırır.

print("============================")
demet=tuple()
print(type(demet)) #veri tipini ekrana yazdırır.

print("=============================")
demet=tuple()
demet+=("abc")
print(demet) #Çalışmaz hata verir.

print("=============================")
liste=["a"]
liste+=["b"]
print(liste) #['a','b'] ekrana yazdırır.
