import pickle as pkl

import pandas as pd

sciezka_modelu = "D:\\Source\\ZSME\\Resources\\Python\\Regresja liniowa\\Zadanie 2\\model.pkl"



def main():
    print("Aplikacja prognozy spalania samochodu (l/100 km)")

    with open(sciezka_modelu, "rb") as f:
        model = pkl.load(f)


    print(f"Wczytano model: {sciezka_modelu}")

    masa_kg = float(input("Podaj mase pojazdu [kg]: ").replace(",", "."))
    moc_km = float(input("Podaj moc silnika [KM]: ").replace(",", "."))
    opory_aero = float(input("Podaj wspolczynnik oporu aerodynamicznego: ").replace(",", "."))

    dane = pd.DataFrame(
        [{"masa_kg": masa_kg, "moc_km": moc_km, "opory_aero": opory_aero}]
    )


    prognoza = model.predict(dane)[0]
    print(f"\nHipotetyczne spalanie: {prognoza:.2f} l/100 km")


if __name__ == "__main__":
    main()
