# dekoratory

# funkcja nr 1

def fun1(txt:str) -> str:
    return txt.upper()

def fun2(txt:str) -> str:
    return txt.lower()

def fun3(txt:str) -> str:
    return txt.title()

def fun4(txt:str) -> str:
    return txt.capitalize()

tekst = "ala ma kota A KOT MA alĘ"

# print(fun1(tekst))
# print(fun2(tekst))
# print(fun3(tekst))
# print(fun4(tekst))

functions = [fun1,fun2,fun3,fun4]

# for f in functions:
#     print(f(tekst))

# def Wypisz(co,jak):
#     print(jak(co))


# for f in functions:
#     Wypisz(tekst,f)


# def Waluta(nazwa):
#     def fwew(kwota):
#         return f'{kwota} {nazwa}'
#     return fwew

# PLN = Waluta("zł")
# USD = Waluta("$")

# print(PLN(123))
# print(USD(123))


def dekorator(f_dekorowana):
    def fwew():
        print('Ekstra dodatkowe instrukcje przed')
        f_dekorowana()
        print('Ekstra dodatkowe instrukcje po')
    return fwew

# @dekorator
def jakas_funkcja():
    print('Jakas funkcja')


jakas_funkcja()

# nowa = dekorator(jakas_funkcja)

# nowa()