# Exercício Python #030 - Par ou Ímpar?
# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

while True:
	try:
		numero = int(input('Digite um número inteiro: '))
	except ValueError:
		print('Apenas valores numéricos.')
	else:
		print('ÍMPAR' if numero % 2 else 'PAR')
		break