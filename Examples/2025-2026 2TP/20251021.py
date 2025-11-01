import random

def Generate(count:int) -> list:
    # 1
    # d = []
    # for _ in range(count):
    #     d.append(random.randint(-100,100))

    # 2
    # d = [random.randint(-100,100) for _ in range(count)]
    # return d

    # 3
    return [random.randint(-100,100) for _ in range(count)]

def Sum(data:list) -> int:
    s = 0
    for el in data:
        s += el
    return s

def Mean(data:list) -> int: #Avg
    n = len(data)
    if n == 0:
        return None
    else: 
        return Sum(data) / n

def Min(data:list) -> int:
    m = data[0]
    for el in data:
        if el < m:
            m = el
    return m

def Max(data:list) -> int:
    m = data[0]
    for el in data:
        if el > m:
            m = el
    return m

def Mode(data:list) -> list: #dominanta # 1, 1, 2, 2, 3, 4, -> [1, 2]
    ...

def Med(data:list) -> int|float:
    data.sort()
    n = len(data)
    if  n%2 == 1:
        return data[n//2]
    else:
        return (data[n//2-1] + data[n//2])/2

dane = [1,2,5,1] #1, 1, 2, 5

# dane = Generate(10)

print(f'{dane = }')
print(f'{Sum(dane) = }')
print(f'{Mean(dane) = }')
print(f'{Min(dane) = }')
print(f'{Max(dane) = }')
print(f'{Med(dane) = }')
print(f'{Mode(dane) = }')