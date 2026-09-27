class CExample:
    def __init__(self): # definicja konstruktora
        self.attr = 0 # przykładowy atrybut
 
    def Print(self):     # zwykła metoda
        print(self.attr) 
 
    @staticmethod
    def Hi(argument): # poprawna definicja metody statycznej
        print("Hi",argument)
 
a = CExample()
a.Print()
 
#a.Hi() # nieprawidłowe użycie metody Hi! 
a.Hi("ddd") # poprawne wywołanie metody statycznej przez instancję
CExample.Hi("ddd") #prawidłowe użycie metody statycznej Hi
