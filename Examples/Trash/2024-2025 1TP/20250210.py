#Algorytm NWD v1 (algorytm Euklidesa)

liczba_a = a = int(input("Podaj 1 liczbę: "))
liczba_b = b = int(input("Podaj 2 liczbę: "))

while a != b:
    print(a,b)

    if a > b:
        a = a - b
    else:
        b = b - a

print(f"Największy wspólny dzielnik liczb {liczba_a} i {liczba_b}, wynosi {a}")


#Algorytm NWD v2 

liczba_a = a = int(input("Podaj 1 liczbę: "))
liczba_b = b = int(input("Podaj 2 liczbę: "))

while b != 0:
    # print(a,b)
    r = a % b
    a = b
    b = r

print(f"Największy wspólny dzielnik liczb {liczba_a} i {liczba_b}, wynosi {a}")


#Algorytm NWW

NWW = liczba_a*liczba_b // a

print(f"Najmniejsza wspólna wielokrotność wynosi {NWW}")




