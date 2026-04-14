def wypisz(*pos, **args):
    print("Argumenty pozycyjne")
    for el in pos:
        print(el,end=' ')    
    print()
    print("Argumenty typu key-word")
    for key in args:
        print(f'{key} -> {args[key]}',end=' ')    
    print()

    
    
    

wypisz(3,4,5,6,7,87,a=2, b=3)

