# klasy w python

x:int = 12312312
t:str = "c:\\napis.txt"
pi:float = 3.14
b:bool = 3 > 5
c:complex = 3 + 1j

lista = [1,23,4,3,5,6,6,"343"]
krotka = (1,23,4,3,5,6,6,"343")
zestaw = {1,23,4,3,5,6,6,"343"}
slownik = {"klucz":"wartość", "1":"str jeden", 1:"jeden", 2:2, 3.14:"pi", (3 + 1j): "Tak"}
print(f"{lista}\n{krotka}\n{zestaw}\n{slownik}")

class Ulamek:
    def __init__(self, licz = 0, mian = 1, nazwa = ""):
        self.licznik = licz
        if mian == 0:
            self.mianownik = 1
        else:
            self.mianownik = mian

        self.nazwa = nazwa

    def __str__(self):
        if self.licznik > self.mianownik:            
            return f"Ulamek {self.nazwa} = {self.licznik//self.mianownik} i {self.licznik % self.mianownik}/{self.mianownik}"
        else:
            return f"Ulamek {self.nazwa} = {self.licznik}/{self.mianownik}"
    
    def __float__(self):
        return self.licznik / self.mianownik
    
    def __mul__(self, other):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __add__(self, other):
        if self.mianownik == other.mianownik:
            return Ulamek(self.licznik + other.licznik, self.mianownik)
        else:
            return Ulamek(self.licznik * other.mianownik + other.licznik * self.mianownik , self.mianownik * other.mianownik)

    def Skracaj(self):
        ...


class SuperInt(int):
    def __init__(self,val):
        self = val
    def isPrime(self):
        return True
    
class SuperStr(str):
    def __init__(self,val):
        self = val
    def isPalindrome(self:str):
        return self.lower() == self[::-1].lower()
    

a = SuperInt(3)

print(2*a+5, a.isPrime(), type(a))

a = SuperStr("pot0p")
print(a.isPalindrome())

a = Ulamek(3,4,"A")
b = Ulamek(2,5,"B")


print(a, float(a),sep=", ")
print(b, float(b),sep=", ")

print(a * b)
print(a + b)
