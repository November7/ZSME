import random as rnd

def Wieksza():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    if a>b: 
        print(f"Liczba {a} jest większa")
    elif b>a:
        print(f"Liczba {b} jest większa")
    else:
        print(f"Liczby są takie same")



def Los():
    # lista = [rnd.randint(0,100) for _ in range(10)]
    lista = []

    for i in range(0,10):        
        lista.append(rnd.randint(0,100))
    print(lista)
    


if __name__ == "__main__":

    Wieksza()
    Los()