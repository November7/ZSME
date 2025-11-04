# definicja klasy
class CPoint:
    counter = 0 # atrybut klasy
    def __init__(self, x = 0, y = 0): # Konstruktor klasy
        self.x = x # atrybut obiektu (instancji)
        self.y = y # atrybut obiektu (instancji)
        print(f"To ja konstruktor, tworzę nowy obiekt {self}") 
        CPoint.counter += 1
    
    def __str__(self): # metoda konwertująca nasz obiekt na string
        return f"Point = ({self.x}, {self.y})"
    
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**.5
    
    # def __add__(self,other):
    #     return CPoint(self.x + other.x, self.y + other.y)


print(f'Licznik obiektów: {CPoint.counter}')

# definicja obiektów (instancji) klasy
A = CPoint(3, 4)
B = CPoint(1, 2)

print(f'Licznik obiektów: {CPoint.counter} lub {A.__class__.counter}')

print(f'{A}')
print(f'{B}')
print(f'Odleglość {A} od {B} wynosi {A.distance(B)}')



