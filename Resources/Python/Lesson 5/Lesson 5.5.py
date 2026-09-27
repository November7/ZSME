Krotka = (1,2,3,1,3,2,-1,"tekst") #definicja krotki
 
print(Krotka)
print("-----------------")
i = 0
n = len(Krotka)
 
#Wypisanie elementów listy za pomocą pętli while
while i<n:
  print(Krotka[i],end=", ")
  i+=1
 
print("\n-----------------")
 
#Wypisanie elementów listy za pomocą pętli for
 
for element in Krotka:
  print(element,end=", ")
 
print("\n-----------------")  
 
#Modyfikacja zawoartości elementów krotki nie jest możliwe, próba zakończy się błędem:
 
# Krotka[0] = 321
# Krotka[1] = "dwa"
