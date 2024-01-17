from time import sleep
from emoji import emojize
from cursoemvideo_python.aula115.lib.arquivo import *

def tratamento_arquivo():
    try:
        abrir_arquivo()
    except FileNotFoundError:
        criar_arquivo()

    # Adiciona a funcionalidade de pesquisa
    pesquisa = input("Digite parte do EAN para pesquisar (ou deixe em branco para mostrar todos): ").strip().lower()

    if pesquisa:
        pesquisar_ean(pesquisa)

def abrir_arquivo():
    estoque = {}  # Dicionário para armazenar a soma da quantidade por EAN

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            valores = linha.strip().split(', ')
            if len(valores) == 6:
                ean, sap, descricao, quantidade, fornecedor, deposito = valores

                # Verifica se a chave já existe no dicionário
                if ean in estoque:
                    # Se existir, adiciona a quantidade à entrada existente
                    estoque[ean]['quantidade'] += int(quantidade)
                else:
                    # Se não existir, cria uma nova entrada no dicionário
                    estoque[ean] = {
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': int(quantidade),
                    }

        # Imprime os resultados
        print(emojize(f"{'EAN':^15}|{'Descrição':^30}|{'Fornecedor':^30}|{'Quantidade Total':^20}", language='pt'))
        print(f'-' * 95)
        for ean, info in estoque.items():
            print(f"{ean:^15}|{info['descricao']:^30}|{info['fornecedor']:^30}|{info['quantidade']:^20}")
            print(f'-' * 95)

        if not estoque:
            print(emojize(":xis: Não há produtos cadastrados.", language='pt'))

def pesquisar_ean(pesquisa):
    resultados = []

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            valores = linha.strip().split(', ')
            if len(valores) == 6:
                ean, sap, descricao, quantidade, fornecedor, deposito = valores

                if pesquisa in ean.lower():
                    resultados.append({
                        'ean': ean,
                        'descricao': descricao,
                        'fornecedor': fornecedor,
                        'quantidade': quantidade,
                    })

        # Imprime os resultados da pesquisa
        if resultados:
            print("\nResultados da pesquisa:")
            print(emojize(f"{'EAN':^15}|{'Descrição':^30}|{'Fornecedor':^30}|{'Quantidade':^20}", language='pt'))
            print(f'-' * 95)
            for resultado in resultados:
                print(f"{resultado['ean']:^15}|{resultado['descricao']:^30}|{resultado['fornecedor']:^30}|{resultado['quantidade']:^20}")
                print(f'-' * 95)
        else:
            print(emojize(f":xi: Não foram encontrados resultados para a pesquisa '{pesquisa}'.", language='pt'))

def criar_arquivo():
    # Se o arquivo não existir, cria um arquivo vazio
    print(emojize(":clipe_de_papel: O arquivo 'estoque.txt' não existe. Criando o arquivo...", language='pt'))
    sleep(1)
    with open("estoque.txt", "w"):
        pass
    print(emojize(":caixa_de_arquivos: Arquivo 'estoque.txt' criado com sucesso! :marca_de_seleção_branca:", language='pt'))

# Restante do seu código...

# Exemplo de uso
# tratamento_arquivo()