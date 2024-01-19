# Exercício Python #115a - Criando um menu em Python
from time import sleep
# ___________________________________
#         MENU PRINCIPAL
# ___________________________________
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar pessoas
# 3 - Sair do sistema
# ___________________________________
# Escolha a opção desejada:

# Se for um tipo diferente mostra uma mensagem de erro e pergunta novamente
# Se for um número fora do intervalo mostra o menu e pergunta novamente

# Se escolher uma opção correta mostra

# ___________________________________
#         OPÇÃO ESCOLHIDA
# ___________________________________
import json

def ver_pessoas_cadastradas():
    try:
        with open("pessoas.txt", "r") as arquivo:
            pessoas = arquivo.readlines()

        if not pessoas:
            print("Nenhuma pessoa cadastrada ainda.")
        else:
            print("Pessoas cadastradas:")
            for pessoa_json in pessoas:
                pessoa = json.loads(pessoa_json)
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
    except FileNotFoundError:
        print("Nenhuma pessoa cadastrada ainda.")


def menu():
    try:
        escolha_user = int(input('Digite o número da opção desejada: '))
        return escolha_user
    except ValueError:
        print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
    return None


def cadastrar_pessoa():
    # Adicione lógica para cadastrar uma nova pessoa
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoa = {"nome": nome, "idade": idade}
    salvar_pessoa(pessoa)

def salvar_pessoa(pessoa):
    # Adicione lógica para salvar a pessoa em um arquivo TXT
    with open("pessoas.txt", "a") as arquivo:
        arquivo.write(json.dumps(pessoa) + "\n")
    print("Pessoa cadastrada com sucesso!")

def escolha():
    while True:
        titulo('SISTEMA DE GESTÃO DE PESSOAS')
        print("""# 1 - Ver pessoas cadastradas
# 2 - Cadastrar pessoas
# 3 - Sair do sistema
--------------------------------------""")

        num_escolhido = menu()

        if num_escolhido is not None:
            if num_escolhido == 1:
                ver_pessoas_cadastradas()
            elif num_escolhido == 2:
                cadastrar_pessoa()
            elif num_escolhido == 3:
                titulo('SAIR DO SISTEMA')
                print('Saindo do sistema... Obrigado por utilizar!')
                break
            else:
                print(f'Selecione uma das opções do menu acima. {num_escolhido} não é válido!')

def titulo(frase):
    print(f'-' * (len(frase) + 10))
    print(f'\033[1;32m{frase:^35}\033[m')
    print(f'-' * (len(frase) + 10))

escolha()