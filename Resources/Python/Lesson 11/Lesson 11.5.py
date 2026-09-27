# Rekurencja i funkcje jako obiekty

def silnia(n: int) -> int:
    if n <= 1:
        return 1
    return n * silnia(n - 1)


def zastosuj(funkcja, wartosc: int) -> int:
    return funkcja(wartosc)

print(silnia(5))
print(zastosuj(silnia, 4))
