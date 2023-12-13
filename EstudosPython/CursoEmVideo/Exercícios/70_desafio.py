# Exercício Python #070 - Estatísticas em produtos - Aula 00 até 15 - Mundo 2
#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_gasto = 0

produtos_mais_mil = 0

produto_mais_barato = ''
valor_produto_mais_barato = 0

contador = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto: R$ '))

    total_gasto += valor

    contador += 1

    if valor > 1000:
        produtos_mais_mil += 1

    if contador == 1:
        produto_mais_barato = nome
        valor_produto_mais_barato = valor
    else:
        if valor < valor_produto_mais_barato:
            produto_mais_barato = nome
            valor_produto_mais_barato = valor

    continuar = str(input('Deseja continuar? S/N ')).strip().upper()

    while continuar not in 'SsNn':
        continuar = str(input('Comando inválido: S ou N ')).strip().upper()

    if continuar in 'Ss':
        print('Continuando...')
    if continuar in 'Nn':
        print('Encerrando...')
        break

print(f'O total gasto na compra foi: R$ {total_gasto:.2f}')
print(f'Ao todo {produtos_mais_mil} produtos custam mais de R$ 1000,00')
print(f'O produto mais barato é {produto_mais_barato} que custa R$ {valor_produto_mais_barato:.2f}')