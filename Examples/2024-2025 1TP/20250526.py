tekst = "jakiś tekst"
lista = [2,34,5,6,3,3,4,65,7]
krotka = (2,34,5,6,3,3,4,65,7)
zestaw = {2,34,5,6,3,3,4,65,7,7,7,7,7}
miesiace = {"styczeń":31, "luty":28, "marzec":31, 0:"test1", "0":"test2"}




ob_i = miesiace

# for element in ob_i:
#     print(element)

# i = 0
# while i < len(ob_i):
#     print(ob_i[i])
#     i+=1


# print(tekst[5]) #ok
# print(lista[5]) #ok 
# print(krotka[5]) #ok
# print(zestaw[5]) #err
print(miesiace["0"])

# tekst[0] = "J" #err
# lista[0] = "J" #ok
# krotka[0] = "J" #err
# lista.append("34444") #ok

zestaw.add(9)
zestaw.add(65)
zestaw.remove(65)

print(f"{tekst = },\n{lista = },\n{krotka = }\n{zestaw = }")