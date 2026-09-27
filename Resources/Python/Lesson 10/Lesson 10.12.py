class CExample:
    x = 1 # atrybut klasy 
    def __init__(self):
        self.y = 2    #atrybut instancji (każda instancja będzie go posiadała)    
 
a = CExample()
 
print(a.x) # 1, poprawny odczyt: instancja nie ma własnego x, więc używany jest atrybut klasy
print(a.__class__.x) # 1, prawidłowe odwołanie do atrybutu klasowego za pomocą instancji 
print(CExample.x) # 1, poprawne odwołanie do atrybutu x 
 
print(a.y) # 2, poprawne odwołanie do atrybutu y (jest to atrybut obiektu a)
#print(CExample.y) # błąd, atrybut y należy do obiektu a nie do klasy
setattr(a, "z", 3)
print(getattr(a, "z")) # 3, poprawne odwołanie do atrybutu z (jest to dynamiczny atrybut obiektu a)
 
b = CExample()
 
#print(b.z) # błąd, b nie posiada atrybutu z
 
b.x = 4 # powstanie atrybut instancji b, który zasłoni atrybut klasy x. Od teraz obiekt b ma swój atrybut x
 
print(CExample.x) # 1, atrybut wspólny dla wszystkich obiektów, nadpisanie atrybutu w obiekcie b nie ma wpływu na atrybut klasy
print(a.x) # 1, poprawny odczyt: instancja nie ma własnego x, więc używany jest atrybut klasy
print(b.x) # 4, atrybut x w obiekcie b zasłania klasowy atrybut x, nie zmieniając go 
print(b.__class__.x) # 1, odczyt atrybutu klasy; można też użyć CExample.x
