kitaplar = [
    {"ad": "Kitap A", "yazar": "Yazar 1", "fiyat": 20},
    {"ad": "Kitap B", "yazar": "Yazar 2", "fiyat": 15},
    {"ad": "Kitap C", "yazar": "Yazar 3", "fiyat": 25},
]

sirali = sorted (kitaplar, key=lambda x: x["fiyat"])
print(sirali)