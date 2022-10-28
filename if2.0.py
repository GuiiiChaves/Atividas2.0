print ('Bem vindo ao estacionamento do Shopping Patteo! retire sua ficha:')
s = 10.50
print ('Bem vindo ao sistema de pagamento do estacionamento Patteo')
pi = int (input ('digite abaixo o tempo que voce passou no Shopping Patteo: em minutos '))
if pi<=20:
    print (float (input ('O valor a pagar sera 0 R$.')))
if pi<=60:
   print (float (input (f'o valor a pagar e de {s}R$. ')))
if pi <= 120:
    print (float(input(f'o valor a pagar sera de {s+2:.2f}R$')))
if pi <= 180:
    print (float(input(f'o valor a pagar sera de {s+4:.2f}R$')))
if pi <= 240:
    print (float (input(f'o valor a pagar sera de {s+6:.2f}R$')))
else:
    print(float(input(f'o valor a pagar sera {s+9.50:.2f}')))


