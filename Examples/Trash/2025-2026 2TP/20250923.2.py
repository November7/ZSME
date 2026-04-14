import random
n = int(input('Podaj ilość danych: '))
if n <= 0:
    exit()
dane = []
for i in range(n): # range(k) <0,k), range(p,k) <p,k), range(p,k,s) <p,k)
    dane.append(random.randint(0,100))
# dane = [random.randint(0,100) for i in range(n)]

print(dane)
suma = 0
for el in dane:
    suma += el

print(f'{suma = }')

mean = suma / n

print(f'{mean = }')

min = dane[0]
max = dane[0]

for el in dane[1::]:
    if el < min:
        min = el
    if el > max:
        max = el
print(f'{min = }')
print(f'{max = }')

