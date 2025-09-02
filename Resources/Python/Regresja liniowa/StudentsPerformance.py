import pandas as pd
import numpy as np
import seaborn as sns #pip install seaborn


from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score 


#zmiana katalogu na ten w którym znajduje się skrypt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))



### Wczytanie danych

df = pd.read_csv("StudentsPerformance.csv",delimiter=",", decimal=".")


print(df.columns)
print(df.head())
print(df.shape)
print(df.describe())
print(df.info())
print(df.isnull().sum())

os.system("pause")

df['Extracurricular Activities'] = df['Extracurricular Activities'].replace({'Yes': 1, 'No': 0})

target = "Performance Index"

for col in ['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']:    
    plt.figure() 
    plt.scatter(df[col], df[target])
    plt.xlabel(col)
    plt.ylabel(target)
    plt.title(f'{col} vs {target}')
    plt.show()

def Ranges(perf):
    if perf < 25:
        return 1
    elif perf < 50:
        return 2
    elif perf < 75:
        return 3
    else:
        return 4

df_ranges = df.copy()
df_ranges['Ranges'] = df_ranges['Performance Index'].apply(Ranges)

print(df_ranges.head())


#
# sns.pairplot(df_ranges,hue='Ranges',palette='coolwarm')
sns.pairplot(df,hue='Performance Index',palette='coolwarm')
plt.show()

corr = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()

X = df[['Hours Studied','Previous Scores','Extracurricular Activities','Sleep Hours','Sample Question Papers Practiced']]  
y = df['Performance Index']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


model = LinearRegression()
model.fit(X_train, y_train)

print(model.coef_, model.intercept_)

y_predicted = model.predict(X_test)

comparison_df = pd.DataFrame({'Dane': y_test, 'Przewidywane': y_predicted, 'Różnica': y_predicted-y_test})
print(comparison_df.head())

mse = mean_squared_error(y_test, y_predicted)
r2 = r2_score(y_test, y_predicted)
print("Mean Squared Error: ", mse) #Błąd średniokwadratowy
print("R2 Error: ", r2) #Współczynnik determinacji 
print("Model score: ", model.score(X_test,y_test)) #Współczynnik determinacji najczęściej to samo co R2