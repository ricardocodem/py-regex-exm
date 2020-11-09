import re

lista = ['Paulo pula','Paula pilota','Paulo canta','Paula grita','pula pula']

for m in lista:
    encontra = re.match('(p\w+)\W(p\w+)', m, flags=re.IGNORECASE)

    if encontra:
        print((encontra.groups()))