import re

#entrada
texto = '''
Ricardo Teixeira, Marck, C. Zuck, Connor MacLeod, Dr. João da Silva, 
Garcia, Robert, Sra. Julia Maria, José Bonifácio, Pres. Juscelino Kubitschek '''

titulo = r"(?:[A-Z][a-z]*\.\s*)?"
nome1 = r"[A-Z][a-z]\w+,?\s+"
meioD = r"(?:da|de|do|das|dos)*\s*"
meioI = r"(?:[A-Z][a-z]*\.?\s*)?"
nome2 = r"[A-Z][a-z]\w+"

nomes = re.findall(titulo + nome1 + meioD + meioI + nome2, texto)
print(nomes)