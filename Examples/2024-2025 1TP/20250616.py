# potęgowanie iteracyjne

def PotegaI(x:int, n:int) -> int:
    wynik = 1
    for _ in range(n):
        wynik = wynik * x
    return wynik

def PotegaR(x:int, n:int) -> int:

    if n == 0:
        return 1
    else:
        return x * PotegaR(x, n - 1)    
        

print("Potęgi liczby 2:")
for i in range(41):
    print(f"2 ^ {i} = {PotegaR(2,i)}")

def SilniaI(n: int) -> int:
    if n<0: return None
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
    return wynik

def SilniaR(n: int) -> int:
    if n<0: return None
    if n == 0: return 1
    else: return n * SilniaR(n - 1)

print("Silnie liczb naturalnych")
for i in range(41):
    print(f"Silnia({i}) = {SilniaR(i)}")

## Ciąg Fibbonaciego??


def FibR(n:int) -> int:
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return FibR(n - 1) + FibR(n - 2)

def FibI(n:int) -> int:
    if n == 0: return 0
    elif n == 1: return 1
    else:
        f0 = 0
        f1 = 1
        wynik = 0
        for _ in range(n - 1):
            wynik = f0 + f1
            f0 = f1
            f1 = wynik
        return wynik

print("Wyrazy ciągu Fibonacciego")
for i in range(41):
    print(f"Fib({i}) = {FibI(i)}")


