def Up(txt):
    return txt.upper()


def Low(txt):
    return txt.lower()


def pisz(co, jak):
    return jak(co)


def waluta(nazwa):
    def dodaj_walute(kwota):
        return f"{kwota} {nazwa}"
    return dodaj_walute


def dekorator_przywitaj(funkcja):
    def wrapper(*args, **kwargs):
        print("Dodatkowa instrukcja przed wywołaniem funkcji.")
        ret = funkcja(*args, **kwargs)
        print("Dodatkowa instrukcja przed wywołaniem funkcji.")
        return ret
    return wrapper


nowy_print = dekorator_przywitaj(print)


nowy_print("Cześć, świecie!")
