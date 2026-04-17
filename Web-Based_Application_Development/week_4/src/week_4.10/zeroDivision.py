try:
    print("Try başladı")
    x = 10 / 0  # Bu satır ZeroDivisionError hatası oluşturacak
except ZeroDivisionError as e:
    print("Hata yakalandı:", e)
finally:
    print("Finally bloğu çalıştı")  