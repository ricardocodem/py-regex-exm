import re

texto = "Vc viu  como   o dia está bonito hj, está ótimo para um  passeio vc não acha?"

subst1 = re.sub(r'\s+', ' ', texto) #elimina espaços duplicados
subst2 = re.sub(r'vc', 'você', subst1, flags=re.IGNORECASE)
subst3 = re.sub(r'hj', 'hoje', subst2)

print(subst3)