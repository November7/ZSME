zmienna_1 = 1234
zmienna_2 = 213.4
zmienna_3 = "123.4"
zmienna_4 = 1 > 2
 
print(zmienna_1, zmienna_2, zmienna_3, zmienna_4)
print(id(zmienna_1), id(zmienna_2), id(zmienna_3), id(zmienna_4))
print(type(zmienna_1), type(zmienna_2), type(zmienna_3), type(zmienna_4))
 
zmienna_5 = zmienna_1 #Kopia czy referencja?
 
print(zmienna_1, zmienna_5)
print(id(zmienna_1), id(zmienna_5))
print(type(zmienna_1), type(zmienna_5))
 
zmienna_5 += 10 #Co z oryginałem?
 
print(zmienna_1, zmienna_5)
print(id(zmienna_1), id(zmienna_5))
print(type(zmienna_1), type(zmienna_5))
