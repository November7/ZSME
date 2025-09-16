tekst = "jakiś tekst"
lista = [1,2,34,5,'fdsfdsfsd',76,7,3]
krotka = (1,2,34,5,'fdsfdsfsd',76,7,3) 
zestaw = {7,3,34,5,'fdsfdsfsd',76,7,3}

aggr = zestaw

print(aggr)

for literka in aggr:
    print(literka,end=", ")

print()
# i = 0
# n = len(aggr)
# while i < n:
#     print(aggr[i],end=', ')
#     i+=1

print()
# print(aggr[0])
# print(aggr[-1])
# aggr[0] = 'J'

zestaw.add(5)

print(zestaw)