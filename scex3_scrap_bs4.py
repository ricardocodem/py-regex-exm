import re
import requests
from bs4 import BeautifulSoup

#pegando url
data = requests.get('https://www.unicarioca.edu.br/conheca/professores', verify=False)

#extraindo conteudo e carregando bs4
soup = BeautifulSoup(data.text, 'html.parser')
#capturando os nomes dos professores
p_nomes = soup.find_all('p', {'class': 'professor-nome'})
#captura emails
p_emails = re.finditer(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
#loop para limpar as tags e excesso de espaços
for nomes in p_nomes:
    print('Nome:',nomes.text.strip())
#loop para email
for emails in p_emails:
    print(emails.expand(r'emails: \1'))