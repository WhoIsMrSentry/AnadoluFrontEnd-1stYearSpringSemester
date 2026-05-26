================================================
HAFTA 5 LAB PROJESI - KAYIT YONETICISI
================================================

PROJE ACIKLAMASI
================================================
Dosyaya yazan Kayit Yoneticisi fikri:
• Her kayit bir object (Record) olacak
• Dosyada her satir: id | ad | telefon
• Ozellikler: listele, ekle, ara, sil
• Program kapanip acilinca veriler dosyada kaliyor

Basit veri orneği:
1|Ali Kaya|05551234567
2|Zeynep Demir|05321234567
3|Can Yilmaz|05441234567


DOSYA YAPISI
================================================
models.py      → Record sinifi (to_line, from_line)
storage.py     → Dosya islemleri (load, save, append)
main.py        → Menu ve akis
kayitlar.txt   → Veri dosyasi
README.txt     → Bu dosya


MODELS.PY - KAYIT SINIFI
================================================

class Record:
    def __init__(self, id, ad, telefon):
        self.id = id
        self.ad = ad
        self.telefon = telefon
    
    def to_line():
        Nesneyi dosya satirina cevirme
        Record(1, "Ali", "0555...") → "1|Ali|0555..."
    
    def from_line(satir):
        Dosya satirini nesneye cevirme
        "1|Ali|0555..." → Record(1, "Ali", "0555...")


STORAGE.PY - DOSYA ISLEMLERI
================================================

load_records():
    • Dosyadan kayitlari oku
    • Her satiri Record nesnesine cevirme
    • Dosya yoksa bos liste don

append_record(kayit):
    • Yeni kayiti dosyaya ekle
    • to_line() ile nesneyi satirina cevirme

save_records(kayitlar):
    • Tum kayitlari dosyaya yeniden yaz
    • Silme+yazma islemi (w mode)


MAIN.PY - MENU VE AKIS
================================================

Secenekler:
1. Listele    → Tum kayitlari goster
2. Ekle       → Yeni kayit ekle
3. Ara        → Kayit ara (ada gore)
4. Sil        → Kayit sil (ID ile)
0. Cikis      → Programdan cik

Akis:
→ load_records() ile dosyadan kayitlar okunur
→ Kullanıcı secim yapar
→ Eger ekle/sil yapilirsa append_record() veya save_records() calisti
→ Yeni kayitlar kayitlar.txt dosyasina yazilir
→ Program kapanirken kayitlar dosyada kaliyor


PROGRAMI CALISTIRMA
================================================

Klasor degistirme (Windows PowerShell):
Set-Location "c:\Users\emirh\OneDrive\Masaüstü\Project AnadoluFrontEnd-1stYearSpringSemester\Web-Based_Application_Development\week_5\src"

Programi calistirma:
python main.py


ISLEM ORNEKLERI
================================================

1. LISTELE:
   Tum 3 kayit ekranda gosterilir

2. EKLE:
   → Ad: Mehmet Yildirim
   → Telefon: 05359876543
   → Kayit eklenir ve kayitlar.txt dosyasina yazilir

3. ARA:
   → Aranacak ad: Ali
   → "Ali Kaya" bulunur ve gosterilir

4. SIL:
   → Silinecek ID: 2
   → Zeynep Demir siliner
   → Dosya yeniden yazilir


ONEMLI KAVRAMLAR
================================================

1. Object Tabani (OOP):
   - Record sinifi
   - Her kayit bir nesne

2. Dosya Donusumu:
   - to_line(): object → string
   - from_line(): string → object

3. Dosya Islemleri:
   - Read (okuma)
   - Append (ekleme)
   - Write (yeniden yazma)

4. List Islemleri:
   - Nesne ekleme
   - Nesne arama
   - Nesne silme

5. UTF-8 Encoding:
   - Turk karakterleri icin


SORUN GIDERMELER
================================================

Problem: Dosya bulunamadi
Cozum: kayitlar.txt ayn klasorde olmali

Problem: Turk karakterleri yanlis gozukuyor
Cozum: encoding="utf-8" kullaniliyor zaten

Problem: ID numaralari karisiyor
Cozum: next_id() fonksiyonu otomatik takip ediyor


KONTROL LISTESI
================================================
[X] 1. models.py icinde Record sinifini yazma
[X] 2. storage.py icinde load/append/save yazma
[X] 3. main.py menuyu kurma
[X] 4. Listele ve ekle ozellikleri test etme
[X] 5. Ara ve sil islevlerini yapma
[ ] 6. Program kapat-ac: veriler dosyada kaliyor mu kontrol etme (Kendin dene!)

================================================
