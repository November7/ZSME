a = "1"
b = 0
try:
    x = a / b 
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except TypeError:
    print("Nieprawidłowy typ danych!")
