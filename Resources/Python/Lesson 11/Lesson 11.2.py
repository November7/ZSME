# Przykład funkcji zwracającej funkcję

# funkcja tworząca funkcję dodającą nazwę waluty do kwoty
def Waluta(nazwa):
    # funkcja wewnętrzna dodająca nazwę waluty
    def fwew(kwota):
        return f'{kwota} {nazwa}'
    return fwew # zwraca funkcję wewnętrzną

PLN = Waluta("zł") # tworzy funkcję dodającą "zł"
USD = Waluta("$") # tworzy funkcję dodającą "$"

# testowanie funkcji zwracających funkcje
print(PLN(123))
print(USD(123))