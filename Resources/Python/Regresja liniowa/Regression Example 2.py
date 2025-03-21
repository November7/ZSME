### Importowanie bibliotek

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures



#zmiana katalogu na ten w którym znajduje się skrypt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### Wczytanie danych

df = pd.read_csv("example2.csv",delimiter=";", decimal=",")

print(df.head())
print(df.shape)

X = np.single(df['x'])
X.shape = (-1,1)
Y = np.single(df['y'])

plt.figure(figsize=[8,8], facecolor="white")
plt.title("Dane z importu")

plt.xlabel('x')
plt.ylabel("y")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.plot(X,Y,'.')
plt.show()

pf = PolynomialFeatures(2)
x_trans = pf.fit_transform(X)

model = LinearRegression().fit(x_trans,Y)

print(f"Wynik dopasowania: {100*model.score(x_trans,Y):.2f}%")
print(model.coef_, model.intercept_)

x_test = np.arange(X.min()-2,X.max()+2,0.1)
x_test.shape = (-1,1)

plt.figure(figsize=[8,8], facecolor="white")
plt.plot(X,Y,'.')
plt.plot(x_test,model.predict(pf.fit_transform(x_test)),'-')
plt.xlabel('x')
plt.ylabel("y")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.show()


from sklearn.model_selection import train_test_split
# Podział na zestaw treningowy (70%) i testowy (30%)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5) #, random_state=12

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