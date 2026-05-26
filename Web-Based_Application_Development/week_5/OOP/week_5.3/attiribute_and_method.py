class Ogrenci:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
    def selamla(self):
            print(f"Merhaba, ben {self.ad}")
            
            
o1 = Ogrenci("Mehmet", 19)
o1.selamla()
