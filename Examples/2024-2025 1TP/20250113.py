#Pętla while

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while True:    
#     print("Podaj wartość od 1 - 10")
#     liczba = int(input())
#     if liczba >= 1 and liczba <= 10:
#         break

# print(f"Twoja liczba to {liczba}")

#Pętla for in

# tekst = "jakiś randomowy tekst"

# for literka in tekst:
#     print(literka)


# for i in range(10,-10,-2): # <-10, 10)
#     print(i)


# Zgadywanie liczby

niewiadoma = 123
ile = 1

while True:
    odp = int(input("Podaj liczbę z zakresu 1 - 1000: "))
    if odp == niewiadoma:
        print(f"Brawo, zgadłeś za {ile} razem!")
    else:
        if odp > niewiadoma:
            print("Szukana liczba jest mniejsza")
        else:
            print("Szukana liczba jest większa")

    ile += 1

