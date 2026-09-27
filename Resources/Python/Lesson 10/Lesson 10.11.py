class Osoba:
    def __init__(self,imie,nazwisko) -> None:
        self.pesel = ""
        self.imie = imie
        self.nazwisko = nazwisko
    def Wypisz(self):
        print(f"{self.imie} {self.nazwisko} {self.pesel if self.pesel!='' else '' }")
 
    def wprowadzPesel(self,pesel):
        if Osoba.sprawdzPesel(pesel): # Wywołanie metody statycznej
            self.pesel = pesel
 
    @staticmethod
    def czyRokPrzestepny(rok):
        if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0): return True
        else: return False
 
    @staticmethod
    def sprawdzPesel(pesel):
        pesel = str(pesel)
        if len(pesel) != 11: return False
        if not all("0" <= znak <= "9" for znak in pesel): return False
        sum = 0
        w = [1,3,7,9,1,3,7,9,1,3]        
        for s,i in zip(pesel[:10],range(10)):
            if s < '0' or s > '9': return False
            sum += w[i]*int(s)
        sum = (10 - sum % 10) % 10        
        if sum != int(pesel[-1]): return False
        
        d = [31,28,31,30,31,30,31,31,30,31,30,31]
        rr = int(pesel[0:2])
        mm = int(pesel[2:4])
        dd = int(pesel[4:6])
        
        cent = (1 + mm // 20) % 5 
        mm %= 20 
 
        rrrr = 1800 + 100 * cent + rr
 
        if Osoba.czyRokPrzestepny(rrrr): # Wywołanie metody statycznej
            d[1] = 29
 
        if mm < 1 or mm > 12: return False
        if dd < 1 or dd > d[mm - 1]: return False
 
        return True
    
a = Osoba("Jan","Nowak")
a.wprowadzPesel("44051401458")
 
print(Osoba.sprawdzPesel("44051401458")) #Wywołanie metody statycznej
print(Osoba.czyRokPrzestepny(2000)) # Wywołanie metody statycznej
print(Osoba.czyRokPrzestepny(2024)) # Wywołanie metody statycznej
print(Osoba.czyRokPrzestepny(2022)) # Wywołanie metody statycznej
 
a.Wypisz()
