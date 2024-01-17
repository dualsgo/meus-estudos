from time import sleep
from emoji import emojize
from cursoemvideo_python.aula115.lib.arquivo import *

def main():
    while True:
        print_menu()
        escolha_usuario = obter_escolha_usuario()

        if escolha_usuario == 1:
            tratamento_arquivo()
        elif escolha_usuario == 2:
            realizar_pesquisa()
        elif escolha_usuario == 3:
            print("Saindo do sistema... Obrigado por utilizar!")
            break
        else:
            print('\033[1;33mSelecione uma das opções do menu.\033[m')

def print_menu():
    print("\nMenu Principal:")
    print("1. Visualizar todos os produtos")
    print("2. Pesquisar produtos")
    print("3. Sair do sistema")

def obter_escolha_usuario():
    try:
        return int(input("Digite o número da opção desejada: "))
    except ValueError:
        print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
        return 0

def realizar_pesquisa():
    print("\nOpções de pesquisa:")
    print("1. Pesquisar por EAN")
    print("2. Pesquisar por SAP")
    print("3. Pesquisar por Descrição")
    print("4. Pesquisar por Fornecedor")
    print("5. Voltar ao menu principal")

    opcao_pesquisa = obter_opcao_pesquisa()

    if opcao_pesquisa == 5:
        return

    termo_pesquisa = input("Digite o termo de pesquisa: ").strip().lower()

    if opcao_pesquisa in [1, 2, 3, 4]:
        pesquisar_produtos(opcao_pesquisa, termo_pesquisa)

def obter_opcao_pesquisa():
    try:
        return int(input("Digite o número da opção de pesquisa desejada: "))
    except ValueError:
        print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
        return 0

def pesquisar_produtos(opcao_pesquisa, termo_pesquisa):
    resultados = []

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            valores = linha.strip().split(', ')
            if len(valores) == 6:
                ean, sap, descricao, quantidade, fornecedor, deposito = valores

                termo = ""

                if opcao_pesquisa == 1:
                    termo = ean.lower()
                elif opcao_pesquisa == 2:
                    termo = sap.lower()
                elif opcao_pesquisa == 3:
                    termo = descricao.lower()
                elif opcao_pesquisa == 4:
                    termo = fornecedor.lower()

                if termo_pesquisa in termo:
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })

        if resultados:
            print("\nResultados da pesquisa:")
            print(emojize(f"{'EAN':^15}|{'Descrição':^30}|{'Fornecedor':^30}|{'Quantidade':^20}", language='pt'))
            print(f'-' * 95)
            for resultado in resultados:
                print(f"{resultado['ean']:^15}|{resultado['descricao']:^30}|{resultado['fornecedor']:^30}|{resultado['quantidade']:^20}")
                print(f'-' * 95)
        else:
            print(emojize(f":xi: Não foram encontrados resultados para a pesquisa '{termo_pesquisa}'.", language='pt'))

def pesquisar_por_coluna(coluna, termo):
    resultados = []

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            valores = linha.strip().split(', ')
            if len(valores) == 6:
                ean, sap, descricao, quantidade, fornecedor, deposito = valores

                # Verifica a coluna escolhida e compara com o termo
                if coluna == '1' and termo in ean.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })
                elif coluna == '2' and termo in sap.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })
                elif coluna == '3' and termo in descricao.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })
                elif coluna == '4' and termo in quantidade.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })
                elif coluna == '5' and termo in fornecedor.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })
                elif coluna == '6' and termo in deposito.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })

    if resultados:
        print("\nResultados da pesquisa:")
        print(emojize(f"{'EAN':^15}|{'Descrição':^30}|{'Fornecedor':^30}|{'Quantidade':^20}", language='pt'))
        print(f'-' * 95)
        for resultado in resultados:
            print(f"{resultado['ean']:^15}|{resultado['descricao']:^30}|{resultado['fornecedor']:^30}|{resultado['quantidade']:^20}")
            print(f'-' * 95)
    else:
        print(emojize(f":xi: Não foram encontrados resultados para a pesquisa '{termo}' na coluna '{coluna}'.", language='pt'))



def menu_principal():
    while True:
        print("======= MENU PRINCIPAL =======")
        print("1. Visualizar tudo")
        print("2. Pesquisar por EAN")
        print("3. Pesquisar por coluna")
        print("4. Sair do sistema")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            tratamento_arquivo()
        elif escolha == '2':
            pesquisa = input("Digite parte do EAN para pesquisar: ").strip().lower()
            pesquisar_ean(pesquisa)
        elif escolha == '3':
            coluna = input("Digite o número da coluna para pesquisar (1 - EAN, 2 - SAP, 3 - Descrição, 4 - Quantidade, 5 - Fornecedor, 6 - Depósito): ")
            termo = input("Digite o termo para pesquisar: ").strip().lower()
            pesquisar_por_coluna(coluna, termo)
        elif escolha == '4':
            print("Saindo do sistema... Obrigado por utilizar!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()