# Proste testowanie funkcji za pomoca assert

def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0

assert czy_parzysta(2)
assert not czy_parzysta(3)
print("Testy zakonczone powodzeniem")
