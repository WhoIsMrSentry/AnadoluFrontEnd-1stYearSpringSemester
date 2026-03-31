koordinat = (41.0082, 28.9784)  # İstanbul'un koordinatları
print(koordinat[0])  # 41.0082

gunler = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma")
# gunler[0] = "Pazar"  # Hata verir, çünkü tuple'lar değiştirilemez (immutable) yapılardır TypeError: 'tuple' object does not support item assignment
print(gunler)  # ('Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma')