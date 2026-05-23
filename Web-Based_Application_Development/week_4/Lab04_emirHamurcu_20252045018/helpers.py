# ============================================
# Hafta 4 - Dosya İşlemleri Yardımcı Fonksiyonları
# ============================================

# MARK: - Dosya Okuma
def gorevleri_oku(dosya_adi="gorevler.txt"):
    """Güvenli dosya okuma - dosya yoksa boş liste dön
    
    - Her satırı temizle
    - Boş satırları atla
    """
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            return [satir.strip() for satir in f if satir.strip()]
    except FileNotFoundError:
        return []


# MARK: - Görev Ekleme
def gorev_ekle(kayit, dosya_adi="gorevler.txt"):
    """Görev ekleme - dosya sonuna yeni kayıt ekle
    
    - Yeni kayıt satırını oluştur
    - a modunda dosya sonuna ekle
    - Hata olursa kullanıcıyı bilgilendir
    """
    try:
        with open(dosya_adi, "a", encoding="utf-8") as f:
            f.write(kayit + "\n")
        return True
    except Exception as e:
        print(f"Kayıt hatası: {e}")
        return False


# MARK: - Görev Silme
def gorev_sil(indeks, dosya_adi="gorevler.txt"):
    """Silme işlemi
    
    - Önce tüm satırları oku
    - Silinecek satırı listeden çıkar
    - Dosyayı w modu ile baştan yaz
    """
    satirlar = gorevleri_oku(dosya_adi)
    if 0 <= indeks < len(satirlar):
        yeni_satirlar = []
        for i, satir in enumerate(satirlar):
            if i != indeks:
                yeni_satirlar.append(satir)
        
        try:
            with open(dosya_adi, "w", encoding="utf-8") as f:
                for satir in yeni_satirlar:
                    f.write(satir + "\n")
            return True
        except Exception as e:
            print(f"Silme hatası: {e}")
            return False
    return False


# MARK: - Görev Arama
def gorev_ara(anahtar, dosya_adi="gorevler.txt"):
    """Görev arama - anahtar kelimeyi içeren görevleri bul"""
    satirlar = gorevleri_oku(dosya_adi)
    return [satir for satir in satirlar if anahtar.lower() in satir.lower()]


# MARK: - Sayı Girişi (Hata Kontrollü)
def int_input(prompt):
    """Kullanıcıdan sayı al - hata yönetimi ile"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")