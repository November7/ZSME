# Definiowanie funkcji w python

# Przykładowa funkcja (która nic nie robi)
def DoNothing():
    ...

# Wywołanie funkcji
DoNothing()

# Funkcja z parametrem
# Wpython możliwe jest określenie typu parametru
# oraz typu zwracanego przez funkcję
# taka operacja nazywa się "type hinting"
# (w rzeczywistości Python i tak nie wymusza typów)

def PrintText(text: str) -> None:
    print(text)

# Wywołanie funkcji z parametrem
PrintText("Hello World!")


# Funkcja z parametrem domyślnym
def PrintTextWithPrefix(text: str, prefix: str = "Info: ") -> None:
    print(prefix + text)

# Wywołania funkcji z i bez parametru domyślnego
PrintTextWithPrefix("Hello World!")

# Wywołanie z nadpisaniem parametru domyślnego
PrintTextWithPrefix("Hello World!", "Warning: ")

# Funkcja zwracająca wartość
def Add(a: int, b: int) -> int:
    return a + b

# Wywołanie funkcji i przypisanie wyniku do zmiennej
result = Add(5, 3)
print(result)

# Wywołanie funkcji bez przypisywania wyniku do zmiennej
print(Add(10, 20))

