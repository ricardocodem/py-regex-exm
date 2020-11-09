import re

texto = "Hoje Acordei às 08:00, almocei 12:30 e fui dormir às 23:30."

hr = re.finditer(r'(\d\d):(\d\d)', texto)

for rx in hr:
    hora = rx.group(1)
    minutos = rx.group(2)
    print("%s horas,%s minutos" %(hora, minutos))