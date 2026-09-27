# wersja z optymalizacją, sprawdzane tylko do pierwiastka z 'num' i tylko dzielniki pierwsze
import time 

timeup = 10  # czas działania programu w sekundach
start = time.time()
count = 0
num = 3  # pierwsza liczba do sprawdzenia 
primes = [2, ]
dzielnik = 2
print(f'Szukam liczb pierwszych przez {timeup} sekund...')
endTime = start + timeup
while time.time() < endTime:        
    sqrtNum = int(num**0.5)
    isPrime = True
    for dzielnik in primes: #sprawdź wszystkie dzielniki  pierwsze mniejsze od pierwiastek z 'num' liczby 'num'        
        if dzielnik > sqrtNum:
            break
        if num % dzielnik == 0: # jeśli 'num' jest podzielne przez 'dzielnik' 
            isPrime = False
            break
    if isPrime:  # pętla zakończyła się bez 'break', więc liczba jest pierwsza
        primes.append(num)
        # print(num) # odkomentuj, aby wyświetlić znalezione liczby pierwsze
        count += 1
    num += 2 # pomijamy parzyste

print(f'Znaleziono {count} liczb pierwszych w czasie {timeup} sekund.')