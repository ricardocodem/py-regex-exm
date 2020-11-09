import re

padrao_busca = ['Kawasaki','ninja','ZX-6R','BMW']

texto = '''A Kawasaki Ninja ZX-6R é uma motocicleta da classe 600 cc na série Ninja sport bike da fabricante japonesa Kawasaki. 
Foi introduzida em 1995 e foi constantemente atualizada ao longo dos anos em resposta a novos produtos da Honda, Suzuki e Yamaha.'''

for padrao in padrao_busca:
    print('Procurando por "%s" em "%s":' % (padrao,texto), end=' ')
    if re.search(padrao,texto, flags=re.IGNORECASE):
        print('Encontrado!')
    else:
        print('Não encontrado!')