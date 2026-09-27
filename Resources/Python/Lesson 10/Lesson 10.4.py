# Dataclass jako prosty model danych

from dataclasses import dataclass


@dataclass
class Punkt:
    x: float
    y: float

    def przesun(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy


punkt = Punkt(1, 2)
punkt.przesun(3, -1)
print(punkt)
