lista = ["samolot", 100, 33.1]
zestaw = {"okręt", 101, 33.2}
krotka = ("autobus", 102, 33.3)
slownik = {"typ": "samochód", "marka": "Tesla"}
 
l1, l2, l3 = lista
z1, z2, z3 = zestaw
k1, k2, k3 = krotka
s1, s2 = slownik
 
print(lista)
print(l1, l2, l3)
#l1, l2 = lista # błąd - lista posiada więcej elementów i nie da się ich rozpakować do dówch zmiennych!
 
print(zestaw)
print(z1, z2, z3)
 
print(krotka)
print(k1, k2, k3)
 
print(slownik)
print(s1, s2)
print(slownik[s1], slownik[s2])
