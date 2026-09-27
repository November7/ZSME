Lista = [1, 2, 3, 1, 3, 2, -1] #definicja listy
print(Lista)
Lista.append(333) #dodanie wartości 333 na koniec listy
print(Lista)
Lista.insert(0, 222) #wstawienie wartości 222 na początek listy (index o wartości 0)
print(Lista)
Lista.remove(1) #usunięcie pierwszego wystąpienia elementu o wartości 1
print(Lista)
Lista.pop(2) #usunięcie elementu o indeksie 2
print(Lista)
Lista.sort() #uporządkowoanie listy rosnąco
print(Lista)
Lista.sort(reverse=True) #uporządkowoanie listy malejąco
print(Lista)
Lista.reverse() #odwrócenie kolejności elementów
print(Lista)
print(Lista.count(2)) #zliczenie elementów o wartości 2
Lista.clear() #usunięcie wszystkich elementów
print(Lista)
