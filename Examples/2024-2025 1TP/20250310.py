# napisz program który losuje liczbę z zakresu 1 - 1000 a następnie użytkownik
# stara się ją zgadnąć podając swoje propozycje. Program odpowiada użytkownikowi:
# - Za dużo
# - Za mało
# - Dobrze, zgadłeś za x razem

# import random as rnd
# liczba_losowa = rnd.randint(1,1000)
# licznik = 0
# while True:
#     liczba_uzytkownika = int(input("Podaj liczbę: "))
#     licznik += 1
#     if liczba_uzytkownika > liczba_losowa:
#         print("Za dużo")
#     elif liczba_uzytkownika < liczba_losowa:
#         print("Za mało")
#     else:
#         print(f"Dobrze, zgadłeś za {licznik} razem")    
#         break



liczba = int(input("Podaj liczbę: "))
wynik = ""
while True:
    r = liczba % 2
    wynik = str(r) + wynik
    print(r)
    liczba = liczba // 2
    if liczba == 0:
        break

print(wynik)