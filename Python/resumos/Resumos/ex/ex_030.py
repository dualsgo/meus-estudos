# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

while True:
	try:
		número = int(input('Digite um valor (diferente de zero): '))
		if not número:
			continue
		print(f'{número} é', '\033[1;31mÍMPAR\033[m' if número % 2 else '\033[1;32mPAR\033[m')
		break
	except ValueError:
		print('Valor de tipo não válido para essa operação.')