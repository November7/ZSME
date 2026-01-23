def Suma(dane):
    w = 0
    for el in dane:
        w += el
    return w

def Srednia(dane):
    s = Suma(dane)
    n = len(dane)
    if n > 0: return s/n
    else: return None

def Odchylenie(dane):
    n = len(dane)
    if n == 0: return None
    s = Srednia(dane)
    w = 0
    for el in dane:
        w += (el - s)**2
    
    return (w / n) ** 0.5

def Mediana(dane):
    n = len(dane)
    if n == 0: return None
    kopia = dane
    kopia.sort()
    sr = n // 2
    if n % 2 == 1:
        return kopia[sr]
    else:

        w1 = kopia[sr - 1]
        w2 = kopia[sr]
        return (w1 + w2) / 2

def Min(dane):
    m = dane[0]
    for el in dane:
        if el < m:
            m = el
    return m

def Max(dane):
    m = dane[0]
    for el in dane:
        if el > m:
            m = el
    return m



def Dominanta(dane):
    slownik = {}
    for el in dane:
        if el in slownik:
            slownik[el] += 1
        else:
            slownik[el] = 1
    ldict = [(slownik[k],k) for k in slownik]
    
    ldict.sort(reverse=True)
    max = ldict[0][0]
    ret = [el[1] for el in ldict if el[0] == max]    
    return ret

import random

n = int(input("Podaj ilość danych: "))

# temperatura  = []
# for _ in range(n):
#     temperatura.append(random.randint(-30, 40))

temperatura = [random.randint(-30, 40) for _ in range(n)]

print(temperatura)
print(f'Suma danych: {Suma(temperatura)}')
print(f'Średnia danych: {Srednia(temperatura)}')
print(f'Odchylenie standardowe danych: {Odchylenie(temperatura)}')
print(f'Mediana danych: {Mediana(temperatura)}')
print(f'Dominanta danych: {Dominanta(temperatura)}')