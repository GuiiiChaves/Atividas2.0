print("Sou um conversor de Real para outras Moedas, selecione a moeda que voce deseja::")
print("1. Dolar")
print("2. Euro")


escolha = input("Digite sua escolha (1/2): ")

num1 = float(input("Digite o valor em Real que voce deseja converter: "))
euro = float (num1/6)
dolar = float (num1/5.50)


if escolha == '1':
    print(f"Resultado, essa e sua quantidade de dolar: {dolar:.2f}" )
elif escolha == '2':
    print(f"Resultado, essa e sua quantidade de euro: {euro:.2f} ")


