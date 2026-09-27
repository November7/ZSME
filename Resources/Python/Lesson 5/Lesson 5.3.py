Lista = [1,2,3,1,3,2,-1,"tekst"] #definicja listy
 
print(Lista)
print("-----------------")
i = 0
n = len(Lista)
 
#Wypisanie elementów listy za pomocą pętli while
while i<n:
  print(Lista[i],end=", ")
  i+=1
 
print("\n-----------------")
 
#Wypisanie elementów listy za pomocą pętli for
 
for element in Lista:
  print(element,end=", ")
 
print("\n-----------------")  
 
#Modyfikacja zawoartości elementów:
 
Lista[0] = 321
Lista[1] = "dwa"
 
print(Lista)
