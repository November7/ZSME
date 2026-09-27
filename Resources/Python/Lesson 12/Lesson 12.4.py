a = 1
b = 0
try:
    # Kod, który powoduje błąd dzielenia przez zero
    x = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
