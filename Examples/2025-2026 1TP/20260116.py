# Tworzenie własnych funkcji

#definicja funkcji:
def suma(a, b): #zwraca wynik
    return a + b

def roznica(a, b): #zwraca wynik
    return a - b

def iloczyn(a, b): #zwraca wynik
    return a * b

def iloraz(a, b): #zwraca wynik
    if b != 0:
        return a / b
    else:
        if a > 0:
            return '+Inf'
        elif a < 0:
            return '-Inf'
        else:
            return None


def srednia(dane: list) -> float | None:
    n = len(dane)
    if n == 0: return None

    s = 0
    for el in dane:
        s += el

    return s / n
 
def potega(a, b): #zwraca wynik
    w = 1
    for _ in range(b):
        w *= a
    return w

def silnia(a):
    w = 1
    for i in range(1, a + 1):
        w *= i
    return w

x = 2
y = 10
dane = [3,4,56,3,32,4,5,6]

print(f'Wynik dodawania {x} i {y} wynosi {suma(x, y)}')
print(f'Wynik odejmowania {x} i {y} wynosi {roznica(x, y)}')
print(f'Wynik mnożenia {x} i {y} wynosi {iloczyn(x, y)}')
print(f'Wynik dzielenia {x} i {y} wynosi {iloraz(x, y)}')
print(f'Wynik potęgowania {x} do {y} wynosi {potega(x, y)}')
print(f'Srednia danych {dane}  wynosi {srednia(dane)}')

for i in range(41):
    print(f'{i}! = {silnia(i)}')