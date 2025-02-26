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

