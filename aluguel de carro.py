qd = int (input ('Por quantos dias voce alugou o carro?'))
qk = float (input ('quantos km voce rodou com o carro?'))
v = float (60 * qd) + (0.15 * qk)
print (f'voce alugou o carro por {qd}, rodou {qk}km, valor a ser pago e {v:.2f}R$')
