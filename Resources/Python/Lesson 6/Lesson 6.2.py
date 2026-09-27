# Generowanie danych i list comprehensions

liczby = list(range(10))
kwadraty = [liczba ** 2 for liczba in liczby]
parzyste_kwadraty = [x ** 2 for x in liczby if x % 2 == 0]
slownik = {x: x ** 2 for x in liczby}

print(liczby)
print(kwadraty)
print(parzyste_kwadraty)
print(slownik)
