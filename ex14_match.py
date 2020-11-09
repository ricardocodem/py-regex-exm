import re

lista=['222-4685','192.168.0.1','E0-06-E0-FD-EC-27','2016:0000:130F:000:0000:07C0:853A:140B','192.168.0.115']
padrao=re.compile(r'(\d{3})\.(\d{3})\.(\d)\.(\d+)')

for m in lista:
    p = re.match(padrao, m)
    if p:
        print((p.group(0)))