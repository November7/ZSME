class CExample:
    def __init__(self, attrib):
        self.attrib = attrib

    def __str__(self):
        return f"{self.attrib}"

    def __int__(self):
        return int(self.attrib)

    def __float__(self):
        return float(self.attrib)
 
 
a = CExample(123)
 
print(a) # automatyczne wywołanie metody __str__
print(str(a)) # jawne wywołanie metody __str__
print(int(a)) # jawne wywołanie metody __int__
print(float(a)) # jawne wywołanie metody __float__
