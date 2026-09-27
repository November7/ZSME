import pandas as pd
 
# Tworzenie obiektu DataFrame ze słownika zawierającego listy
data = {'Imię': ['Anna', 'Jan', 'Piotr', 'Maria'],
        'Wiek': [28, 34, 29, 22],
        'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław']}
df = pd.DataFrame(data)
 
# Wyświetlenie pierwszych dwóch wierszy DataFrame
print(df.head(2))
# Wyświetlenie ostatnich dwóch wierszy DataFrame
print(df.tail(2))
# Wybór wiersza po etykiecie indeksu
print(df.loc[1])
# Wybór wiersza po numerze indeksu
print(df.iloc[2])
