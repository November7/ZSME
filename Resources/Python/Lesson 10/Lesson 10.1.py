# Klasy w Python

class CExample:
    x = 1 # atrybut klasy (wspólny dla wszystkich instancji klasy)
    def __init__(self):
        self.y = 2    #atrybut instancji (każda instancja będzie go posiadała)    

a = CExample()

print(a.x) # 1, niepoprawne odwołanie do atrybutu x (sugeruje że to jest składnik instancji), zostanie wypisana wartość atrybutu klasy
print(a.__class__.x) # 1, prawidłowe odwołanie do atrybutu klasowego za pomocą instancji 
print(CExample.x) # 1, poprawne odwołanie do atrybutu x 

print(a.y) # 2, poprawne odwołanie do atrybutu y (jest to atrybut obiektu a)
#print(CExample.y) # błąd, atrybut y należy do obiektu a nie do klasy

a.z = 3 # dynamiczne utworzenie atrybutu z w obiekcie a (tylko obiekt a będzie go posiadał)
print(a.z) # 3, poprawne odwołanie do atrybutu z (jest to dynamiczny atrybut obiektu a)

b = CExample()

#print(b.z) # błąd, b nie posiada atrybutu z

b.x = 4 # klasowy atrybut x zostanie nadpisany przez dynamiczny atrybut obiektu b. Od teraz obiekt b ma swój atrybut x

print(CExample.x) # 1, atrybut wspólny dla wszystkich obiektów, nadpisanie atrybutu w obiekcie b nie ma wpływu na atrybut klasy
print(a.x) # 1, niepoprawne odwołanie do atrybutu x (sugeruje że to jest składnik instancji), zostanie wypisana wartość atrybutu klasy
print(b.x) # 4, atrybut x w obiekcie b zasłania (nadpisuje) klasowy atrybut x 
print(b.__class__.x) # 1, obiekt b może odwołać się do klasowego atrybutu x tylko w ten sposób

