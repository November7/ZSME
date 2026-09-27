import time,sys
 
Lista = ["a","b","c",1,2,3]
Krotka = ("a","b","c",1,2,3)
 
print("Rozmiar listy:", sys.getsizeof(Lista))
print("Rozmiar krotki:",sys.getsizeof(Krotka))
 
 
bigNumber = 100000 # umiarkowana liczba elementów do ćwiczenia
Lista = list(range(bigNumber))
Krotka = tuple(range(bigNumber))
 
 
i = 0
n = len(Lista)
start = time.time()
while i<n:
    x = Lista[i]
    i+=1
stop = time.time()
 
print("Czas dostępu do kolejnych elementów Listy:",stop - start)
 
 
i = 0
n = len(Krotka)
start = time.time()
while i<n:
    x = Krotka[i]
    i+=1
stop = time.time()
 
print("Czas dostępu do kolejnych elementów Krotki:",stop - start)
