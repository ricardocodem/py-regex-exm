import re
import urllib.request

#pegando url e preparando para extracao de dados
data = urllib.request.urlopen('https://web.archive.org/web/20190415032528/https://www.nasdaq.com/')
#extraindo os dados
for info in data:
    if re.findall('nasdaqHomeIndexChart.storeIndexInfo', info.decode()):
        p1 = re.findall('\"(.+?)\"', info.decode())
        print(info.decode())
        for final in p1:
            print(final)