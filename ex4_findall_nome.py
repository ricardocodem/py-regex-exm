import re

#entrada
texto = '''
Ricardo Teixeira, Marck, C. Zuck, Connor MacLeod, Dr. João da Silva, 
Garcia, Robert, Sra. Julia Maria, José Bonifácio, Pres. Juscelino Kubitschek '''

#buscando nomes
nomes = re.findall(r"[A-Z][a-z]\w+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]\w+",texto)
print(nomes)