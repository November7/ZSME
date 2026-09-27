import pandas as pd
 
dane = pd.read_csv("plik.csv",sep=";",encoding="UTF-8",decimal=",") # import danych z pliku CSV
#dane = pd.read_excel("plik.xlsx") # import danych z pliku Excel
 
print(dane)
