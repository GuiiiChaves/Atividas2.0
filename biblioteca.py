# Dicionário para armazenar informações de livros
livros = {
    "Senhor dos Anéis": 3,
    "Bíblia": 5,
    "Harry Potter": 2,
    "O Pequeno Príncipe": 4,
    "Extraordinário": 1
}

# Dicionário para armazenar informações de usuários
usuarios = {}

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")

def login():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    
    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido!")
        alugar_livro(nome)
    else:
        print("Login falhou. Verifique seu nome de usuário e senha.")

def alugar_livro(usuario):
    print("Livros disponíveis para aluguel:")
    for livro, quantidade in livros.items():
        if quantidade > 0:
            print(livro)
    
    livro_escolhido = input("Digite o nome do livro que deseja alugar: ")
    
    if livro_escolhido in livros and livros[livro_escolhido] > 0:
        livros[livro_escolhido] -= 1
        print(f"Você alugou o livro '{livro_escolhido}'. Aproveite a leitura!")
    else:
        print("Desculpe, o livro não está disponível para aluguel no momento.")

while True:
    print("\nBiblioteca Online")
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Obrigado por usar a Biblioteca Online. Até a próxima!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
