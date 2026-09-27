# Biblioteka pandas: Series i DataFrame

import pandas as pd

seria = pd.Series([10, 20, 30], name="wynik")
data = pd.DataFrame({"imie": ["Anna", "Jan"], "wiek": [28, 34]})

print(seria)
print(data)
print(data.head(1))
