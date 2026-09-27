# Import danych CSV w pandas

import pandas as pd

# Plik powinien zawierac naglowek: imie;wiek
# dane = pd.read_csv("osoby.csv", sep=";", encoding="utf-8")
# print(dane.head())

przyklad = pd.DataFrame({"imie": ["Anna", "Jan"], "wiek": [28, 34]})
print(przyklad.loc[przyklad["wiek"] > 30])
