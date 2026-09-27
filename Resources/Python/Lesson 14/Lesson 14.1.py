# JSON i serializacja danych

import json

osoba = {"imie": "Jan", "wiek": 20, "aktywny": True}
tekst = json.dumps(osoba, ensure_ascii=False)
print(tekst)

odczytane = json.loads(tekst)
print(odczytane["imie"])
