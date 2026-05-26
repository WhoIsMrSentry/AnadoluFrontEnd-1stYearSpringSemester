# ============================================
# MAIN.PY - Kayit Yoneticisi Ana Programi
# ============================================

from models import Record
from storage import load_records, append_record, save_records, next_id


# MARK: - Yardimci Fonksiyonlar

def find_by_id(kayitlar, id):
    """ID ile kayi bul"""
    for kayit in kayitlar:
        if kayit.id == id:
            return kayit
    return None


def find_by_name(kayitlar, ad):
    """Ad ile kayit ara"""
    sonuc = []
    for kayit in kayitlar:
        if ad.lower() in kayit.ad.lower():
            sonuc.append(kayit)
    return sonuc


# MARK: - Menu Fonksiyonlari

def listele(kayitlar):
    """Tum kayitlari listele"""
    if not kayitlar:
        print("Kayit bulunamadi.")
        return
    
    print("\n" + "="*50)
    print("KAYITLAR")
    print("="*50)
    for kayit in kayitlar:
        print(kayit)
    print("="*50)


def ekle(kayitlar):
    """Yeni kayit ekle"""
    ad = input("Ad: ").strip()
    telefon = input("Telefon: ").strip()
    
    if not ad or not telefon:
        print("Ad ve telefon bos olamaz!")
        return
    
    # Yeni Record nesnesi olustur
    yeni_kayit = Record(next_id(kayitlar), ad, telefon)
    
    # Dosyaya ekle
    if append_record(yeni_kayit):
        kayitlar.append(yeni_kayit)
        print(f"✓ Kayit eklendi: {yeni_kayit}")
    else:
        print("✗ Kayit eklenemedi.")


def ara(kayitlar):
    """Kayit ara"""
    aranacak = input("Aranacak ad: ").strip()
    
    if not aranacak:
        print("Bos arama yapilan!")
        return
    
    bulunan = find_by_name(kayitlar, aranacak)
    
    if bulunan:
        print(f"\n{len(bulunan)} kayit bulundu:")
        for kayit in bulunan:
            print(f"  {kayit}")
    else:
        print("Kayit bulunamadi.")


def sil(kayitlar):
    """Kayit sil"""
    if not kayitlar:
        print("Silinecek kayit yok.")
        return
    
    listele(kayitlar)
    
    try:
        id = int(input("\nSilinecek kayt ID'si: "))
        kayit = find_by_id(kayitlar, id)
        
        if kayit:
            kayitlar.remove(kayit)
            save_records(kayitlar)
            print(f"✓ Kayit silindi: {kayit}")
        else:
            print("Kayit bulunamadi.")
    except ValueError:
        print("Hata: Sayi girin.")


# MARK: - Ana Menu

def main():
    """Ana program - Menu loop"""
    
    kayitlar = load_records()
    
    while True:
        print("\n" + "="*50)
        print("KAYIT YONETICISI")
        print("="*50)
        print("1. Listele")
        print("2. Ekle")
        print("3. Ara")
        print("4. Sil")
        print("0. Cikis")
        print("="*50)
        
        secim = input("Secim: ").strip()
        
        if secim == "0":
            print("Programdan cikiliyor...")
            break
        elif secim == "1":
            listele(kayitlar)
        elif secim == "2":
            ekle(kayitlar)
        elif secim == "3":
            ara(kayitlar)
        elif secim == "4":
            sil(kayitlar)
        else:
            print("Gecersiz secim. Tekrar deneyin.")


if __name__ == "__main__":
    main()
