import re

texto = "Heitor nasceu em 16/04/2016"

regex = r'(\d+)/(\d+)/(\d+)'

match = re.search(regex,texto)

if match != None:
    #lista todo o grupo
    print("Encontrado: % s" % (match.group(0))) 
    #lista grupo 1 dia
    print("Dia: % s" % (match.group(1))) 
    #lista grupo 2 mes  
    print("Mês: % s" % (match.group(2)))
    #lista grupo 3 ano
    print("Ano: % s" % (match.group(3))) 
    
else:  
    print("Padrão não encontrado.") 