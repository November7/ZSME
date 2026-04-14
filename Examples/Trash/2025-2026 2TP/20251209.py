# wyjątki

def getInt(prompt:str, strError:str, nTries:int = 3) -> int:
    i = 0
    while i < nTries:
        try:
            return int(input(prompt))            
        except:
            print(strError)
            i+=1    
    return None


x = getInt("Podaj liczbę: ","Nieprawidłowa wartość", 2)
y = getInt("Podaj liczbę: ","Nieprawidłowa wartość")

if x == None or y == None:
    exit(12321)

print(f'{x} {y}')
    
        






