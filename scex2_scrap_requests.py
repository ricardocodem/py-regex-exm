import re
import requests
#pegando url
data = requests.get('https://www.summet.com/dmsi/html/codesamples/addresses.html')
#extraindo telefones
telefone = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
nomes = re.findall(r'[A-Z][a-z]\w+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]\w+', data.text)
print(nomes)
print(telefone)