import pandas as pd
import os
import matplotlib.pyplot as plt

#1 pobieranie danych
path = os.path.dirname(__file__)

df = pd.read_csv(f"{path}\\temperature.csv",sep=";",decimal=".")


# #2 Wyświetlanie danych

# #2a
# print(df.head(10))
# #2b
# print(df.tail(10))
# #2c
# print(df.to_string())

#3 Porządkowanie danych

#3a
df.drop("record_id",axis=1,inplace=True)
# print(df.head())

#3b
# df["id"] = range(len(df))
# print(df.head())

#3c
df.insert(0,"id",range(len(df)))
# print(df.head())

#3d
kolumny = ["id","year","month","day","AverageTemperatureFahr","AverageTemperatureUncertaintyFahr","City","country_id","Country","Latitude","Longitude"]
df = df[kolumny]
# print(df.head())

#3e
df.rename(columns = {"AverageTemperatureFahr":"AvgTmpF"},inplace=True)
df.rename(columns = {"AverageTemperatureUncertaintyFahr":"AvgTmpUncF"},inplace=True)
# print(df.head())

#3f
df = df[["id","year","month","day","AvgTmpF","AvgTmpUncF","City","Country","Latitude","Longitude"]]
# print(df.head())

#4 Poprawianie danych:

#4a
def F2C(tmp):
    return 5 * (tmp - 32) / 9

# def C2F(tmp):
#     return 9 * tmp / 5 + 32

df["AvgTmpC"] = df["AvgTmpF"].apply(F2C)
df["AvgTmpUncC"] = df["AvgTmpUncF"].apply(F2C)
# print(df.head(20))

df = df[["id","year","month","day","AvgTmpC","AvgTmpUncC","City","Country","Latitude","Longitude"]]
# print(df.head(20))


#4b
def LatLong(inp):
    last = inp[-1]
    try:
        val = float(inp[:-1])
    except:
        val = 0
    if last == "S" or last == "W":
        return -val
    else:
        return val

df["Latitude"] = df["Latitude"].apply(LatLong)
df["Longitude"] = df["Longitude"].apply(LatLong)
# print(df.head(20))

# #4c
# df_beznan = df.dropna()
# print(df_beznan.head())

#4d
# df_beznan = df.fillna(0)
# print(df_beznan.head())

#4e

# df.fillna({"AvgTmpUncC" : 0}, inplace=True)
df["AvgTmpUncC"] = df["AvgTmpUncC"].fillna(0)

# print(df.head())

#4f
def AvgLoc(dane):
    return dane.fillna(dane.mean())

df["AvgTmpC"] = df.groupby(["City", "Country", "month"])["AvgTmpC"].transform(AvgLoc)
# df["AvgTmpC"] = df.groupby(["City", "Country", "month"])["AvgTmpC"].transform(lambda x: x.fillna(x.mean()))
# print(df.head())

#5 Filtowanie

# 5a 
# print(df[["id","Country","AvgTmpC"]])

# 5b
# print(df[["id","Country","AvgTmpC"]].loc[df["AvgTmpC"]<0])

# 5c
cond1 = df["AvgTmpC"] > 20
cond2 = df["AvgTmpC"] < -10
cond3 = df["Country"] == "Poland"
print(df[["id","Country","AvgTmpC"]].loc[cond3 & (cond1 | cond2)])

# #6 Statystyki


# srednia_temp = df["AvgTmpC"].mean() 
# max_temp = df["AvgTmpC"].max() 
# min_temp = df["AvgTmpC"].min() 
# print(f"Ilość danych: {len(df)}")
# print(f"Średnia temperatura: {srednia_temp}") 
# print(f"Minimalna temperatura: {min_temp}")
# print(f"Maksymalna temperatura: {max_temp}")

# #7 Grupowanie

# # filtr1 = df.loc[df["year"]>1900]
filtr1 = df



# # 7a
grupa0 = filtr1.groupby("Country").count()
print(grupa0)
print(grupa0.index.tolist())

# # 7b
# grupa1 = filtr1.groupby(["Country","year"])["AvgTmpC"].mean()
# # print(grupa1)
# print(grupa1.loc[("Poland")])

# # 7c
# grupa2 = filtr1.groupby(["Country","year","month"])["AvgTmpC"].mean()
# print(grupa2.loc[("Poland")])
# print(grupa2.loc[("Poland",1901)])
# print(grupa2.loc[("Poland",1901,1)])

# # 7d
# grupa3 = filtr1.groupby(["year","month","Country"])["AvgTmpC"].mean()
# print(grupa3.loc[(1901)])



#8 Wykresy



dane_w1 = df[["Country","year","month","AvgTmpC"]].loc[df["Country"]=="Poland"]
dane_w2 = df[["Country","year","month","AvgTmpC"]].loc[df["Country"]=="Sweden"]
dane_w3 = df[["Country","year","month","AvgTmpC"]].loc[df["Country"]=="France"]
grupa1 = dane_w1.groupby(["year"])["AvgTmpC"].mean()
grupa2 = dane_w2.groupby(["year"])["AvgTmpC"].mean()
grupa3 = dane_w3.groupby(["year"])["AvgTmpC"].mean()

#8a

xlabels = grupa1.index.tolist()[::20]


plt.plot(grupa1.index,grupa1.values,label = "Polska")
plt.plot(grupa2.index,grupa2.values,label = "Szwecja")
plt.plot(grupa3.index,grupa3.values,label = "Francja")
plt.title("Średnia temperatura na przestrzeni lat") 
plt.xticks(xlabels)
plt.xlabel("Miesiąc") 
plt.ylabel("Średnia temperatura (°C)") 
plt.legend() 
plt.grid(True)
plt.show()


