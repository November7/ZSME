# Obsluga wyjatkow

try:
    licznik = int(input("Podaj licznik: "))
    mianownik = int(input("Podaj mianownik: "))
    wynik = licznik / mianownik
except ValueError:
    print("Wprowadzono nieprawidlowa liczbe.")
except ZeroDivisionError:
    print("Nie mozna dzielic przez zero.")
else:
    print("Wynik:", wynik)
finally:
    print("Koniec operacji.")
