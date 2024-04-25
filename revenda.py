usuario = input('Digite seu nome completo: ')
print('Prazer, ' + usuario)
salario = float(input('Digite seu salario mensal: '))
carros = int(input('Digite o numero de carros que voce vendeu: '))
totalv = float(input('Digite o valor total das vendas dos carros que voce vendeu: '))
comissao = totalv * 5 / 100
salariofinal = salario + comissao
print(f'Ola, {usuario}, você vendeu {carros} carros, e o valor total do seu salário é igual a R${salariofinal:.2f}')
