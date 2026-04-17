import os
print("Current working directory:", os.getcwd())

f = open("gorev.txt", "r", encoding="utf-8")

icerik = f.read()
print(icerik)
f.close()