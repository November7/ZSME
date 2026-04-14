#1
# import random

#2
import random as rnd
import mojabiblioteka as mb

#3
# from random import random, randint

#4
# from random import *

# print(rnd.randint(0,100))

# mb.randint()


# Program wypisujący dwie losowe liczby z zakresu <1,1000> 
# i obliczający ich NWD

import random

min = 1
max = 1000
a = orgA = random.randint(min, max)
b = orgB = random.randint(min, max)

# algorytm Euklidesa
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(f"NWD liczb {orgA} i {orgB} wynosi {a}")

# Program sprawdzający czy podana liczba jest pierwsz czy złożona:

import math

liczba = int(input("Podaj liczbę większą niż jeden: "))
if liczba < 2: 
    print("Podana liczba nie jest prawidłowa")
else:
    i = 2
    pierwsza = True
    sq = math.sqrt(liczba)

    while i <= sq:
        if liczba % i == 0:        
            pierwsza = False
            break
        i += 1

    if pierwsza == 1:
        print("Liczba pierwsza")
    else:
        print("Liczba jest złożona")




