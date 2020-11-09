import re

def data_por_extenso(data):
    dia = data.group(1)
    mes = data.group(2)
    ano = data.group(3)
    meses = {
        '01':'Janeiro', '02': 'Fevereiro', '03':'Março', '04':'Abril',
        '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto',
        '09':'Setembro', '10':'Novembro', '12':'Dezembro'    
    }
    return dia + " de " + meses[mes] + " de " + ano

texto = "Hoje é dia 16/04/2016."
regex = r'(\d\d)/(\d\d)/(\d\d\d\d)'

print (re.sub(regex, data_por_extenso, texto))


