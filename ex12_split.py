import re

rxHora = re.compile(r'(\d\d):(\d\d)')
rxSeparador = re.compile(r'[/.:]')

if rxHora.search('05:30'):
    print("Válido")

print(rxHora.sub(r'\1h\2min','05:30'))

print(rxSeparador.split('1.23'))
print(rxSeparador.split('05:30'))
print(rxSeparador.split('16/04/16'))
