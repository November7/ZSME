
class Point:
    def __init__(self): #konstruktor
        self.x = 0
        self.y = 0


A = Point()
B = Point()

print(A.x, A.y)
print(B.x, B.y)


#definicja klasy (typu)
class Punkt:
    x = 1 #statyczny składnik klasy (całej klasy)

print(Punkt.x)

ob1 = Punkt()
ob2 = Punkt()

print("Etap 1")
print(ob1.x) # print(ob1.__class__.x)
print(ob2.x)

Punkt.x = 123

print("Etap 2")
print(ob1.x)
print(ob2.x)

ob1.x = "trzy"

print("Etap 3")
print(ob1.x)
print(ob2.x)

ob1.x = 2
print("Etap 4")
print(ob1.x)
print(ob2.x)

del ob1.x

print("Etap 5")
print(ob1.x)
print(ob2.x)




