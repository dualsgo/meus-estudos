# Exercício Python #076 - Lista de Preços com Tupla
# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


tupla = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

for índice, valor in enumerate(tupla, 1):
	print(f'{valor:.<15}' if índice % 2 else f'R${valor:>8.2f}\n', end='')