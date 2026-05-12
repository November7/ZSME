from pathlib import Path

import pickle


MODEL_PATH = Path(__file__).with_name("model_cena_mieszkan.pkl")

def main():
    # 1. Wczytanie modelu
    with MODEL_PATH.open("rb") as f:
        model = pickle.load(f)
    print("Model załadowany.")

    # 2. Pobranie danych od użytkownika
    metraz = float(input("Podaj metraż [m2]: "))
    pietro = int(input("Podaj piętro: "))
    odl = float(input("Podaj odległość od centrum [km]: "))
    rok = int(input("Podaj rok budowy: "))
    standard = int(input("Podaj standard (1-5): "))

    # 3. Predykcja w kolejnosci cech zgodnej z treningiem modelu
    dane = [[metraz, pietro, rok, standard, odl]]
    pred = model.predict(dane)[0]
    print(f"\nPrzewidywana cena mieszkania: {pred:.2f} tys. PLN")

if __name__ == "__main__":
    main()
