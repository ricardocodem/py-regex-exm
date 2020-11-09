import re

regex = re.compile(r'[^.+\-*\(?\/^0-9\s\)?]')

teste_exp = ['3 - 3','2+2','1-1','2*2','20/2','2+3+5.5','.3 * -3+ 9','1+3x 3','21 ÷ 7','5+(2-5)','(3*(55+1))']

for m in teste_exp:
    if len(regex.findall(m)):
        print(m,'Inválida')
    else:
        print(m,'Válida')