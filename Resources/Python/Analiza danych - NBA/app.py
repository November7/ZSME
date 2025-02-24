import pandas as pd
# from matplotlib import pyplot as plt

#załaduj pliki

# players = pd.read_csv("players-data.csv",sep=';')
# collages = pd.read_csv("players-collage.csv",sep=';')
# salaries = pd.read_csv("players-salary.csv",sep=';')



#wyświetl załadowane dane oraz informacje o nagłówkach

# print(players.head(3))
# print(players.info())

# print(collages.head(3))
# print(collages.info())

# print(salaries.head(3))
# print(salaries.info())


#połącz wszystkie tabele łącząc tylko istniejące dane

# merged_tmp = pd.merge(left=players,right=collages,how="inner")
# merged_inner = merged_tmp.merge(salaries,how="inner")

# print(merged_inner.to_string())
# print(merged_inner.info())

#Połącz tabele players-data z tabelami players-collage i players-salary. Tabela players-data jest nadrzędna

# merged_tmp = pd.merge(left=players,right=collages,how="left")
# merged_left = merged_tmp.merge(salaries,how="left")
# print(merged_left)
# # print(merged_left.info())

# grp1 = merged_left.groupby("Team").agg(Means = ("Salary","mean"))
# grp1["Means"] = grp1["Means"].map('{:.2f}'.format)
# merged_all = merged_left.merge(grp1,on="Team",how="left")
# print(merged_all)
# print(merged_all.info())

# merged_all["Means"] = merged_all["Means"].map(lambda x: float(x))
# print(merged_all)
# print(merged_all.info())

# merged_all['Salary'][merged_all['Salary'].isna()] = merged_all["Means"]
# print(merged_all)
# print(merged_all.info())

# # #globalne formatowanie wyświetlania
# # # pd.options.display.float_format = '{:,.2f} $'.format

# #formatowanie wyświetlania konkretnej kolumny
# merged_all["SalaryUSD"] = merged_all["Salary"].map('{:,.2f} $'.format)
# merged_all["SalaryUSD"] = merged_all["SalaryUSD"].map(lambda x: x.replace(',',' '))

# del merged_all["Means"]

# print(merged_all)
# print(merged_all.info())


# plt.hist(merged_all["Salary"], bins = 25)
# plt.xticks(rotation=45)
# xlabels = plt.gca().get_xticks().tolist()
# plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in xlabels])
# plt.tight_layout()
# plt.show()

# BC = merged_all[merged_all["Team"] == "Boston Celtics"]
# plt.hist(BC["Salary"], bins = 25)
# plt.xticks(rotation=45)
# xlabels = plt.gca().get_xticks().tolist()
# plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in xlabels])
# plt.tight_layout()
# plt.show()


# UJ = merged_all[merged_all["Team"] == "Utah Jazz"]
# plt.bar(UJ["Name"],UJ["Salary"])
# plt.xticks(rotation=45, ha='right')
# ylabels = plt.gca().get_yticks().tolist()
# plt.gca().set_yticklabels(['{:,.0f} $'.format(y) for y in ylabels])
# plt.tight_layout()
# plt.show()


# plt.pie(UJ["Salary"],labels=UJ["Name"])
# plt.show()
