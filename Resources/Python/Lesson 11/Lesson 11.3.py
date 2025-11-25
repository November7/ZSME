# Prosty dekorator
def dekorator(f_dekorowana):
    def fwew(*args, **kwargs):
        print('Ekstra dodatkowe instrukcje przed')
        f_dekorowana(*args, **kwargs)
        print('Ekstra dodatkowe instrukcje po')
    return fwew

def przykladowa_funkcja():
    print('Instrukcje przykladowej funkcji')

# podmiana funkcji przykladowa_funkcja na wersję udekorowaną
przykladowa_funkcja = dekorator(przykladowa_funkcja)

przykladowa_funkcja()

# Alternatywna składnia z użyciem @
@dekorator  
def inna_funkcja():
    print('Instrukcje innej funkcji')

# wywołanie udekorowanej funkcji
inna_funkcja()
