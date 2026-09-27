# Instrukcja warunkowa

liczba = int(input("Podaj liczbe: "))

if liczba < 0:
    print("Liczba ujemna")
elif liczba > 0:
    print("Liczba dodatnia")
else:
    print("Zero")

print("Parzysta" if liczba % 2 == 0 else "Nieparzysta")
