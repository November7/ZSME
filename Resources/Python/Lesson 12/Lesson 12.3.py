# Odczyt i zapis plikow tekstowych

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Pierwsza linia\nDruga linia\n")

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
