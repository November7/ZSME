Lista = [1, 4, 2, 3, 4, 5, 6, 7, 5, 44] #10 elementów
Krotka = (1, 4, 2, 3, 4, 5, 6, 7, 5, 44)
#Test = Lista
Test = Krotka
 
print(Test[1:8]) #zwraca elementy o indeksach od 1 do 7 włącznie
print(Test[1:8:2]) #zwraca co drugi element listy od 1 do 7 włącznie 
 
#Korzystanie z ujemnych indeksów:
print(Test[-8:-4]) #zwraca elementy listy od 8 elementu od końca do 5 elementu od końca włącznie
 
print(Test[-4:-8:-1]) #zwraca elementy listy od 4 elementu od końca do 7 elementu od końca włącznie
print(Test[6:2:-1]) #zwraca elementy listy od 6 do 3 włącznie

#Przypisywanie wartości do wycinków listy (krotka jest tylko do odczytu!)

print(Lista)
Lista[1:3] = [55, 66] #przypisanie do elementu 1 i 2 wartości odpowiednio: 55 i 66
print(Lista)
