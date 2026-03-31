urunler = ["kitap", "defter", "kalem", "silgi", "boya"]

print(urunler[:3])  # ['kitap', 'defter', 'kalem']
print(urunler[2:])   # ['kalem', 'silgi', 'boya']
print(urunler[1:4])  # ['defter', 'kalem', 'silgi']

for urun in urunler:
    print(urun)