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


# # Zgadywanie liczby
# import random
# niewiadoma = random.randint(1,1000)

# # niewiadoma = 123
# ile = 1

# while True:
#     odp = int(input("Podaj liczbę z zakresu 1 - 1000: "))
#     if odp == niewiadoma:
#         print(f"Brawo, zgadłeś za {ile} razem!")
#     else:
#         if odp > niewiadoma:
#             print("Szukana liczba jest mniejsza")
#         else:
#             print("Szukana liczba jest większa")

#     ile += 1


size = 17

# for y in range(size):
#     for x in range(size):
#         print("*",end="")
#     print()

# # Litera L
# for y in range(size):
#     for x in range(size):
#         if x == 0 or y == size-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Litera H
for y in range(size):
    for x in range(size):
        if x == 0 or y == size//2 or x == size - 1:
            print("*",end="")
        else:
            print(" ",end="")
    print()