n = input ('Digite seu nome:').strip()
m = n.upper()
mi = n.lower()
c = len(n) - n.count (' ')
pn = n.split() [0]
pl = len(pn)
print ('Analisando seu nome...')
print (f'Seu nome em maiusculo e {m}')
print (f'Seu nome em minusculo e {mi} ')
print (f'Seu nome possui {c} letras')
print (f'Seu primeiro nome e {pn} e ele tem {pl} letras.')



