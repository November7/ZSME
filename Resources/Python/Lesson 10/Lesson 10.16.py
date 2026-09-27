class CFraction:
    def __init__(self,nom,denom):
        self.nominator = nom
        self.denominator = denom
 
    def __str__(self):
        return f"{self.nominator} / {self.denominator}"
    
    def __float__(self):
        return float(self.nominator / self.denominator)
    
    def __mul__(self,other):   # operator mnożenia: * 
        return CFraction(self.nominator * other.nominator, self.denominator * other.denominator) 
    
    def __imul__(self,other):  # operator przypisania i mnożenia: *=
        return CFraction(self.nominator * other.nominator, self.denominator * other.denominator) 
    
    def __neg__(self):                
        return CFraction( -self.nominator, self.denominator)
    
 
a = CFraction(1,2) 
b = CFraction(3,4) 
 
print(a, float(a), sep=",\t") # 1 / 2, 0.5 
print(b, float(b), sep=",\t") # 3 / 4, 0.75
 
c = a * b
print(c, float(c), sep=",\t") # 3 / 8, 0.375
 
c *= b
print(c, float(c), sep=",\t") # 9 / 32, 0.28125
 
print(-c, float(-c), sep=",\t") # -9 / 32, -0.28125
