ogrenci = {
    "ad": "Emir",
    "soyad": "Hamurcu",
    "yas": 20,
    "bolum": "Gömülü Sitemler Mühendisliği"
}

print(ogrenci["ad"])  # Emir
print(ogrenci["soyad"])  # Hamurcu
print(ogrenci["yas"])  # 20
print(ogrenci["bolum"])  # Gömülü Sitemler Mühendisiliği

ogrenci["sehir"] = "İstanbul"  # yeni bir anahtar-değer çifti ekler
print(ogrenci)  # {'ad': 'Emir', 'soyad': 'Hamurcu', 'yas': 20, 'bolum': 'Gömülü Sitemler Mühendisliği', 'sehir': 'İstanbul'} 
