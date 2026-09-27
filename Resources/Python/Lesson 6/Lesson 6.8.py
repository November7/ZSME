lista = [1,2,3,4,5,6,7] #działa dla wszystkich typów agregacyjnych: (), [], {}
 
a, b, *reszta, c, d = lista
 
print(a, b, c, d, reszta, sep="\n")
 
pierwszy, *tmp, ostatni = lista
 
print(pierwszy, ostatni)
