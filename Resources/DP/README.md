# Programowanie dynamiczne w C++

[![AI Generated](https://img.shields.io/badge/README-AI%20Generated-4B8BF5?style=flat&logo=githubcopilot&logoColor=white)](#)

Zbiór przykładów programowania dynamicznego w C++, uporządkowanych w 12 rozdziałów i podrozdziały. Katalog prowadzi od rekurencji, memoizacji i tabulacji przez projektowanie stanów i przejść do problemów jednowymiarowych i dwuwymiarowych, plecaka 0/1, LCS, LIS i odległości edycyjnej. Obejmuje także odtwarzanie rozwiązań, optymalizację pamięci oraz rozpoznawanie problemów wymagających DP. Samodzielne programy ilustrują poszczególne zagadnienia i mogą być osadzane w materiałach dydaktycznych, m.in. w Moodle.

1. Wprowadzenie do programowania dynamicznego  
    1.1. [Czym jest DP i kiedy je stosować – minimalna liczba monet](Lesson%201/Lesson%201.1.cpp)  
    1.2. [Nakładające się podproblemy – licznik wywołań](Lesson%201/Lesson%201.2.cpp)  
    1.3. [Optymalna podstruktura – minimalny koszt dojścia](Lesson%201/Lesson%201.3.cpp)  
    1.4. [Brute force, rekurencja i DP – liczba sposobów wejścia po schodach](Lesson%201/Lesson%201.4.cpp)  
2. Rekurencja jako punkt wyjścia  
    2.1. [Rozbijanie problemu – ciąg Fibonacciego](Lesson%202/Lesson%202.1.cpp)  
    2.2. [Drzewo wywołań](Lesson%202/Lesson%202.2.cpp)  
    2.3. [Koszt wielokrotnego obliczania tych samych wartości](Lesson%202/Lesson%202.3.cpp)  
3. Memoizacja – podejście top-down  
    3.1. [Rekurencja z pamięcią – wektor wyników](Lesson%203/Lesson%203.1.cpp)  
    3.2. [Oznaczanie nieobliczonych stanów – osobna tablica](Lesson%203/Lesson%203.2.cpp)  
    3.3. [Analiza złożoności – liczba obliczonych stanów](Lesson%203/Lesson%203.3.cpp)  
4. Tabulacja – podejście bottom-up  
    4.1. [Budowanie rozwiązania od najmniejszych podproblemów](Lesson%204/Lesson%204.1.cpp)  
    4.2. [Wyznaczanie kolejności obliczeń – koszt od końca](Lesson%204/Lesson%204.2.cpp)  
    4.3. [Porównanie memoizacji i tabulacji](Lesson%204/Lesson%204.3.cpp)  
5. Projektowanie rozwiązania DP  
    5.1. [Określenie stanu DP – liczba sposobów dotarcia na stopień](Lesson%205/Lesson%205.1.cpp)  
    5.2. [Przypadki bazowe – pusty problem i pierwszy stopień](Lesson%205/Lesson%205.2.cpp)  
    5.3. [Przejścia między stanami – dozwolone długości skoków](Lesson%205/Lesson%205.3.cpp)  
    5.4. [Kolejność obliczeń – zależności między stanami](Lesson%205/Lesson%205.4.cpp)  
    5.5. [Odczytanie wyniku – stany nieosiągalne](Lesson%205/Lesson%205.5.cpp)  
6. DP jednowymiarowe  
    6.1. [Fibonacci](Lesson%206/Lesson%206.1.cpp)  
    6.2. [Liczba sposobów wejścia po schodach](Lesson%206/Lesson%206.2.cpp)  
    6.3. [Minimalny koszt dotarcia do celu](Lesson%206/Lesson%206.3.cpp)  
    6.4. [Maksymalna suma bez wybierania sąsiednich elementów](Lesson%206/Lesson%206.4.cpp)  
    6.5. [Coin Change – minimalna liczba monet](Lesson%206/Lesson%206.5.cpp)  
    6.6. [Coin Change – liczba kombinacji monet](Lesson%206/Lesson%206.6.cpp)  
7. Odtwarzanie rozwiązania  
    7.1. [Zapamiętywanie poprzednich stanów – wybrane monety](Lesson%207/Lesson%207.1.cpp)  
    7.2. [Odtwarzanie ścieżki o minimalnym koszcie](Lesson%207/Lesson%207.2.cpp)  
    7.3. [Odtwarzanie wybranych niesąsiednich elementów](Lesson%207/Lesson%207.3.cpp)  
8. DP dwuwymiarowe  
    8.1. [Tablica dp[i][j] i liczba ścieżek w siatce](Lesson%208/Lesson%208.1.cpp)  
    8.2. [Minimalny koszt przejścia przez planszę](Lesson%208/Lesson%208.2.cpp)  
    8.3. [Przeszkody i ograniczenia na planszy](Lesson%208/Lesson%208.3.cpp)  
9. Problem plecakowy 0/1  
    9.1. [Modelowanie problemu – wybór biorę / nie biorę](Lesson%209/Lesson%209.1.cpp)  
    9.2. [Stan dp[i][w] – wersja 2D](Lesson%209/Lesson%209.2.cpp)  
    9.3. [Optymalizacja pamięci do 1D](Lesson%209/Lesson%209.3.cpp)  
    9.4. [Odtwarzanie przedmiotów w plecaku](Lesson%209/Lesson%209.4.cpp)  
10. Problemy na ciągach i napisach  
    10.1. [Najdłuższy wspólny podciąg (LCS)](Lesson%2010/Lesson%2010.1.cpp)  
    10.2. [Najdłuższy rosnący podciąg (LIS)](Lesson%2010/Lesson%2010.2.cpp)  
    10.3. [Odległość edycyjna](Lesson%2010/Lesson%2010.3.cpp)  
    10.4. [Podział ciągu na podproblemy – mnożenie łańcucha macierzy](Lesson%2010/Lesson%2010.4.cpp)  
11. Optymalizacja pamięci  
    11.1. [Kiedy nie potrzeba całej tablicy – Fibonacci w O(1) pamięci](Lesson%2011/Lesson%2011.1.cpp)  
    11.2. [Poprzedni i bieżący wiersz – LCS w O(m) pamięci](Lesson%2011/Lesson%2011.2.cpp)  
    11.3. [Siatka – redukcja pamięci z O(n²) do O(n)](Lesson%2011/Lesson%2011.3.cpp)  
    11.4. [Odległość edycyjna – jeden wiersz i poprzednia przekątna](Lesson%2011/Lesson%2011.4.cpp)  
12. Rozpoznawanie problemów DP  
    12.1. [Znajdowanie stanu i przejścia – suma podzbioru](Lesson%2012/Lesson%2012.1.cpp)  
    12.2. [DP a algorytm zachłanny – kontrprzykład dla monet](Lesson%2012/Lesson%2012.2.cpp)  
    12.3. [DP a divide and conquer – niezależne i nakładające się podproblemy](Lesson%2012/Lesson%2012.3.cpp)  
    12.4. [Typowe błędy – kierunek pętli w plecaku 0/1](Lesson%2012/Lesson%2012.4.cpp)  
    12.5. [Typowe błędy – kombinacje a kolejność monet](Lesson%2012/Lesson%2012.5.cpp)  
    12.6. [Przypadki brzegowe – baza, nieosiągalny cel i puste dane](Lesson%2012/Lesson%2012.6.cpp)  

Każdy plik `.cpp` jest samodzielnym programem z własną funkcją `main`. Przykłady korzystają z C++17, a dane wejściowe są zapisane w kodzie. Opisy lekcji znajdują się poza plikami źródłowymi.