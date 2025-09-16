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

while True:
    print(' ----- Menu ------ ')
    print(' 0. Wyjście (spacja)')
    print(' 1. Dodawanie (+)')
    print(' 2. Odejmowanie (-)')
    print(' 3. Dodawanie (+)')
    print(' 4. Wprowadzenie wartości zmiennych (@)')

    operation = input("Podaj działanie [space == exit]: ")

    if operation == '+' or operation == '1':
        print(f"Wynik dodawania {x} i {y} wynosi {x + y}")
    elif operation == '-' or operation == '2':
        print(f"Wynik odejmowania {x} i {y} wynosi {x - y}")
    elif operation == '@' or operation == '4':
        x = GetValue("Podaj pierwszą liczbę: ")
        y = GetValue("Podaj drugą liczbę: ")
        ...
        # kolejne opcje
    elif operation == " " or operation == '0':
        break
    else:
        print("Nieprawidłowa opcja")


    
    # # print("Wynik dodawania ",x," i ",y," wynosi ",x+y,sep="")
    # print(f"Wynik mnożenia {x} i {y} wynosi {x * y}")
    # if y != 0:
    #     print(f"Wynik dzielenia {x} i {y} wynosi {x / y}")
    #     print(f"Wynik dzielenia całkowitego {x} i {y} wynosi {x // y}")
    #     print(f"Wynik dzielenia modulo {x} i {y} wynosi {x % y}")

    # try:
    #     print(f"Wynik potęgowania {x} i {y} wynosi {x ** y}")
    # except OverflowError:
    #     print("Przekroczona wartość wyniku")
    # except:
    #     print("Inny nieznany błąd")





