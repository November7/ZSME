# Funkcje generujace i wyrazenia generatorowe

def liczby_do(limitu: int):
    for liczba in range(limitu):
        yield liczba

suma = sum(liczba * liczba for liczba in liczby_do(5))
print(suma)
