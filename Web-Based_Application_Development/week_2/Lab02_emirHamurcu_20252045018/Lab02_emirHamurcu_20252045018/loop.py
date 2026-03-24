# Görev 3 — Döngü ile tekrar
#  for kullanarak 1’den 10’a kadar sayıları yazdırınız.
#  while kullanarak 1’den N’e kadar sayıların toplamını bulunuz.
#  Kullanıcı 0 girene kadar sayıları toplayan bir program yazınız.

for i in range(1, 11):
    print(i)

while True:
    n = int(input("N değerini giriniz: "))
    if n < 1:
        print("Lütfen 1 veya daha büyük bir sayı giriniz.")
        continue
    toplam = sum(range(1, n + 1))
    print(f"1'den {n}'e kadar sayıların toplamı: {toplam}")
    break



toplam = 0
while True:
        sayi = int(input("Bir sayı giriniz (bitirmek için 0): "))
        if sayi == 0:
            break
        toplam += sayi
print(f"Girilen sayıların toplamı: {toplam}")