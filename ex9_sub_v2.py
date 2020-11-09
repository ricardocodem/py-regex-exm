import re

def corretor_simples(m):
    abreviado = m.group()
    abreviacoes = {
        'vc':'você', 'hj':'hoje'
    }
    return abreviacoes[abreviado]

texto = "vc viu  como   o dia está bonito hj, está ótimo para um  passeio vc não acha?"
novoTexto = re.sub(r'\s+', ' ',texto)
print (re.sub(r'vc|hj', corretor_simples, novoTexto))