# Przykad klasy w Pythonie

class CPoint2D:
    counter = 0  # class attribute to count instances

    def __init__(self,x,y):
        self.x = x
        self.y = y
        CPoint2D.counter += 1  # increment counter when a new point is created

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self) -> str:
        return f"Point = ({self.x}, {self.y})"
    
a = CPoint2D(1,2)
b = CPoint2D(4,6)
print(a)  # Point = (1, 2)
print(b)  # Point = (4, 6)
print("Distance:", a.distance(b))  # Distance: 5.0
a.move(2,3)
print(a)  # Point = (3, 5)
print("Number of points created:", CPoint2D.counter)  # Number of points created: 2