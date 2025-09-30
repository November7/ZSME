a = int(input("Podaj długość boku: "))
b = int(input("Podaj długość boku: "))
c = int(input("Podaj długość boku: "))

if a + b > c and a + c > b and c + b > a:
    print("Można zbudować trójkąt")

    


else:
    print("Nie można zbudować trójkąta")
