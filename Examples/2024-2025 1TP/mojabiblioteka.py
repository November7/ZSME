# Czy z podanyc boków (a,b,c) można stworzyć trójkąt 

def isTriangle(a:int, b:int, c:int) -> bool:
    if a + b > c and a + c > b and b + c > a: 
        return True
    else:
        return False
    # return (a + b > c and a + c > b and b + c > a)



def isPalindrome(text:str) -> bool:
    # if text == text[::-1]: 
    #     return True
    # else:
    #     return False
    
    i = 0
    rozmiar = len(text)

    while i < rozmiar // 2:
        if text[i] != text[rozmiar - i - 1]:
            return False
        i += 1
    return True

    
def isPrime(number:int) -> bool:
    if number < 2: 
        return False
    
    sqrtNumber = int(number ** 0.5)
    for dzielniki in range(2, sqrtNumber + 1):
        if number % dzielniki == 0:
            return False
    return True


def factorize(number:int) -> []:
    sqrtNumber = int(number ** 0.5)   
    ret = []
    dzielnik = 2
    while dzielnik <= sqrtNumber:
        if number % dzielnik == 0:
            ret.append(dzielnik)
            number //= dzielnik
        else:
            dzielnik += 1

    if number>1: 
        ret.append(number)
    return ret
    
def isPythagoras(a,b,c) -> bool:
    if a * a + b * b == c * c or c * c + b * b == a * a or a * a + c * c == b * b:
        return True
    else:
        return False