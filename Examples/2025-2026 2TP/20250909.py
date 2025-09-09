def GetValue(comment="",error="Nieprawidłowa wartość..."):
    ... 
    while True:
        try:
            val = float(input(comment))
            return val
        except:
            print(error)


x = GetValue("Podaj pierwszą liczbę: ")
y = GetValue("Podaj drugą liczbę: ")
  
# print("Wynik dodawania ",x," i ",y," wynosi ",x+y,sep="")
print(f"Wynik dodawania {x} i {y} wynosi {x + y}")
print(f"Wynik odejmowania {x} i {y} wynosi {x - y}")
print(f"Wynik mnożenia {x} i {y} wynosi {x * y}")
if y != 0:
    print(f"Wynik dzielenia {x} i {y} wynosi {x / y}")
    print(f"Wynik dzielenia całkowitego {x} i {y} wynosi {x // y}")
    print(f"Wynik dzielenia modulo {x} i {y} wynosi {x % y}")

try:
    print(f"Wynik potęgowania {x} i {y} wynosi {x ** y}")
except OverflowError:
    print("Przekroczona wartość wyniku")
except:
    print("Inny nieznany błąd")





