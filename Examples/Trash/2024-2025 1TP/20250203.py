# lista = [] #pusta lista
lista = [3,4,6,3,23,4,6,7,5,3,35]

print(lista)

for element in lista:
    print(element,end=', ')
print()

i = 0
n = len(lista)
while i < n:
    print(lista[i],end=', ')
    i += 1

print()

lista.append(-123)
print(lista)

lista.insert(0,123)
print(lista)

print(lista.pop(0))
print(lista)

lista.remove(3)
print(lista)

print(f"Rozmiar listy: {len(lista)}")

print(lista[3])

lista[3] = "fdsfdssdf"

print(lista)


krotka = (3,4,67,3,3,5,7,3,2,4)
print(krotka)


for element in krotka:
    print(element,end=', ')
print()

i = 0
n = len(krotka)
while i < n:
    print(krotka[i],end=', ')
    i += 1

print()

print(krotka[4])
print(krotka[-4])


########################################

oceny = []

while True:
    ocena = int(input("Podaj ocenę z zakresu <1,6>: "))
    if ocena == 0:
        break
    elif ocena < 0 or ocena > 6:
        print("Nieprawidłowa ocena!")
    else:
        oceny.append(ocena)

print(oceny)
ilosc = len(oceny)
suma = 0
for el in oceny:
    suma += el

print(f"Średnia ocen wynosi {suma / ilosc}")