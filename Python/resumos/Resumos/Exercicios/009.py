# Exercício Python #009 - Tabuada
# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

try:
	fator = int(input('Digite o fator da tabuada: '))

except ValueError:
	print(f'Você digitou um valor inválido!')

else:
	for i in range(11):
		print(f'{fator:^3}{'x':^2}{i:^3}{'=':^2}{fator*i:^3}')