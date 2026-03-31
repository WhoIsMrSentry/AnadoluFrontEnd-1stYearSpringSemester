sayilar = [1, 2, 3, 4, 5]

kareler = list(map(lambda x: x * x, sayilar))
print(kareler)

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(ciftler)