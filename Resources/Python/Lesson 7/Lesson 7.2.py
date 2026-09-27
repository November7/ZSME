# Argumenty pozycyjne, nazwane i zmienna liczba argumentow

def raport(tytul: str, *wartosci: float, autor: str = "brak") -> None:
    print(tytul)
    print("Suma:", sum(wartosci))
    print("Autor:", autor)

raport("Oceny", 5, 4.5, 3, autor="Jan")
