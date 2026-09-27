# Metody i dziedziczenie klas

class Zwierze:
    def __init__(self, imie: str) -> None:
        self.imie = imie

    def przedstaw_sie(self) -> str:
        return f"Mam na imie {self.imie}."


class Pies(Zwierze):
    def przedstaw_sie(self) -> str:
        return f"Hau! {super().przedstaw_sie()}"


pies = Pies("Reks")
print(pies.przedstaw_sie())
