urun = {"ad": "kitap", "fiyat": 20, "stok": 100}

print(urun.keys())  # dict_keys(['ad', 'fiyat', 'stok'])
print(urun.values())  # dict_values(['kitap', 20, 100])
print(urun.get("marka", "Bilinmiyor"))  # Bilinmiyor, çünkü "marka" anahtarı yok

for anahtar, deger in urun.items():
    print(anahtar, "=>", deger) # ad => kitap fiyat => 20 stok => 100