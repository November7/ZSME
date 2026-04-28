import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# Ustaw katalog roboczy na folder skryptu.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 1. Wczytanie danych z pliku CSV
df = pd.read_csv("mieszkania_dane.csv")

print("Podglad danych:")
print(df.head())
print("\nRozmiar danych:", df.shape)
print("\nStatystyki opisowe:")
print(df.describe())


# 2. Przygotowanie cech i zmiennej celu
feature_cols = [
    "metraz_m2",
    "pokoje",
    "pietro",
    "odleglosc_km",
    "rok_budowy",
    "standard",
]

X = df[feature_cols]
y = df["cena_tys_pln"]


# 3. Podzial na zbior treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)


# 4. Trenowanie modelu
model = LinearRegression()
model.fit(X_train, y_train)


# 5. Predykcja i ewaluacja
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

mae_train = mean_absolute_error(y_train, y_train_pred)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
r2_train = r2_score(y_train, y_train_pred)

mae_test = mean_absolute_error(y_test, y_test_pred)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2_test = r2_score(y_test, y_test_pred)

print("\nWyniki modelu:")
print(f"Train -> MAE: {mae_train:.2f}, RMSE: {rmse_train:.2f}, R2: {r2_train:.4f}")
print(f"Test  -> MAE: {mae_test:.2f}, RMSE: {rmse_test:.2f}, R2: {r2_test:.4f}")

print("\nWspolczynniki modelu:")
for col, coef in zip(feature_cols, model.coef_):
    print(f"{col:15s}: {coef:8.3f}")
print(f"Wyraz wolny      : {model.intercept_:8.3f}")


# 6. Przykladowa predykcja dla nowego mieszkania
nowe_mieszkanie = pd.DataFrame(
    {
        "metraz_m2": [76],
        "pokoje": [4],
        "pietro": [5],
        "odleglosc_km": [2.7],
        "rok_budowy": [2018],
        "standard": [5],
    }
)

pred_cena = model.predict(nowe_mieszkanie)[0]
print(
    "\nPredykcja nowego mieszkania (w tys. PLN): "
    f"{pred_cena:.2f}"
)


def read_float(prompt):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Niepoprawna wartosc. Podaj liczbe, np. 75 lub 2.8")


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Niepoprawna wartosc. Podaj liczbe calkowita, np. 4")


def manual_prediction_loop():
    print("\n=== Reczne testowanie modelu ===")
    print("Mozesz podac parametry mieszkania i dostac predykcje ceny.")
    print("Aby zakonczyc, nacisnij Enter bez wpisywania danych.")

    while True:
        first = input("\nMetraz [m2] (Enter = koniec): ").strip().replace(",", ".")
        if first == "":
            print("Zakonczono reczne testowanie modelu.")
            break

        try:
            metraz = float(first)
        except ValueError:
            print("Niepoprawna wartosc metrazu. Sprobuj ponownie.")
            continue

        pokoje = read_int("Liczba pokoi: ")
        pietro = read_int("Pietro: ")
        odleglosc_km = read_float("Odleglosc od centrum [km]: ")
        rok_budowy = read_int("Rok budowy: ")
        standard = read_int("Standard (1-5): ")

        mieszkanie = pd.DataFrame(
            {
                "metraz_m2": [metraz],
                "pokoje": [pokoje],
                "pietro": [pietro],
                "odleglosc_km": [odleglosc_km],
                "rok_budowy": [rok_budowy],
                "standard": [standard],
            }
        )

        cena_pred = model.predict(mieszkanie)[0]
        print(f"Przewidywana cena: {cena_pred:.2f} tys. PLN")


# 7. Wykresy
plt.style.use("seaborn-v0_8-whitegrid")

# Wykres 1: Zaleznosc ceny od metrazu (kolor = odleglosc)
plt.figure(figsize=(10, 6), facecolor="white")
sc = plt.scatter(
    df["metraz_m2"],
    df["cena_tys_pln"],
    c=df["odleglosc_km"],
    cmap="viridis",
    s=80,
    alpha=0.9,
    edgecolors="black",
    linewidths=0.4,
)
plt.colorbar(sc, label="Odleglosc od centrum [km]")
plt.title("Cena mieszkania vs metraz")
plt.xlabel("Metraz [m2]")
plt.ylabel("Cena [tys. PLN]")
plt.tight_layout()
plt.show()


# Wykres 2: Rzeczywiste vs przewidywane (zbior testowy)
plt.figure(figsize=(8, 8), facecolor="white")
plt.scatter(y_test, y_test_pred, color="tab:blue", s=80, alpha=0.9)
min_val = min(y_test.min(), y_test_pred.min())
max_val = max(y_test.max(), y_test_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2)
plt.title("Rzeczywista cena vs przewidywana cena (test)")
plt.xlabel("Rzeczywista cena [tys. PLN]")
plt.ylabel("Przewidywana cena [tys. PLN]")
plt.tight_layout()
plt.show()


# Wykres 3: Reszty modelu
residuals = y_test - y_test_pred

fig, ax = plt.subplots(1, 2, figsize=(14, 5), facecolor="white")

ax[0].scatter(y_test_pred, residuals, color="tab:orange", s=75, alpha=0.9)
ax[0].axhline(y=0, color="black", linestyle="--")
ax[0].set_title("Reszty vs przewidywania")
ax[0].set_xlabel("Przewidywana cena [tys. PLN]")
ax[0].set_ylabel("Reszta [tys. PLN]")

ax[1].hist(residuals, bins=8, color="tab:green", edgecolor="black", alpha=0.85)
ax[1].set_title("Histogram reszt")
ax[1].set_xlabel("Reszta [tys. PLN]")
ax[1].set_ylabel("Liczebnosc")

plt.tight_layout()
plt.show()


# Wykres 4: Wplyw cech (wspolczynniki modelu)
plt.figure(figsize=(10, 6), facecolor="white")
coef_series = pd.Series(model.coef_, index=feature_cols).sort_values()
coef_series.plot(kind="barh", color="tab:purple", edgecolor="black")
plt.title("Wspolczynniki regresji liniowej")
plt.xlabel("Zmiana ceny [tys. PLN] na jednostke cechy")
plt.ylabel("Cecha")
plt.tight_layout()
plt.show()


# 8. Interaktywny test modelu
manual_prediction_loop()