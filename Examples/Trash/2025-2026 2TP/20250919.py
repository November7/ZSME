# przykłady typów agregacyjnych

text = 'Ala ma kota'
lista = ['a','l',123,[2,3,4],{1,2,3},"ala ma kota"]
krotka = ('a','l',123,[2,3,4],{1,2,3},"ala ma kota")
zestaw = {'a','l',123,5,5,5,5,5,6,6,6,6,"ala ma kota"}

slownik = {0: 123, 1: 321, '1': 124, 'test': 'tekst', 1.5:'real'}

print(slownik)

slownik[0] = 333

for keys in slownik:
    print(keys, slownik[keys])

print(slownik[1.5])

slownik['1.5'] = 'nowa'

print(slownik)