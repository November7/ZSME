class CPoint:
    counter = 0
    def __init__(self, x=0, y=0, name="Point"):
        self.x = x
        self.y = y
        self.name = name
        CPoint.counter += 1


    def Distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5 
        # Pierwastek kwadratowy z sumy kwadratów różnic współrzędnych

    def __str__(self):
        return f"{self.name} = ({self.x}, {self.y})"


p1 = CPoint(2, 3, "A")
p2 = CPoint(5, 7, "B")  

print(p1)
print(p2)
print(f"Odległość {p1} od {p2}: {p1.Distance(p2)}")