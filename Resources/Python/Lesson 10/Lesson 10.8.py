class CExample:
    def __init__(self): # definicja konstruktora
        self.attr = 0 # przykładowy atrybut
    
    def Print(self):     # zwykła metoda
        print(self.attr) 
 
    def Hello(): # celowo bez self i @staticmethod: wywołanie przez instancję zgłosi błąd
        print("hello")
 
a = CExample()
a.Print()
 
#a.Hello() # nieprawidłowe użycie metody Hello!
CExample.Hello()
