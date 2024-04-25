print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print("Resultado:", num1 + num2)
elif escolha == '2':
    print("Resultado:", num1 - num2)
elif escolha == '3':
    print("Resultado:", num1 * num2)
elif escolha == '4':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro! Divisão por zero!")
else:
    print("Opção inválida")
