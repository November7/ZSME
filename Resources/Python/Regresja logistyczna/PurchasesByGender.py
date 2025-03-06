import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sn

#zmiana katalogu na ten w którym znajduje się skrypt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
dane = pd.read_csv('PurchasesByGender.csv')

print(dane.head())
print(dane.info())

dane['Gender'] = dane['Gender'].map(lambda x: 1 if x == "Male" else 0)

print(dane.head())

X = np.array(dane[["Gender","Age","EstimatedSalary"]])
y = np.array(dane["Purchased"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(model.score(X_train,y_train))
print(model.score(X_test,y_test))
print(accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred)) # TN, FP, FN, TP



# sn.heatmap(confusion_matrix(y_test, y_pred),annot=True)
           
plt.show()

#przykładowe dane
gender, age, salary = map(int, input("Podaj płeć [0/1], wiek, zarobki: ").split())

X_input = np.array([gender, age, salary]).reshape(1, -1)
print(model.predict(X_input))

