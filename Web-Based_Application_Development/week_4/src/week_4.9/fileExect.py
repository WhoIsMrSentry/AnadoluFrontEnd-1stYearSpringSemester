dosya = None

try:
    dosya = open("gorevler.txt", "r", encoding="utf-8")
    icerik = dosya.read()
except FileNotFoundError:
    print("Dosya bulunamadı.")
else:
    print("Dosya başarıyla okundu.")
    print(icerik)

finally:
    if dosya:
        dosya.close()
        print("Dosya kapatıldı.")
