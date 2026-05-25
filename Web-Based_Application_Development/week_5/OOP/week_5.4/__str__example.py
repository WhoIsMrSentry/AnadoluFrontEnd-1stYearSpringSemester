class Kayit:
    def __init__(self, id, ad, telefon):
        self.id = id
        self.ad = ad
        self.telefon = telefon
    def __str__(self):
            return f"{self.id} - {self.ad} - {self.telefon}"

