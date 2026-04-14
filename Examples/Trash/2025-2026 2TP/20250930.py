import random


def suma(arg:list) -> int:
    s = 0
    for el in arg:
        s = s + el # s += el
    return s

def min(arg:list) -> int:
    if len(arg) == 0:
        return None
    
    minimum = arg[0]
    for el in arg:
        if el < minimum:
            minimum = el
    return minimum

def max(arg:list) -> int:
    if len(arg) == 0:
        return None
    
    maximum = arg[0]
    for el in arg:
        if el > maximum:
            maximum = el
    return maximum

def mean(arg:list) -> int:    
    if len(arg) == 0:
        return None
    
    n = len(arg)
    return suma(arg) / n

def bubbleSort(arg):
    n = len(arg) - 1
    while True:
        sorted = True
        for i in range(n):
            if arg[i] > arg[i+1]:
                tmp = arg[i]
                arg[i] = arg[i+1]
                arg[i+1] = tmp
                sorted = False
            # arg[i], arg[i+1] = arg[i+1], arg[i]
        if sorted == True:
            break
        n = n - 1


dane = [random.randint(-100,100) for _ in range(20)]

print(dane)
print("Sum: ", suma(dane))
print("Min: ", min(dane))
print("Max: ", max(dane))
print("Avg: ", mean(dane))
bubbleSort(dane)

print(dane)

    


