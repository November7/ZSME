class Fraction:
    def __init__(self,num = 0, den = 1): # konstruktor
        self.num = num
        if den == 0:
            self.__den = 1
        else: 
            self.__den = den
    
    #getter
    def den(self):
        return self.__den
    
    #setter
    def setden(self, val):
        if val != 0:
            self.__den = val

    def __str__(self):  # Fraction -> string
        return f'{self.num} / {self.__den}'
    
    def __float__(self):  # Fraction -> float
        if self.__den == 0:
            return 0.0
        return self.num / self.__den
    
    def __add__(self, other):        
        return Fraction(self.num * other.__den + other.num * self.__den, self.__den * other.__den)


    def __sub__(self, other): #odejmowanie
        return None
    
    def __mul__(self, other): #mnożenie
        return None
    
    def __truediv__(self, other): #dzielenie /
        return None

a = Fraction(1,2)
b = Fraction(3,4)

a.setden(123)


print(f'{a}, {b}')
print(f'{float(a)}, {float(b)}')

print(a + b)
