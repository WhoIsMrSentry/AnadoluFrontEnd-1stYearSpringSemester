# Kullanıcıdan yaş bilgisi alınız ve aşağıdaki kurala göre sonucu yazdırınız:
#  0–12: Çocuk
#  13–17: Ergen
#  18–64: Yetişkin
#  65 ve üzeri: Yaşlı

yas = int(input("Yaşınızı giriniz: "))
if yas >= 0 and yas <= 12:
    print("Çocuk")
elif yas >= 13 and yas <= 17:
    print("Ergen")
elif yas >= 18 and yas <= 64:
    print("Yetişkin")
else:
    print("Yaşlı")        
        