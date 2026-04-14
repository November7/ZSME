def SilniaI(n):
    w = 1
    for i in range(1, n + 1): 
        w *= i
    return w

def SilniaR(n):
    if n == 0:
        return 1    
    return n * SilniaR(n - 1)



ile = 1000
print(f'Silnia z kolejnych liczb od <0, {ile}')
for i in range(ile):
    print(f'{i}! = {SilniaR(i)}')