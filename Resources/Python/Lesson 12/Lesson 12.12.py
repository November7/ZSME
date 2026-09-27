with open('plik.txt', 'r', encoding='utf-8') as file:
    #odczyt całego pliku
    content = file.read()
    print(content, end='')
 
    file.seek(0) #ustawienie 'wskaźnika' w pliku na początek
 
    # odczyt znak po znaku
    while True:
        f = file.read(1)
        if not f: break
        print(f, end='')
 
    file.seek(0) #ustawienie 'wskaźnika' w pliku na początek
 
    # odczyt linia po linii    
    while True:
        line = file.readline()
        if len(line) == 0: break
        print(line, end='')
 
    file.seek(0) #ustawienie 'wskaźnika' w pliku na początek
 
    # odczyt linia po linii
    for line in file:
        print(line, end='')
 
    file.seek(0) #ustawienie 'wskaźnika' w pliku na początek
 
    #odczyt wszystkich linii i umieszczenie ich w liście
    lines = file.readlines()
    print(lines)
 
with open('out.txt', 'w', encoding="utf-8") as file:
    tekst = "jakiś przykładowy tekst"
    file.write(tekst)
    file.writelines(["tekst 1", "tekst 2", "tekst3"])
