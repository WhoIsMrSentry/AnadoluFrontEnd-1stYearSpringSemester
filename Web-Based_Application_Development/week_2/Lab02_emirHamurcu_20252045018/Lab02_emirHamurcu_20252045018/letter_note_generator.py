# Görev 2 — Harf notu üretme
# 0 ile 100 arasında not alan bir program yazınız ve aşağıdaki kurala göre harf notu üretiniz:
#  85–100: AA
#  70–84: BB
#  50–69: CC
#  0–49: FF
#  Aralık dışında değer girilmişse hata mesajı

puan = int(input("Notunuzu giriniz: "))
if puan >= 0 and puan <= 100:
    if puan >= 85:
        print("Harf Notunuz: AA")
    elif puan >= 70:
        print("Harf Notunuz: BB")
    elif puan >= 50:
        print("Harf Notunuz: CC")
    else:
        print("Harf Notunuz: FF")