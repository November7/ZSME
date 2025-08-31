
def suma(lista):
    s = 0
    for el in lista:
        s += el
    return s


file = open("./Examples/2024-2025 1TP/dane.txt","r")

linie = file.readlines()
dane = []
for linia in linie:
    try:
        liczba = int(linia.strip())
        dane.append(liczba)
    except:
        print("Niewłaściwe dane!")
        ...
        
file.close()

print(dane)

# file = open("./Examples/2024-2025 1TP/wyniki.txt","w")
# s = suma(dane)
# file.write(f"suma elementow wynosi {s}")
# file.close()

with open("./Examples/2024-2025 1TP/wyniki.txt","w") as file:
    s = suma(dane)
    file.write(f"suma elementow wynosi {s}")
