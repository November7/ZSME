def funkcja(a, b, c):
    print(f'{a = } {b = } {c = }')

# funkcja(111, 222, 333)
# funkcja(111, 222, c = 333)
# # funkcja(a = 111, 222, 333) #źle, najpierw pozycyjne potem nazwane (key-args)
# funkcja(b = 222, a = 111, c = 333)


def suma(*arg):
    s = 0
    for el in arg:
        s += el

    return s

def srednia(*arg):
    n = len(arg) 
    if n == 0:
        return None
    return suma(*arg) / n

print(suma(3,4,5,6,7,3))
print(srednia(3,4,5,6,7,3))

lista = [3,4,6,2,4]

a,b,*c = lista

print(a,b,c)









