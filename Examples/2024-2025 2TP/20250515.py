def parseIP(strAddress):
    strAddress = strAddress.replace(' ', '')
    parts = strAddress.split('.')        
    try:
        parts = [int(part) for part in parts]
    except:
        return False
    return parts

def isValidIP(ipAddress):
    if not isinstance(ipAddress, list) or len(ipAddress) != 4:
        return False
    
    for part in ipAddress:
        if not isinstance(part, int) or not 0 <= part <= 255:
            return False
    return True


def isValidSubnetMask(subnetMask):
    if isValidIP(subnetMask) == False:
        return False
    ...

def classIP(ipAddress):
    if isValidIP(ipAddress) == False:
        return False
    
    if ipAddress[0] < 128:
        return 'A'
    elif ipAddress[0] < 192:
        return 'B'
    elif ipAddress[0] < 224:
        return 'C'
    elif ipAddress[0] < 240:
        return 'D'
    else:
        return 'E'

def extInfoIP(ipAddress):
    if isValidIP(ipAddress) == False:
        return False
    
    if ipAddress[0] == 0:
        return 'Zarezerwowana pula adresów'
    elif ipAddress[0] == 127:
        return 'Adres pętli zwrotnej (loopback)'
    elif ipAddress[0] == 10 or ipAddress[0] == 192 and ipAddress[1] == 168 or ipAddress[0] == 172 and 16 <= ipAddress[1] <= 31:
        return 'Adres z puli prywatnej'
    elif ipAddress[0] == 169 and ipAddress[1] == 254:
        return 'Aders protokołu APIPA (Automatic Private IP Addressing)'
    elif ipAddress[0] == 255 and ipAddress[1] == 255 and ipAddress[2] == 255 and ipAddress[3] == 255:
        return 'Globalny adres rozgłoszeniowy (broadcast)'
    return 'Adres publiczny'

def calcSubnets(ipAddress, subnetMask):
    ...

def main():
    while True:
        ipAddress = input('Wprowadź adres IPv4 (lub q żeby zakończyć): ')
        if ipAddress.lower() == 'q':
            break
        
        parsedipAddress = parseIP(ipAddress)
        
        if isValidIP(parsedipAddress) == False:
            print('Adres IP jest nieprawidłowy')
        else:   
        
            print(f'Adres IPv4: {ipAddress}')
            print(f'Klasa adresu: {classIP(parsedipAddress)}')
            print(f'Dodatkowe informacje: {extInfoIP(parsedipAddress)}')
            print()



main()