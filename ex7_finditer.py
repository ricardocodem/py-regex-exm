import re

texto = "Hoje Acordei às 08:00, almocei 12:30 e fui dormir às 23:30."
hr = re.finditer(r'(\d\d):(\d\d)', texto)

for rx in hr:
    print (rx.expand(r'\1 horas, \2 minutos.'))