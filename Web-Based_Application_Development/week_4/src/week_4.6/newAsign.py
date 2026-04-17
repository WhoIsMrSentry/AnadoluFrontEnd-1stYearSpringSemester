yeni_kayit = "Bu bir deneme yazısıdır.\nBu yazı gorevler.txt dosyasına yazılacaktır.\n" 

with open("gorevler.txt","a", encoding="utf-8") as f:
    f.write(yeni_kayit)
