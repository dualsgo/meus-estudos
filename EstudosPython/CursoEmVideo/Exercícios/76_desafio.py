# Exercício Python #076 - Lista de Preços com Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""produtos = (('Notebook', 3399.99), ('Playstation 5', 4799.99), ('TV 52', 2499.99), ('Cadeira', 999.99), ('Mesa', 699.99), ('Monitor', 1199.99), ('Iphone 15', 7999.99))

for item in produtos:
    print(item)"""

# Lista de itens do carrinho com seus respectivos preços
carrinho = ('Notebook', 3399.99, 'Playstation 5', 4799.99, 'TV 52', 2499.99, 'Cadeira', 999.99, 'Mesa', 699.99, 'Monitor', 1199.99, 'Iphone 15', 7999.99)

# Imprime a nota fiscal
print('-'*45)
print(f'{"NOTA FISCAL": ^45}')
total = 0  # Inicializa a variável total para calcular o valor total da compra
print('-'*45)

# Itera sobre os itens do carrinho e imprime a descrição e o preço
for indice, item in enumerate(carrinho):
    if indice % 2 == 0:  # Se o índice for par (posição da descrição)
        print(f'{item:.<30}', end='')  # Imprime a descrição com ponto final e alinhado à esquerda
    elif indice % 2 == 1:  # Se o índice for ímpar (posição do preço)
        print(f' R${item:>10.2f}')  # Imprime o preço alinhado à direita com duas casas decimais
        total += item  # Soma o preço ao total

# Imprime a linha final da nota fiscal
print('-'*45)

# Imprime o valor total da compra
print(f'{"Valor total": <30} R${total: >10.2f}')
