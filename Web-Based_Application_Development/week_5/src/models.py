# ============================================
# MODELS.PY - Kayit Sinifi
# ============================================

class Record:
    """Kayit nesne: id, ad, telefon
    
    Dosya satiri ile nesne arasinda donusum yapabiliyor
    """
    
    def __init__(self, id, ad, telefon):
        self.id = id
        self.ad = ad
        self.telefon = telefon
    
    def to_line(self):
        """Nesneyi dosya satirina cevirme: "1|Ali|05551234567" """
        return f"{self.id}|{self.ad}|{self.telefon}"
    
    @classmethod
    def from_line(cls, satir):
        """Dosya satirini nesneye cevirme: "1|Ali|05551234567" → Record(1, "Ali", "05551234567")"""
        id, ad, tel = satir.strip().split("|")
        return cls(int(id), ad, tel)
    
    def __str__(self):
        """Nesneyi yazdirma"""
        return f"{self.id}. {self.ad} - {self.telefon}"
    
    def __repr__(self):
        return self.__str__()
