kitaplar = [
    {"ad": "Sefiller", "yazar": "Victor Hugo", "yil": 1862},
    {"ad": "Suç ve Ceza", "yazar": "Fyodor Dostoevsky", "yil": 1866},
    {"ad": "Savaş ve Barış", "yazar": "Leo Tolstoy", "yil": 1869}
 ]


for kitap in kitaplar:
    print(kitap["ad"], "-", kitap["yazar"], "(", kitap["yil"], ")")
