lista = [1, 2, 3, 4, 5, 6, 7]

#a,b,c = lista # błąd

a, b, *reszta = lista

print(a, b, reszta, sep="\n")
