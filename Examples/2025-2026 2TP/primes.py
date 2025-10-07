def isPrime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2,int(number**0.5)):
        if number % i == 0:
            return False
        
    return True


for liczba in range(100000):
    if isPrime(liczba) == True:
        print(liczba,end=', ')