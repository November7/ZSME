#Tworzenie listy / krotki / zestawu za pomocą kontruktora: list / tuple / set
Lista = list(range(100)) #użycie kontruktora - utworzenie listy z elementami od 0 do 99
 
print(Lista)
#Tworzenie listy zawierającej określone elementy
 
Lista = [x for x in range(2,50,3)] #utwórz listę takich wartości x, które należą do zakresu od <2,50) co 3
print(Lista)
 
Lista = [x for x in range(2,200,3) if x%5 == 0] #utwórz listę takich wartości x, które należą do zakresu od <2,200) co 3 i są podzielne przez 5
print(Lista)
