kitapListesi = list()

menu = """
[1]=KitapEkle
[2]=KitapÇıkar
[3]=Listele
[q]=Çıkış

"""

def kitapEkle(kitap,liste):
    liste += [kitap]
    print("Kitap Eklendi...")
    input("Ana menüye dönmek için 'enter' a basın!")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print("Kitap Adı : {}".format(i))
        input("Ana menüye dönmek için 'enter' a basın!")


def cik():
    quit()

while True:
    print(menu)

    secim = input("Seçiminiz: ")

    if secim == "1":
        kitapAdi = input("Kitap Adı:")
        kitapEkle(kitapAdi,kitapListesi)

    elif secim == "2":
        kitapCikar()

    elif secim == "3":
        listele(kitapListesi)

    elif secim == "q" or secim == "Q":
        cik()

    else:
        print("Hatalı Giriş")
        input("Ana menüye dönmek için 'enter' a basınız!")
