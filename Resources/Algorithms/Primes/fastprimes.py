# wersja z optymalizacją, sprawdzane tylko do pierwiastka z 'num' i tylko dzielniki pierwsze
import time 

timeup = 10  # czas działania programu w sekundach
start = time.time()
count = 0
num = 3  # pierwsza liczba do sprawdzenia
primes = [2,]
dzielnik = 2
print(f'Szukam liczb pierwszych przez {timeup} sekund...')
endTime = start + timeup

while time.time() < endTime:        
    sqrtNum = int(num**0.5)
    it = iter(primes)

    isPrime = True
    dzielnik = 2
    while dzielnik <= sqrtNum:
        dzielnik = next(it)        
        if num % dzielnik == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
        count += 1

    num += 2  # pomijamy parzyste

print(f'Znaleziono {count} liczb pierwszych w czasie {timeup} sekund.')