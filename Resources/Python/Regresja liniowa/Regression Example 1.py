### Importowanie bibliotek

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


### Wczytanie danych

df = pd.read_csv('example1.csv',sep=';',decimal=',')

print(df.head())
print(df.shape)

# X = []
# for i in df['X']:
#     X.append([i])
# Y = list(df['Y'])


X = np.single(df['X'])
Y = np.single(df['Y'])

X.shape = (-1,1) # odwracanie wektora X (zmiana wymiarów z poziomego na pionowy)

print(X,Y)

plt.figure(figsize=[8,8], facecolor="white")

plt.title("Dane z pomiaru")
plt.xlabel('x')
plt.ylabel("y")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.plot(X,Y,'o')
plt.show()

#Wyznaczanie parametrów modelu

model = LinearRegression().fit(X,Y)

print(model.coef_)
print(model.intercept_)
a = model.coef_[0]
b = model.intercept_

print(f"Wynikiem jest prosta o równaniu y = {a:.3f} x {b:+.3f}")

# X = np.arange(-10,10) #
x_test = np.single(range(int(X.min())-2,int(X.max())+2))
x_test.shape = (-1,1)

y_predict = model.predict(x_test)
print(f"Wynik dopasowania: {100*model.score(X,Y):.2f}%")

plt.figure(figsize=[8,8], facecolor="white")
plt.title(f'Funkcja liniowa o równaniu y = {a:.3f} x {b:+.3f} dopasowana do danych')

plt.xlabel('x')
plt.ylabel("y")
plt.axis([X.min()-2,X.max()+2,Y.min()-2,Y.max()+2])
plt.grid(True,which="both",axis="both",alpha=.5)
plt.plot(X,Y,'o')
plt.plot(x_test,y_predict,'-')
plt.show()

### Importowanie bibliotek

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

pf = PolynomialFeatures(12)
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