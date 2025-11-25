# Funbkcja jako argument innej funkcji

#przykładowe funkcja na tekście:

#funkcja zwraca tekst wielkimi literami
def fun1(txt:str) -> str: 
    return txt.upper()

#funkcja zwraca tekst małymi literami
def fun2(txt:str) -> str: 
    return txt.lower()

#funkcja zwraca tekst z wielką literą na początku każdego wyrazu
def fun3(txt:str) -> str: 
    return txt.title()

#funkcja zwraca tekst z wielką literą na początku pierwszego wyrazu
def fun4(txt:str) -> str: 
    return txt.capitalize()

tekst = "lorem ipsum DOLOR sit amet"

# testowanie funkcji

print(fun1(tekst))
print(fun2(tekst))
print(fun3(tekst))
print(fun4(tekst))

# Przygotowane funkcji przyjmującej inną funkcję jako argument

# co - tekst do przetworzenia
# jak - funkcja przetwarzająca tekst
def Wypisz(co,jak):
    print(jak(co))

# testowanie funkcji Wypisz z różnymi funkcjami
Wypisz(tekst,fun1)
Wypisz(tekst,fun2)
Wypisz(tekst,fun3)
Wypisz(tekst,fun4)

