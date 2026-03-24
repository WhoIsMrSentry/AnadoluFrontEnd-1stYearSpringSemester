bakiye = 1000
toplam_yatirilan = 0
toplam_cekilen = 0
islem_sayisi = 0
hatali_secim_sayisi = 0

def islem_ozeti_goster():
    print("\n--- İşlem Özeti ---")
    print(f"Toplam yatırılan miktar: {toplam_yatirilan} TL")
    print(f"Toplam çekilen miktar: {toplam_cekilen} TL")
    print(f"Toplam işlem sayısı: {islem_sayisi}")

while True:
    print("\n--- ATM Menüsü ---")
    print("1- Bakiye görüntüle")
    print("2- Para yatır")
    print("3- Para çek")
    print("4- İşlem özeti")
    print("5- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        print(f"Mevcut bakiyeniz: {bakiye} TL")
        hatali_secim_sayisi = 0
    elif secim == "2":
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
        if miktar > 0:
            bakiye += miktar
            toplam_yatirilan += miktar
            islem_sayisi += 1
            print(f"{miktar} TL yatırıldı. Yeni bakiyeniz: {bakiye} TL")
        else:
            print("Lütfen pozitif bir miktar giriniz.")
        hatali_secim_sayisi = 0
    elif secim == "3":
        miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
        if miktar > 0:
            if miktar <= bakiye:
                bakiye -= miktar
                toplam_cekilen += miktar
                islem_sayisi += 1
                print(f"{miktar} TL çekildi. Yeni bakiyeniz: {bakiye} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Lütfen pozitif bir miktar giriniz.")
        hatali_secim_sayisi = 0
    elif secim == "4":
        islem_ozeti_goster()
        hatali_secim_sayisi = 0
    elif secim == "5":
        print("Çıkış yapılıyor. İyi günler!")
        islem_ozeti_goster()
        devam = input("Yeni işlem yapmak ister misiniz? (E/H): ").strip().lower()
        if devam == "e":
            continue
        else:
            break
    else:
        hatali_secim_sayisi += 1
        print("Geçersiz menü seçimi! Lütfen tekrar deneyin.")
        if hatali_secim_sayisi >= 3:
            print("3 kez hatalı seçim yaptınız. Lütfen menüden geçerli bir seçenek giriniz!")
