def BubbleSort(data,length):
    licznik = 0
    for i in range(length - 1):
        flaga = 0
        for j in range(length - i - 1):
            licznik += 1
            if data[j] > data[j + 1]:
                # data[j], data[j + 1] = data[j + 1], data[j]
                flaga = 1
                tmp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = tmp
        if flaga == 0:
            break
    return licznik

def SelectionSort(data,length):
    licznik = 0
    for i in range (length):
        min = i
        for j in range(i + 1,length):
            licznik += 1
            if data[j] < data[min]:
                min = j
        tmp = data[j]
        data[j] = data[min]
        data[min] = tmp
        # data[j], data[min] = data[min], data[j]

    return licznik
    

def InsertionSort(data,length):
    licznik = 0
    for i in range(1,length):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            licznik += 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = tmp
    return licznik


import random
dane = []

n = int(input("Podaj ilość danych: "))

for _ in range(n):
    dane.append(random.randint(0,100))

print(dane)

# SelAlgorithm = BubbleSort
# SelAlgorithm = SelectionSort
SelAlgorithm = InsertionSort

print(f"Sortowanie zakończone po {SelAlgorithm(dane,n)} iteracjach")


print(dane)