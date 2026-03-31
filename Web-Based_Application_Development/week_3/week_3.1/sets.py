sehirler = {"İstanbul", "Ankara", "İzmir", "Bursa", "Adana", "Ankara"}

print(sehirler)  # {'Bursa', 'Adana', 'İzmir', 'Ankara', 'İstanbul'}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)  # {3, 4} - kesişim
print(a | b)  # {1, 2, 3, 4, 5, 6} - birleşim
print(a - b)  # {1, 2} - fark