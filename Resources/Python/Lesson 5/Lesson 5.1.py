# Listy i ich podstawowe metody

lista = [1, 2, 3, 1]
lista.append(4)
lista.insert(0, 0)
lista.remove(1)
ostatni = lista.pop()
lista.sort(reverse=True)

print(lista)
print("Usuniety element:", ostatni)
print("Liczba dwojek:", lista.count(2))
