"""Desafio 076 - Lista de preços com Tupla (Aula 01 a 16): Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final mostre uma listagem de preços organizados em forma tabular.
"""

# Criar a tupla única com os produtos e preços
produtos_precos = ("Mouse", 49.99, "Teclado", 129.99, "Mouse Pad", 19.99, "Cadeira Gamer", 1199.99, "Monitor", 949.99, "Gabinete", 249.99, "Processador", 1099.99, "Fonte", 498.99, "Memória Ram", 499.99, "Placa Mãe", 1299.99, "Fone", 349.99)

# Imprimir nota fiscal
print("=" * 40)
print("                 NOTA FISCAL")
print("=" * 40)

# Separar produtos e preços
produtos = produtos_precos[0::2]  # Seleciona todos os elementos de índice par (produtos)
precos = produtos_precos[1::2]    # Seleciona todos os elementos de índice ímpar (preços)

# Iterar sobre os pares e imprimir
for produto, preco in zip(produtos, precos):
    # {produto: <20} alinha o texto à esquerda em uma largura de campo de 20 caracteres
    # {preco:.2f} formata o preço com duas casas decimais
    print(f'{produto:.<30}R$ {preco: >8.2f}')

print('VERÃO ITERANDO')

# Criar a tupla única com os produtos e preços
produtos_precos = ("Mouse", 49.99, "Teclado", 129.99, "Mouse Pad", 19.99, "Cadeira Gamer", 1199.99, "Monitor", 949.99, "Gabinete", 249.99, "Processador", 1099.99, "Fonte", 498.99, "Memória Ram", 499.99, "Placa Mãe", 1299.99, "Fone", 349.99)

# Imprimir nota fiscal
print("=" * 40)
print("                 NOTA FISCAL")
print("=" * 40)

# Iterar sobre os pares e imprimir usando incrementos de 2
for i in range(0, len(produtos_precos), 2):
    produto = produtos_precos[i]
    preco = produtos_precos[i + 1]
    # {produto: <20} alinha o texto à esquerda em uma largura de campo de 20 caracteres
    # {preco:.2f} formata o preço com duas casas decimais
    print(f'{produto: <30}R$ {preco: >8.2f}')

# SOLUÇÃO GUANABARA

# Criar a tupla única com os produtos e preços
produtos_precos = ("Mouse", 49.99, "Teclado", 129.99, "Mouse Pad", 19.99, "Cadeira Gamer", 1199.99, "Monitor", 949.99, "Gabinete", 249.99, "Processador", 1099.99, "Fonte", 498.99, "Memória Ram", 499.99, "Placa Mãe", 1299.99, "Fone", 349.99)
print("=" * 40)
print("                 NOTA FISCAL")
print("=" * 40)
for pos in range(0, len(produtos_precos)):
    if pos % 2 == 0:
        print(f'{produtos_precos[pos]: <30}', end='')
    else:
        print(f'R$ {produtos_precos[pos]: >8.2f}')
