# funkcja do pobierania liczb

def getInt(prompt:str = '', errorMsg:str =' Value error', tries:int =3) -> int:
    """Pobiera liczbę całkowitą od użytkownika.    
    prompt - komunikat wyświetlany użytkownikowi
    errorMsg - komunikat wyświetlany w przypadku błędu
    tries - liczba prób podania poprawnej wartości
    """
    while tries > 0:
        try:
            userInput = int(input(prompt))
            return userInput
        except ValueError:
            print(errorMsg)
            tries -= 1
    raise ValueError('Exceeded number of tries')

# zapis do pliku

n = getInt('Ile liczb chcesz zapisać do pliku? ', 'To nie jest liczba całkowita!', 2)
with open('data.txt', 'w') as file:
    for i in range(n):
        file.write(f'{i}\n')