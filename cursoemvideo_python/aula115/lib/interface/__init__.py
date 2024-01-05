from time import sleep
from emoji import emojize
from cursoemvideo_python.aula115.lib.arquivo import *


def menu_principal():
    while True:
        escolha_usuario = resposta_usuario()
        if escolha_usuario == 1:
            titulo('VER PESSOAS CADASTRADAS')
            tratamento_arquivo()

        elif escolha_usuario == 2:
            titulo('CADASTRAR PESSOAS')
            nome = leia_nome('Digite o nome: ')
            idade = leia_int('Digite a idade: ')
            adicionar_dados(nome, idade)

        elif escolha_usuario == 3:
            titulo('SAIR DO SISTEMA')
            print('Saindo do sistema... Obrigado por utilizar!')
            break

        else:
            sleep(1)
            print('\033[1;33mSelecione uma das opções do menu.\033[m')



def resposta_usuario():
    # Função para obter a escolha do usuário a partir do menu
    titulo('SISTEMA DE GESTÃO DE PESSOAS')
    menu_de_opcoes()
    try:
        print(f'-' * 45)
        alternativas = int(input('Digite o número da opção desejada: '))
        return alternativas
    except ValueError:
        # Trata erro se o usuário não fornecer um número inteiro
        print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
    except TypeError:
        # Trata erro se ocorrer um TypeError durante a conversão para inteiro
        print(f'\033[1;31mErro! O valor digitado não é de um tipo válido.\033[m')


def menu_de_opcoes():
    # Função para imprimir o menu de opções
    opc = ['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema']
    for i, v in enumerate(opc, 1):
        print(emojize(f'\033[1;32m:tecla_{i}:\033[m \033[1m{v}\033[m', language='pt'))


def titulo(frase):
    sleep(1)
    # Função para imprimir um título centralizado
    print(f'-' * 45)
    print(emojize(f':laptop:\033[1;32m{frase.center(45)}\033[m', language='pt'))
    print(f'-' * 45)