def Hello(imie="", nazwisko=""): #definicja funkcji
    ...
    print(f"Hello {imie} {nazwisko}") #wyświetlenie napisu


Hello() #wywołanie funkcji bez argumentów (argumenty są domyślne)
Hello("Marcin") #wywołanie funkcji
Hello("Marcin", "Kowalski") #wywołanie funkcji z arguentami pozycyjnymi
Hello(nazwisko="Kowalski", imie="Marcin") #wywołanie funkcji z argumentami kluczowymi (key-arguments)
Hello("Marcin", nazwisko="Kowalski") #wywołanie funkcji z argumentami pozycyjnymi i kluczowymi

# Hello(imie="Marcin", "Kowalski") #wywołanie funkcji z argumentem kluczowym - błąd
# Hello("Marcin", imie="Marek") #wywołanie funkcji z argumentami pozycyjnymi i kluczowymi - błąd

def Witaj(imie:str = "", nazwisko:str = "") -> None: #definicja funkcji
    ...
    print(f"Witaj {imie} {nazwisko}") #wyświetlenie napisu
    

#Ćwiczenie

def Dodawanie(a, b):
    return a+b

def Odejmowanie(a, b):
    return a-b

def Mnozenie(a, b):
    return a * b

def Dzielenie(a:float, b:float): #definicja funkcji
    if a > 0 and b == 0:
        return "Infinity"
    elif a < 0 and b == 0:
        return "-Infinity"
    elif a == 0 and b == 0:
        return "NaN"
    return a/b #zwrócenie wyniku dzielenia

def NWD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

liczba_a = int(input("Podaj pierwszą liczbę: "))
liczba_b = int(input("Podaj pierwszą liczbę: "))

print(f"Wynik dodawania {liczba_a} i {liczba_b} wynosi {Dodawanie(liczba_a, liczba_b)}")
print(f"Wynik odejmowania {liczba_a} i {liczba_b} wynosi {Odejmowanie(liczba_a, liczba_b)}")
print(f"Wynik mnożenia {liczba_a} i {liczba_b} wynosi {Mnozenie(liczba_a, liczba_b)}")
print(f"Wynik dzielenia {liczba_a} i {liczba_b} wynosi {Dzielenie(liczba_a, liczba_b)}")
print(f"Największy wspólny dzielnik {liczba_a} i {liczba_b} wynosi {NWD(liczba_a, liczba_b)}")

