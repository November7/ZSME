# class Osoba:
#     def __init__(self,imie,nazwisko) -> None:
#         self.pesel = ""
#         self.imie = imie
#         self.nazwisko = nazwisko
#     def Wypisz(self):
#         print(f"{self.imie} {self.nazwisko} {self.pesel if self.pesel!='' else '' }")

#     def wprowadzPesel(self,pesel):
#         if Osoba.sprawdzPesel(pesel): # Wywołanie metody statycznej
#             self.pesel = pesel

#     @staticmethod
#     def czyRokPrzestepny(rok):
#         if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0): return True
#         else: return False

#     @staticmethod
#     def sprawdzPesel(pesel):
#         pesel = str(pesel)
#         if len(pesel) != 11: return False
#         sum = 0
#         w = [1,3,7,9,1,3,7,9,1,3]        
#         for s,i in zip(pesel[:10],range(10)):
#             if s<'0' or s>'9': return False
#             sum += w[i]*int(s)
#         sum = (10 - sum % 10) % 10        
#         if sum != int(pesel[-1]): return False
        
#         d = [31,28,31,30,31,30,31,31,30,31,30,31]
#         rr = int(pesel[0:2])
#         mm = int(pesel[2:4])
#         dd = int(pesel[4:6])
        
#         cent = (1 + mm // 20) % 5 
#         mm %= 20 

#         rrrr = 1800 + 100 * cent + rr

#         if Osoba.czyRokPrzestepny(rrrr): # Wywołanie metody statycznej
#             d[1] = 29

#         if dd<1 or dd>d[mm-1]: return False
#         if mm <1 or mm > 12: return False

#         return True

# class CExample:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self,other):
#         if self.x == other.x and self.y == other.y: return True
#         else: return False

#     def __str__(self):
#         return f"{self.x}, {self.y}"
    
#     def __int__(self):
#         return int(self.x)
    
#     def __float__(self):
#         return float(self.x/self.y)
    
#     def __iter__(self):
#         return iter([self.attrib,2,3,4,5])
    
#     def __iadd__(self,other):
#         self.x += other.x
#         self.y += other.y
#         return self


# a = CExample(1, 2)
# b = CExample(1, 2)
# c = CExample(1, 3)

# print(a == b) # True
# print(a == c) # False
# print(a == b == c) # False

# a += c

# print(a)

# a = Osoba("Jan","Nowak")
# a.wprowadzPesel("44051401458")

# print(Osoba.sprawdzPesel("44051401458")) #Wywołanie metody statycznej
# print(Osoba.czyRokPrzestepny(2000)) # Wywołanie metody statycznej
# print(Osoba.czyRokPrzestepny(2024)) # Wywołanie metody statycznej
# print(Osoba.czyRokPrzestepny(2022)) # Wywołanie metody statycznej

# a.Wypisz()

def checkClassMember(obj,member):
    ret = f"{member} is " 
    member = str(member)
    if str(type(obj)) == "<class 'type'>":
        objType = obj  
        pureObj = objType()
        obj = objType()
    else:
        objType = type(obj)
        pureObj = objType()      

    if member in vars(objType):
        if callable(vars(objType)[member]):
            return ret+"a method"

    inDir = member in dir(obj)
    inVars = member in vars(obj)
    inPure = member in dir(pureObj)

    if inDir and inPure and inVars:
        return ret+"an instance attribute"
    elif inDir and inPure and not(inVars):
        return ret+"a static attribute"
    elif inDir and not(inPure) and inVars:
        return ret+"a dynamic instance attribute"
    else:
        return ret+"is undefined"

# class T:
#     x = 1 # atrybut statyczny
#     def __init__(self) -> None:
#         self.y = 2 # atrybut instancji

    
# ob = T()
# ob.z = 3 # dynamiczny atrybut intancji

# print("Dla klasy T:")
# print(checkClassMember(T,"x"))
# print(checkClassMember(T,"y"))
# print(checkClassMember(T,"z"))

# print("Dla obiektu klasy T:")
# print(checkClassMember(ob,"x"))
# print(checkClassMember(ob,"y"))
# print(checkClassMember(ob,"z"))


class CExample:
    x = 1 # atrybut klasy 
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









