def checkPESEL(pesel):

    if len(pesel) != 11: return False
    try:
        int(pesel)
    except:
        return False
    intMonth = int(pesel[2:4]) #<2, 4)
    month = int(intMonth) % 20    
    if month < 1 or month > 12: return False
    offset = (intMonth - month) // 20
    century = [19,20,21,22,18]
    try:
        century = 100 * century[offset]        
    except:
        return False
    rokprzestepny = False
    intYear = int(pesel[:2]) + century
    # rok przestępny  # rokprzestepny = True    
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if rokprzestepny:
        days[2] = 29  
    intDay = int(pesel[4:6])
    if intDay < 1 or intDay > days[month]: return False  
    weights = [1,3,7,9,1,3,7,9,1,3]
    sum = 0
    for c, w in zip(pesel, weights):
        sum += w * int(c)
    sum = (10 - sum % 10) % 10
    if int(pesel[-1]) != sum: return False
    return True


dane = ['123445-567', '12345678901', '10242912913','11242912913','44051401359']

for p in dane:
    print(f'{p}: {checkPESEL(p)}')