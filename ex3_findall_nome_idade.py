#setup
import re

#entrada
texto = '''
Michelle tem 20 anos a sua irmã Monique tem 22 anos.
José, o avô delas, tem 77 anos e mora no apto 17.'''

#buscando idades
idades = re.findall(r"[0-9]{1,2}\s[a-z]+",texto)
print(idades)

#buscando nomes
nomes = re.findall(r"[A-Z][a-z]+\w",texto)
print(nomes)