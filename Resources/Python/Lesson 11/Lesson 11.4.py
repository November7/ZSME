# dekorator obliczający czas wywołania funkcji

import time
def mierzenie_czasu(f_dekorowana):
    def fwew(*args, **kwargs):
        start = time.time()  # czas rozpoczęcia
        wynik = f_dekorowana(*args, **kwargs)
        end = time.time()    # czas zakończenia
        print(f'Czas wykonania funkcji {f_dekorowana.__name__}: {end - start:.6f} sekund')
        return wynik
    return fwew

# przykładowa funkcja do dekorowania
@mierzenie_czasu
def oblicz_sume(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma

# testowanie dekorowanej funkcji
wynik = oblicz_sume(1000000)

print(f'Wynik: {wynik}')