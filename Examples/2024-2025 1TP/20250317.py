import random
dane = []
# dane = [random.randint(0,100) for _ in range(10)]

for _ in range(10):
    dane.append(random.randint(0,100))

n = len(dane)

print(dane)

for j in range(n - 1):
    flaga = 0
    for i in range(n - 1 - j):
        if dane[i] > dane[i + 1]:
            # dane[i], dane[i + 1] = dane[i + 1], dane[i]
            flaga = 1
            tmp = dane[i]
            dane[i] = dane[i + 1]
            dane[i + 1] = tmp
    if flaga == 0:
        break

print(dane)
