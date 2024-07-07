# Exercício Python #038 - Comparando números
#  Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os mostrando uma mensagem na tela:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

print(
	f'{valor1} é maior que {valor2}' if valor1 > valor2 else
	f'{valor1} é menor que {valor2}' if valor1 < valor2 else
	f'{valor1} e {valor2} são iguais.')