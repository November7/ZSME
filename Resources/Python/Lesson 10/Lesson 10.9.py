class CExample:
    def __init__(self): # definicja konstruktora
        self.attr = 0 # przykładowy atrybut
 
    def Print(self):     # zwykła metoda
        print(self.attr)

    def Hi(argument): # błędna definicja metody statycznej (interpreter nie zwróci błędu, ponieważ uzna ją za zwykłą metodę)
        print("Hi", argument)
 
a = CExample()
a.Print()
 
 
a.Hi() # instancja a zostaje automatycznie przekazana jako argument
CExample.Hi("Jan") # wywołanie funkcji przez klasę z jawnym argumentem; brak @staticmethod
