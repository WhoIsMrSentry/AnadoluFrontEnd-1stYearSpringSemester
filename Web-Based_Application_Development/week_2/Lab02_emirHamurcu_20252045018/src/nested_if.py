yas = int(input("Lütfen yaşınızı giriniz: "))
kimlik_varmi_mi = input("Kimlik var mı? (evet/hayır): ")

if yas >= 18:
    if kimlik_varmi_mi.lower() == "evet":
        print("Sürücü olabilir.")
    else:
        print("Sürücü olamaz, kimlik gereklidir.")
else:
    print("Sürücü olamaz, yaşınız 18'den küçük.")        
        