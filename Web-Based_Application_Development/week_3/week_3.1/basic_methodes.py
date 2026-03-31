sayilar = [10, 4, 7]
sayilar.append(12)  # sayilar listesine 12 ekler
sayilar.insert(1, 99)  # sayilar listesine 1. indexe 99 ekler
sayilar.remove(4)  # sayilar listesinden 4'ü kaldırır
son = sayilar.pop()  # sayilar listesinin son elemanını kaldırır ve son değişkenine atar.
sayilar.sort()  # sayilar listesini küçükten büyüğe sıralar
print(sayilar)  # [7, 10, 12, 99]
print("silinen sayı:", son)  # silinen sayı: 12