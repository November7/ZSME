sudoku = []
with open('./Examples/2024-2025 2TP/sudoku.txt', 'r') as plik:
    while True:
        line = plik.readline()
        if not line:
            break
        row = list(map(int,line.split(" ")))
        
        sudoku.append(row)
        

    # print(row)

print(sudoku)