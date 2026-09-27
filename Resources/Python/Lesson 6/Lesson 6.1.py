# Indeksowanie, wycinki i rozpakowywanie

wartosci = [1, 4, 2, 3, 5, 6, 7]
print(wartosci[0])
print(wartosci[-1])
print(wartosci[1:5])
print(wartosci[::2])

pierwsza, druga, *reszta, ostatnia = wartosci
print(pierwsza, druga, reszta, ostatnia)
