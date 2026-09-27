### Importowanie bibliotek

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split


#zmiana katalogu na ten w którym znajduje się skrypt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### Wczytanie danych

df = pd.read_csv("Happiness.csv",delimiter=",", decimal=",")

print(df.head())
print(df.shape)
print(df.describe())

os.system('pause')

X = np.single(df['income'])
X.shape = (-1,1)
Y = np.single(df['happiness'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3) #, random_state=12

plt.figure(figsize=[8,8], facecolor="white")
plt.title("Dane z importu")

plt.xlabel('income')
plt.ylabel("happiness")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.legend(["Wszystkie dane","Dane treningowe"])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.plot(X,Y,'.')
plt.plot(X_train,y_train,'r+')
plt.show()  

pf = PolynomialFeatures(5)
x_train_trans = pf.fit_transform(X_train)
x_test_trans = pf.fit_transform(X_test)
x_trans = pf.transform(X)

model = LinearRegression().fit(x_train_trans,y_train)

print(f"Wynik dopasowania do danych treningowych: {100*model.score(x_train_trans,y_train):.2f}%")
print(f"Wynik dopasowania do danych testowych: {100*model.score(x_test_trans,y_test):.2f}%")
print(f"Wynik dopasowania do wszystkich danych: {100*model.score(x_trans,Y):.2f}%")

print(model.coef_, model.intercept_)

x_test = np.arange(X.min(),X.max(),0.1)
x_test.shape = (-1,1)

plt.figure(figsize=[10,10], facecolor="white")
plt.plot(X,Y,'.')
plt.plot(X_train,y_train,'r+')
plt.plot(x_test,model.predict(pf.fit_transform(x_test)),'-')
plt.legend(["Wszystkie dane","Dane treningowe","Wynik regresji"])
plt.xlabel('x')
plt.ylabel("y")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.show()
