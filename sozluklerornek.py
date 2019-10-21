karakter={"ad":"Muhammed","güc":89,"can":100,"silah":"Kılıç"}

karakter2={"ad":"Oğuz","güc":58,"can":100,"silah":"Bıçak"}

def vur(vuran,vurulan):
    eksilen=vuran["güc"]
    vurulan["can"]=vurulan["can"]-eksilen

vur(karakter,karakter2)
vur(karakter2,karakter)

print("Karakter 1 Canı :",karakter["can"])
print("Karakter 2 Canı :",karakter2["can"])
