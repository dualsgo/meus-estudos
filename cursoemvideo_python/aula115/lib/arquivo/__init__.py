from emoji import emojize
from time import sleep
def tratamento_arquivo():
    try:
        abrir_arquivo()
    except FileNotFoundError:
        criar_arquivo()


def abrir_arquivo():
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print(emojize(f"{'Nome':^30}|{'Idade':>10}", language='pt'))
            print(f'-' * 45)
            for linha in linhas:
                # Extrai nome e idade da linha e imprime
                nome, idade = linha.strip().split(', ')
                print(f"{nome:^30}|{idade:>10}")
                print(f'-' * 45)

        else:
            print(emojize(":xis: Não há pessoas cadastradas.", language='pt'))


def criar_arquivo():
    # Se o arquivo não existir, cria um arquivo vazio
    print(emojize(":clipe_de_papel: O arquivo 'dados.txt' não existe. Criando o arquivo...", language='pt'))
    sleep(1)
    with open("dados.txt", "w"):
        pass
    print(emojize(":caixa_de_arquivos: Arquivo 'dados.txt' criado com sucesso! :marca_de_seleção_branca:", language='pt'))


def adicionar_dados(n='Desconhecido', i=0):
    dados_novos = f"{n}, {i}\n"
    # Adiciona os novos dados ao arquivo
    with open("dados.txt", "a") as arquivo:
        arquivo.write(dados_novos)
        print(emojize(":divisores_de_pastas: Dados adicionados com sucesso!", language='pt'))

def leia_int(msg):
    while True:
        try:
            msg = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
            continue
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')
            msg = ''
        else:
            return msg

def leia_nome(msg):
    while True:
        try:
            msg = str(input(msg))
            if msg == '':
                msg = 'Não informado'
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
            continue
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')
            msg = ''
        else:
            return msg.strip().title()