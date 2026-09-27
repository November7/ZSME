#1. Wypisanie pojedynczego tekstu
print("\n ---------- Przykład 1 ------------")
print("Hello World!") 
 
#2. Wypisanie kilku tekstów jako osobne argumenty funkcji
print("\n ---------- Przykład 2 ------------")
print("Hello","World!")
 
#3. Kilkukrotne użycie funkcji print:
print("\n ---------- Przykład 3 ------------")
print("Hello")
print("World!")
 
#3a Określenie znaku końca linii (domyślnie przejście do nowej linii):
print("\n ---------- Przykład 3a -----------")
print("Hello", end=" ") #po wypisaniu Hello powinna pojawić się spacja zamiast domyślnego znaku nowej linii
print("World!")
 
#3b Określenie separatora argumentów (domyślnie spacja):
print("\n ---------- Przykład 3b -----------")
print("Hello", "World", sep=" : ") #nowy separator: spacja, dwukropek i spacja
 
#4. Użycie specjalnego znaku sterującego określającego nową linię: \n
print("\n ---------- Przykład 4 ------------")
print("Hello\n\n\nWorld!\n\n\n")
