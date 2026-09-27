# Wlasny modul: ten plik pokazuje funkcje gotowe do importu

def pole_prostokata(a: float, b: float) -> float:
    return a * b


def obwod_prostokata(a: float, b: float) -> float:
    return 2 * (a + b)

if __name__ == "__main__":
    print(pole_prostokata(3, 4))
    print(obwod_prostokata(3, 4))
