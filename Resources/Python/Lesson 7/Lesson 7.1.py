# Definiowanie funkcji i wartosc zwracana

def powitanie(imie: str = "Uczniu") -> str:
    return f"Witaj, {imie}!"


def suma(a: int, b: int) -> int:
    return a + b

print(powitanie())
print(powitanie("Jan"))
print(suma(3, 4))
