# Projekt laczacy funkcje, kolekcje i pliki

from pathlib import Path
from collections.abc import Sequence


def srednia(oceny: Sequence[int | float]) -> float:
    return sum(oceny) / len(oceny)


uczniowie = {
    "Anna": [5, 4, 5],
    "Jan": [3, 4, 4],
}

for imie, oceny in uczniowie.items():
    print(imie, srednia(oceny))

Path("wyniki.txt").write_text("Projekt zakonczony\n", encoding="utf-8")
