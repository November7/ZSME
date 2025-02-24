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
    
def Dzielenie(a:float, b:float): #definicja funkcji
    if a > 0 and b == 0:
        return "Infinity"
    elif a < 0 and b == 0:
        return "-Infinity"
    elif a == 0 and b == 0:
        return "NaN"
    return a/b #zwrócenie wyniku dzielenia


print(Dzielenie(3,0))
print(Dzielenie(-13,0))
print(Dzielenie(0,0))
print(Dzielenie(20,10))