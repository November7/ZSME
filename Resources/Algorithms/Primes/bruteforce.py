# wersja bez optymalizacji, brute force
import time 

timeup = 10  # czas działania programu w sekundach
start = time.time()
count = 0
num = 2  # pierwsza liczba do sprawdzenia
print(f'Szukam liczb pierwszych przez {timeup} sekund...')
endTime = start + timeup
while time.time() < endTime:    
    for dzielnik in range(2, num): #sprawdź wszystkie dzielniki liczby 'num'
        if num % dzielnik == 0: # jeśli 'num' jest podzielne przez 'dzielnik'            
            break
    else:  # pętla zakończyła się bez 'break', więc liczba jest pierwsza
        # print(num) # odkomentuj, aby wyświetlić znalezione liczby pierwsze
        count += 1
    num += 1

print(f'Znaleziono {count} liczb pierwszych w czasie {timeup} sekund.')