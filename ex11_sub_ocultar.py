import re

def protege(termo):
    if len(termo.group(0)) == 5:
        return '***' + termo.group(0)[-2:]
    elif len(termo.group(0)) == 9:
        return '*****' + termo.group(0)[-4:]
    else:
        return termo.group(0)

texto = "Matrícula: 12345, Telefone: 999902580, Idade: 33"
texto_protegido = re.sub(r'\d+', protege, texto)

print(texto_protegido)