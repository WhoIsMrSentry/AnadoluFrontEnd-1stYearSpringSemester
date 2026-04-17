from helpers import (int_input, metin_input, gorevleri_oku_finally, gorev_ekle, gorev_ara, gorev_sil, next_id)


def main():
    while True:
        print("1- Listele")
        print("2- Ekle")
        print("3- Ara")
        print("4- Sil")
        print("0- Çıkış")

        secim = input("Seçiminiz: ").strip()

        if secim == "0":
            print("Çıkış yapılıyor...")
            break
        elif secim == "1":
            gorevler = gorevleri_oku_finally()
            if gorevler:
                print("Görevler:")
                for i, g in enumerate(gorevler, start=1):
                    print(f"{i} - {g.strip()}")
            else:
                print("Görev bulunmuyor.")
        elif secim == "2":
            metin = metin_input("Yeni görev (kısa açıklama): ").strip()
            if not metin:
                print("Boş görev eklenemez.")
                continue
            gid = next_id()
            gorev_ekle(f"{gid} | {metin}")
            print("Görev eklendi.")
        elif secim == "3":
            anahtar = metin_input("Aranacak kelime: ").strip()
            if not anahtar:
                print("Boş anahtar girilemez.")
                continue
            bulunan = gorev_ara(anahtar)
            if bulunan:
                print("Bulunan görevler:")
                for g in bulunan:
                    print(f"- {g.strip()}")
            else:
                print("Eşleşen görev bulunamadı.")
        elif secim == "4":
            indeks = int_input("Silinecek görev sıra numarası: ")
            if indeks <= 0:
                print("Geçersiz sıra numarası.")
                continue
            if gorev_sil(indeks - 1):
                print("Görev silindi.")
            else:
                print("Geçersiz sıra numarası.")
        else:
            print("Geçersiz seçim. Tekrar deneyin.")


if __name__ == "__main__":
    main()
