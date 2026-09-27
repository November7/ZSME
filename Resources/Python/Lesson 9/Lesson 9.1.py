# Slownik i bezpieczny dostep do danych

uczen = {"imie": "Jan", "klasa": "3A", "oceny": [5, 4, 5]}

for klucz, wartosc in uczen.items():
    print(klucz, wartosc)

print(uczen.get("email", "Brak adresu email"))
uczen.setdefault("email", "jan@example.com")
print(uczen)
