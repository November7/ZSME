import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv(r"C:\Dane lokalne\Source\ZSME\Resources\Python\Złączenia tabel\państwa.csv",sep=";",decimal=",",encoding="utf-8")
cities = pd.read_csv(r"C:\Dane lokalne\Source\ZSME\Resources\Python\Złączenia tabel\miasta.csv",sep=";",decimal=",",encoding="utf-8")
weather = pd.read_csv(r"C:\Dane lokalne\Source\ZSME\Resources\Python\Złączenia tabel\pogoda.csv",sep=";",decimal=",",encoding="utf-8")


print(countries)
print(cities)
print(weather)

cc = pd.merge(countries,cities,how="inner",on="Miasto")

full = pd.merge(cc,weather,how="inner",on="Miasto")

print(full)

plt.scatter(full["Długość"],full["Szerokość"])

for i in range(len(full)):
    plt.text(full['Długość'][i], full["Szerokość"][i], full['Miasto'][i])

plt.show()


# plt.bar(full["Miasto"],full["Temperatura"])
# plt.bar(full["Miasto"],full["Opad"])
# plt.xticks(rotation=45)  
# plt.legend(["Temperatura","Opad"])
# plt.show()

# plt.plot(full["Temperatura"])
# plt.show()


x = list(range(len(full["Miasto"])))
x2 = [i+.4 for i in x]

plt.bar(x,full["Opad"],width = 0.4)
plt.bar(x2,full["Temperatura"],width=0.4)

plt.xticks(rotation=45)  
plt.legend(["Temperatura","Opad"])
plt.xticks(x2, full["Miasto"])
plt.show()

