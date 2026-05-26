# ============================================
# STORAGE.PY - Dosya Islemleri
# ============================================

from models import Record


def load_records(dosya="kayitlar.txt"):
    """Dosyadan kayitlari oku ve Record nesne listesi olustur
    
    - Dosya yoksa bos liste don
    - Her satiri Record nesnesine cevirme
    - Bos satirlari atla
    """
    try:
        with open(dosya, "r", encoding="utf-8") as f:
            return [Record.from_line(satir) for satir in f if satir.strip()]
    except FileNotFoundError:
        return []


def append_record(kayit, dosya="kayitlar.txt"):
    """Yeni kayi dosyaya ekle
    
    - to_line() ile Record nesnesini satirina cevirme
    - Dosya sonuna yazma (append mode)
    """
    try:
        with open(dosya, "a", encoding="utf-8") as f:
            f.write(kayit.to_line() + "\n")
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False


def save_records(kayitlar, dosya="kayitlar.txt"):
    """Tum kayitlari dosyaya yeniden yaz
    
    - Tum Record nesnelerini satirlara cevirme
    - Dosya w modunda yeniden yazilma (silme+yazma)
    """
    try:
        with open(dosya, "w", encoding="utf-8") as f:
            for kayit in kayitlar:
                f.write(kayit.to_line() + "\n")
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False


def next_id(kayitlar):
    """Sonraki ID numarasini hesapla"""
    if not kayitlar:
        return 1
    return max(k.id for k in kayitlar) + 1
