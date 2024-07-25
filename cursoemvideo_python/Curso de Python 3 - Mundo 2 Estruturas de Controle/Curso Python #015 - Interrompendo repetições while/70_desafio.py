# Exercício Python #070 - Estatísticas em produtos - Aula 00 até 15 - Mundo 2
#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

"""
Essa verificação é necessária porque, na primeira iteração (quando contador é igual a 1), você não tem um valor anterior para comparar.

if contador == 1:
    produto_mais_barato = nome
    valor_produto_mais_barato = valor
else:
    if valor < valor_produto_mais_barato:
        produto_mais_barato = nome
        valor_produto_mais_barato = valor

No entanto, você pode simplificar isso utilizando uma técnica comumente chamada de "sentinela". Nesse caso, você inicializa valor_produto_mais_barato com um valor que representa infinito, indicado por float('inf'). Como nenhum preço real será maior que infinito, na primeira iteração, qualquer preço será menor que esse valor "infinito". Isso elimina a necessidade de verificar se contador é igual a 1.

valor_produto_mais_barato = float('inf')  # Inicializa com infinito

while True:
    # ... (restante do código)

    if valor < valor_produto_mais_barato:
        # Atualiza o produto mais barato se o valor atual for menor
        produto_mais_barato = nome
        valor_produto_mais_barato = valor
"""

total_gasto = 0
produtos_mais_mil = 0
produto_mais_barato = ''
valor_produto_mais_barato = float('inf')  # Inicializa com infinito
contador = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto: R$ '))

    total_gasto += valor  # Atualiza o total gasto na compra
    contador += 1  # Incrementa o contador de produtos

    if valor > 1000:
        produtos_mais_mil += 1  # Conta produtos que custam mais de R$ 1000

    if valor < valor_produto_mais_barato:
        # Atualiza o produto mais barato se o valor atual for menor
        produto_mais_barato = nome
        valor_produto_mais_barato = valor

    continuar = str(input('Deseja continuar? S/N ')).strip().upper()

    while continuar not in 'SsNn':
        continuar = str(input('Comando inválido: S ou N ')).strip().upper()

    if continuar in 'Nn':
        print('Encerrando...')
        break
    else:
        print('Continuando...')

# Exibe as informações finais
print(f'O total gasto na compra foi: R$ {total_gasto:.2f}')
print(f'Ao todo {produtos_mais_mil} {'produto custa' if produtos_mais_mil == 1 else 'produtos custam'} mais de R$ 1000,00')
print(f'O produto mais barato é {produto_mais_barato} que custa R$ {valor_produto_mais_barato:.2f}')
