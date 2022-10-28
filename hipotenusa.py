from math import hypot
print ('Calculamos a hipotenusa, mas precisamos de algumas informacoes.')
co = float (input('Digite o comprimento do cateto oposto:'))
ca = float (input('Digite o comprimento do cateto adjacente:'))
hi = hypot (co, ca)
print (f'O valor da hipotenusa e igual a {hi:.2f}')

