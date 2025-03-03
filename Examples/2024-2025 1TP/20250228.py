import random as rnd

def Min(arg, size):
    min_w = arg[0]

    for i in range(1,size): #zakres od 1 do ile-1
        if arg[i] < min_w:
            min_w = arg[i] 
    return min_w

def Max(arg, size):
    max_w = arg[0]

    for i in range(1,size): #zakres od 1 do ile-1
        if arg[i] > max_w:
            max_w = arg[i] 
    return max_w


ile = int(input("Podaj ilosć danych: "))
dane = [] #pusta lista
start = 0
end = 100

for _ in range(ile): #zakres od 0 do ile-1 <0,ile)
    dane.append(rnd.randint(start,end))  #<start,end>


print(dane)

min = Min(dane,ile)
max = Max(dane,ile)
print(f"{min = }, {max = }")




