================================================
HAFTA 4 - DOSYA İŞLEMLERİ
================================================

PROJE AÇIKLAMASI
================================================
Bu proje Python kullanarak görev yönetim sistemi oluşturmaktadır.

DOSYA YAPISI
================================================
main.py          → Menü ve kullanıcı akışı
helpers.py       → Dosya okuma/yazma yardımcı fonksiyonları
gorevler.txt     → Görevlerin saklandığı veri dosyası
README.txt       → Bu dosya


MAIN.PY - MENÜ VE KULLANICI AKIŞI
================================================
Ana program menüyü sürekli çalıştırır (while True).

Menü Seçenekleri:
1. Listele    → Tüm görevleri göster
2. Ekle       → Yeni görev ekle
3. Ara        → Görev ara
4. Sil        → Görev sil
0. Çıkış      → Programdan çık


HELPERS.PY - DOSYA İŞLEMLERİ
================================================

1. gorevleri_oku()
   - Dosyadan tüm görevleri okur
   - Her satırı temizler (strip)
   - Boş satırları atlar
   - Dosya yoksa [] döner

2. gorev_ekle(kayit)
   - Yeni kayıt ekler
   - Append (a) modunda dosya sonuna yazar
   - Hata durumunda kullanıcıyı bilgilendir

3. gorev_sil(indeks)
   - Tüm satırları oku
   - Silinecek satırı çıkar
   - Tüm dosyayı yaz (w) modunda yeniden yaz

4. gorev_ara(anahtar)
   - Anahtar kelimeyi içeren görevleri bul
   - Büyük/küçük harf farkı gözetmez

5. int_input(prompt)
   - Kullanıcıdan sayı girer
   - Hata kontrollü (try/except)


GOREVLER.TXT - VERİ DOSYASI
================================================
Her satır bir görev içerir.
Format: "görev açıklaması" (opsiyonel: | tarih)

Örnek:
1 | Lab raporu | 2026-04-22
2 | Proje sunumu | 2026-04-23
3 | Kod incelemesi | 2026-04-24


PROGRAMI ÇALIŞTIRMA
================================================
python main.py

Veya IDE'den run butonu ile çalıştırabilirsiniz.


HATA YÖNETIMI
================================================
- Dosya bulunamadığında: Boş liste döner, program çalışmaya devam eder
- Satır okuma hatası: Exception yakalanır, mesaj yazılır
- Geçersiz kullanıcı girişi: Uyarı yazılır, tekrar dene
- Geçersiz menü seçimi: Geçersiz seçim uyarısı, menüye geri dön


KULLANILACAK PYTHON ÖZELLİKLERİ
================================================
- File I/O (Dosya okuma/yazma)
- String işlemleri (strip, lower, in)
- List kavramı ve işlemleri
- Try/Except (Hata yönetimi)
- While döngüsü
- Encoding (UTF-8)


NOTLAR
================================================
- Türkçe karakterleri düzgün göstermek için UTF-8 encoding kullanılır
- Dosya yoksa otomatik oluşturulur (a mode ile)
- Boş satırlar otomatik temizlenir
================================================
