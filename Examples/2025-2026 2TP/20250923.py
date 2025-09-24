

a = int(input("Podaj dlugość 1 boku: "))
b = int(input("Podaj dlugość 2 boku: "))
c = int(input("Podaj dlugość 3 boku: "))

print(f"Podałeś {a = }, {b = }, {c = }")

if a + b > c and a + c > b and b + c > a:
    # print("Z podanych długości można zbudowac trójkąt!")
    if a == b and b == c:
        print("Trójkąt równoboczny")
    elif a == b or a == c or b == c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")

    a2 = a * a
    b2 = b * b
    c2 = c * c

    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        print("Trójkąt prostokątny")
    elif a2 + b2 < c2 or a2 + c2 < b2 or b2 + c2 < a2:
        print("Trójkąt rozwartokątny")
    else:
        print("Trójkąt ostrokątny")

else:
    print("Z podanych długości nie można zbudowac trójkąta!")
    

