import math
an = float (input ('digite o angulo que voce deseja:'))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print (f'O angulo de {an} tem o seno de {s:.2f}, o cosseno de {c:.2f} e a tangente de {t:.2f}.' )