
def load(path):

    screen = []
    with open(path, 'r') as plik:
        while True:
            line = plik.readline()
            if not line:
                break
            row = list(map(int,line.split(" ")))
            
            screen.append(row)
    return screen        

def draw(screen):
    for row in screen:
        for el in row:
            if el != 0: print(f"\033[1;32m{el}\033[0m", end=" ")
            else: print(f"{el}", end=" ")
        print()

def duplicates(part):
    w = [0] * 9
    for i in part:
        if i > 0 and i <10: 
            if w[i-1] !=0:
                return True
            else:
                w[i-1] = 1

def box3x3(screen,x,y):
    box = []
    for j in range(3):
        for i in range(3):
            box.append(screen[y+j][x+i])

    return box

def validate(screen):
    for row in screen:
        if duplicates(row):
            return False
    
    for i in range(9):
        cols = []
        for j in range(9):
            cols.append(screen[j][i])
        if duplicates(cols):
            return False

    for i in range(3):
        for j in range(3):
            if duplicates(box3x3(screen,i,j)):
                return False

        
    return True



plansza = load('./Examples/2024-2025 2TP/sudoku.txt')
draw(plansza)

print(validate(plansza))



