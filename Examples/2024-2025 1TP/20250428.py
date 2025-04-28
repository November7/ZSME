#zadanie 1: Napisz program wyświetlający wizytówkę (imię i nazwisko podane z klawiatury).

# imie = input("Podaj imię: ")
# nazwisko = input("Podaj nazwisko: ")
# print("Wizytówka:")
# print("Imię:", imie)    
# print("Nazwisko:", nazwisko)

#zadanie 2: Uzupełnij poprzedni program w taki sposób aby imię i nazwisko było z wielkiej litery (użyj metody capitalize() obiektu typu string)

# imie = input("Podaj imię: ").capitalize()
# nazwisko = input("Podaj nazwisko: ").capitalize()
# print("Wizytówka:")
# print("Imię:", imie)
# print("Nazwisko:", nazwisko)

#Zadanie 3: Napisz program, który wyświetla liczby z zakresu 〈𝑎, 𝑏) ze skokiem c, gdzie a, b i c podane są z klawiatury, a<b i c≥1 oraz a, b, c są całkowite np. 3, 7, 11, 15, 

# try:
#     a = int(input("Podaj a: "))
#     b = int(input("Podaj b: ")) 
#     c = int(input("Podaj c: "))

#     if a < b and c >= 1:
#         for i in range(a, b, c):
#             print(i,end=", ")
#     else:
#         print("Błędne dane. Upewnij się, że a < b i c >= 1.")

# except ValueError:
#     print("Błędne dane. Upewnij się, że podałeś liczby całkowite.")


#Zadanie 4: Napisz program, który wyświetla liczby z zakresu 〈𝑎, 𝑏) ze skokiem c, gdzie a, b i c podane są z klawiatury, a>b i c≥1 oraz a, b, c są całkowite np. 15, 13, 11, 9, …

# try:
#     a = int(input("Podaj a: "))
#     b = int(input("Podaj b: ")) 
#     c = int(input("Podaj c: "))

#     if a > b and c >= 1:
#         for i in range(a, b, -c):
#             print(i, end=", ")
#     else:
#         print("Błędne dane. Upewnij się, że a > b i c >= 1.")   
# except ValueError:
#     print("Błędne dane. Upewnij się, że podałeś liczby całkowite.")

#zadanie 5 Napisz program, który wyświetla liczby z zakresu 〈𝑎, 𝑏) ze skokiem c, gdzie a, b i c podane są z klawiatury, a<b i c>0 oraz a, b, c należą do zbioru liczb rzeczywistych np. 1.0, 1.5, 2.0, 2.5, …

# try:
#     a = float(input("Podaj a: "))
#     b = float(input("Podaj b: ")) 
#     c = float(input("Podaj c: "))

#     if a < b and c > 0:
#         i = a
#         while i < b:
#             print(f"{i:.2f}",end=", ")
#             i += c
#     else:
#         print("Błędne dane. Upewnij się, że a < b i c > 0.")
# except ValueError:  
#     print("Błędne dane. Upewnij się, że podałeś liczby rzeczywiste.")

#zadanie 6: Napisz program wyświetlający datę wprowadzoną z klawiatury w postaci: 2015 10 02 (ze spacjami). Miesiąc powinien wyświetlać się słownie

# try:
#     data = input("Podaj rok miesiąc dzień: ")
#     rok, miesiac, dzien = str(data).split()    
    
#     miesiace = ("","styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień")
#     miesiac = int(miesiac)
#     dzien = int(dzien)
#     if miesiac < 1 or miesiac > 12 or dzien < 1 or dzien > 31:
#         print("Błędny miesiąc lub dzień. Upewnij się, że podałeś miesiąc w zakresie 1-12 a dzień w zakresie 1 - 31.")
#     else:
#         print(f"{rok} {miesiace[miesiac]} {dzien}")
# except ValueError:
#     print("Błędne dane. Upewnij się, że podałeś datę w formacie: rok miesiąc dzień.")

#zadanie 7: Napisz program, który pobiera liczby całkowite z klawiatury, umieszcza je w 10-elementowej liście, a następnie wyświetla tylko wartości z zakresu 〈3, 7)

# dane = []
# for i in range(10):
#     try:
#         liczba = int(input(f"Podaj liczbę całkowitą {i+1}: "))
#         dane.append(liczba)
#     except ValueError:
#         dane.append(0)

# for i in dane:
#     if 3 <= i < 7:
#         print(i, end=", ")
# print()

#zadanie 8 Analogicznie do przykładu 7 napisz program wyświetlający liczby:
# a. parzyste,
# b. podzielne przez 3 i 5 (jednocześnie)
# c. których suma cyfr równa jest 10
# d. pierwsze

#generowanie 20 liczb losowych z zakresu 1 - 100 (inaczej niż w przykładzie 7)
# import random
# dane = [random.randint(1, 1000) for _ in range(20)]

# print("Wylosowane liczby:\n", dane,sep="")
# print("a) Liczby parzyste:")
# for i in dane:
#     if i % 2 == 0:
#         print(i, end=", ")
# print()

# print("b) Liczby podzielne przez 3 i 5:")
# for i in dane:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=", ")
# print()

# print("c) Liczby, których suma cyfr równa się 10:")
# for liczba in dane:
#     cyfry = str(liczba)
#     suma_cyfr = 0
#     for cyfra in cyfry:
#         suma_cyfr += int(cyfra)
#     if suma_cyfr == 10:
#         print(liczba, end=", ")
# print()

# print("d) Liczby pierwsze:")
# for liczba in dane:
#     if liczba > 1:
#         for i in range(2, int(liczba**0.5) + 1):
#             if liczba % i == 0:
#                 break
#         else:
#             print(liczba, end=", ")
# print()

#zadanie 9: Napisz program zawierający funkcję sprawdzającą czy z podanych długości boków można utworzyć trójkąt, 
# a jeżeli tak to jaki jest ten trójkąt:
# a. równoboczny
# b. równoramienny (ale nie równoboczny)
# c. różnoramienny (ale nie prostokątny)
# d. prostokątny
# e. prostokątny równoramienny

# while True:
#     try:
#         a = float(input("Podaj długość boku a: "))
#         b = float(input("Podaj długość boku b: "))
#         c = float(input("Podaj długość boku c: "))
#     except ValueError:
#         print("Błędne dane. Upewnij się, że podałeś liczby rzeczywiste.")
#         continue
#     break

# if a <= 0 or b <= 0 or c <= 0:
#     print("Błędne dane. Długości boków muszą być większe od zera.")
# elif a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Trójkąt jest równoboczny.")
#     elif a == b or a == c or b == c:
#         if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#             print("Trójkąt jest prostokątny równoramienny.")
#         else:
#             print("Trójkąt jest równoramienny.")
#     elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#         print("Trójkąt jest prostokątny.")
#     else:
#         print("Trójkąt jest różnoramienny.")
# else:
#     print("Z podanych długości boków nie można utworzyć trójkąta.")
