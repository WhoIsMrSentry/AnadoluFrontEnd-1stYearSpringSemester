# ============================================
# Hafta 4 - Dosya İşlemleri Ana Programı
# ============================================

# MARK: - İçe Aktarmalar
from helpers import gorevleri_oku, gorev_ekle, gorev_ara, gorev_sil, int_input


# MARK: - Ana İşlev
def main():
    """Ana menü - Kullanıcı akışı
    
    while True ile sürekli menü döngüsü
    Yanlış seçimlerde uyarı
    """
    # MARK: - Menü Döngüsü
    while True:
        print("\n" + "=" * 30)
        print("GÖREV YÖNETİMİ")
        print("=" * 30)
        print("1- Listele")
        print("2- Ekle")
        print("3- Ara")
        print("4- Sil")
        print("0- Çıkış")
        print("=" * 30)
        
        secim = input("Seçim: ").strip()
        
        # MARK: - Çıkış
        if secim == "0":
            print("Çıkış yapılıyor...")
            break
        
        # MARK: - Seçim 1: Listele
        elif secim == "1":
            # Görevleri listele
            gorevler = gorevleri_oku()
            if gorevler:
                print("\nGÖREVLER:")
                for i, gorev in enumerate(gorevler, start=1):
                    print(f"{i}. {gorev}")
            else:
                print("Görev bulunmuyor.")
        
        # MARK: - Seçim 2: Ekle
        elif secim == "2":
            # Yeni görev ekle
            kayit = input("Yeni görev: ").strip()
            if not kayit:
                print("Boş görev eklenemez.")
                continue
            
            if gorev_ekle(kayit):
                print("✓ Görev eklendi.")
            else:
                print("✗ Görev eklenemedi.")
        
        # MARK: - Seçim 3: Ara
        elif secim == "3":
            # Görev ara
            anahtar = input("Aranacak kelime: ").strip()
            if not anahtar:
                print("Boş anahtar girilemez.")
                continue
            
            bulunan = gorev_ara(anahtar)
            if bulunan:
                print("\nBULUNAN GÖREVLER:")
                for gorev in bulunan:
                    print(f"- {gorev}")
            else:
                print("Eşleşen görev bulunamadı.")
        
        # MARK: - Seçim 4: Sil
        elif secim == "4":
            # Görev sil
            gorevler = gorevleri_oku()
            if not gorevler:
                print("Silinecek görev yok.")
                continue
            
            print("\nGÖREVLER:")
            for i, gorev in enumerate(gorevler, start=1):
                print(f"{i}. {gorev}")
            
            try:
                indeks = int_input("\nSilinecek görev numarası: ")
                if indeks <= 0 or indeks > len(gorevler):
                    print("Geçersiz numaralandırma.")
                    continue
                
                if gorev_sil(indeks - 1):
                    print("✓ Görev silindi.")
                else:
                    print("✗ Görev silinemedi.")
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin.")
        
        # MARK: - Geçersiz Seçim
        else:
            print("Geçersiz seçim. Tekrar deneyin.")


# MARK: - Program Giriş Noktası
if __name__ == "__main__":
    main()

