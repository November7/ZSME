import math
sito = []

n = 1000
sito = [i for i in range(n)]
i = 0
sito[0] = 0 #0 nie jest liczbą pierwszą
sito[1] = 0 #1 nie jest liczbą pierwszą
while i <= math.sqrt(n):
    p = sito[i]
    if p != 0:
        for j in range(2 * p, n, p):
            sito[j] = 0

    i+=1

wynik = [i for i in sito if i > 0]
print(wynik)