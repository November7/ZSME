#dekoratory
import time
def timer(f_dek):
    def f_wew(*args, **kwargs):
        t1 = time.time()
        ret = f_dek(*args, **kwargs)

        t2 = time.time()
        print(f'Czas wywołania funkcji {t2 - t1}')

        return ret    
    return f_wew

dane = [i for i in range(10_000_000)]
@timer
def suma_elementow1(ob):
    s = 0
    for el in ob:
        s += el
    return s

@timer
def suma_elementow2(ob):
    s = 0
    for i in range(len(ob)):
        s += ob[i]
    return s

@timer
def suma_elementow3(ob):
    s = 0
    i = 0
    n = len(ob)
    while i < n:
        s += ob[i]
        i += 1
    return s

print(suma_elementow1(dane))
print(suma_elementow2(dane))
print(suma_elementow3(dane))


