class Kayit:
    def __init__(self, id, ad, telefon):
        self.id = id
        self.ad = ad
        self.telefon = telefon


kayitlar = [
    Kayit(1, "Ali", "0555..."),
    Kayit(2, "Ayse", "0532...")
]

for k in kayitlar:
    print(k.ad, k.telefon)
