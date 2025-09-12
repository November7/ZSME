def GetInt(comment, error = 'Nieprawidłowa wartość!'):
    while True:
        try:
            val = int(input(comment))
            return val
        except:
            print(error)

x = False
y = False

while True:
    print('Menu:')
    print('0: Wyjście  z programu [spacja]')
    print('1: Wprowadzenie argumentów [@]')
    print('2: Dodawanie [+]')
 

    key = input('Wyierz opcję: ')
    if key == '0' or key == ' ':
        print('Bye Bye!')
        break
    elif key == '1' or key == '@':
        x = GetInt('Wporwadź wartość x: ')
        y = GetInt('Wporwadź wartość y: ')
    elif key == '2' or key == '+':
        if x == False or y == False:
            print('Ustaw wartość zmiennych!!')
        else:
            print(f'Suma {x} oraz {y} wynosi {x + y}')
    elif key == '3' or key == '-':
        if x == False or y == False:
             print('Ustaw wartość zmiennych!!')
        else:
            ...

    else:
        print('Nieprawidłowa opcja z menu!')
    







