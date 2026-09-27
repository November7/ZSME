try:
    # W tym miejscu umieść instrukcje, które mogą zgłosić wyjątek.
    pass
except ZeroDivisionError:
    print("Błąd dzielenia przez zero!")
except KeyError: 
    print("Błąd nieprawidłowego klucza!")    
except Exception:
    print("Dowolny inny błąd, który nie został wcześniej obsłużony")
else:
    print("Nie wystąpił żaden wyjątek")
finally:
    print("Czynności końcowe przy opuszczaniu bloku try")
