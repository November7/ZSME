
#ścieżka bezwzględna
# file = open("D:/Marcin/Source/ZSME/Examples/2025-2026 2TP/plik.txt", "r")

#ściezka względna
# file = open(".\\Examples\\2025-2026 2TP\\plik.txt", "r")
# file = open("./Examples/2025-2026 2TP/plik.txt", "r")


# file = open(r"./Examples\2025-2026 2TP\plik.txt", "r")




with open(r"./Examples\2025-2026 2TP\plik.txt", "r") as file1, \
     open(r"./Examples\2025-2026 2TP\plik2.txt", "w") as file2:
    ...
    while True:
        line = file1.readline()
        if not line: break

        line = line.strip()
        try:
            liczba = int(line)
            print(liczba)
            if liczba % 2 == 0:
                file2.write(f'{liczba}\n')
        except:
            ...