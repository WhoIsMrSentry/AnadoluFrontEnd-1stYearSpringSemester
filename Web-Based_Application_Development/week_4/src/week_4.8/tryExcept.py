try:
    sayi = int(input("Bir sayı girin: "))
    print(f"Girdiğiniz sayı: {sayi}")
except ValueError:
    print("Geçerli bir sayı girmediniz.")