"""Desafio 070 - Estatísticas de produtos (Aula 01 a 15): Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
- Qual o total gasto na compra
- Quantos produtos custam mais de R$ 1000
- Qual é o nome do produto mais barato
"""

# Inicializa as variáveis
gasto = 0
produtos_mais_1000 = 0
valor_mais_barato = 0
# Inicia o loop principal
while True:
    # Solicita informações sobre o produto
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: '))
    resposta = str(input('Deseja continuar? S/N')).upper().strip()

    # Atualiza o total gasto
    gasto += preco

    # Verifica se o produto custa mais de R$ 1000,00
    if preco > 1000:
        produtos_mais_1000 += 1

    # Verifica se é o primeiro produto ou se o preço é menor que o preço do produto mais barato atual
    if gasto == preco or preco < valor_mais_barato:
        valor_mais_barato = preco
        nome_mais_barato = produto

    # Verifica se o usuário deseja continuar
    if resposta == 'N':
        print('Processando valores...')
        break

# Exibe os resultados finais
if gasto == 0:
    print('Não houve gastos!')
else:
    print(f'O valor total gasto foi de R$ {gasto:.2f}')
    print(f'Ao todo, há {produtos_mais_1000} produtos que custam acima de R$ 1000,00')
    print(f'O produto mais barato é o {nome_mais_barato} que custa R$ {valor_mais_barato:.2f}')

