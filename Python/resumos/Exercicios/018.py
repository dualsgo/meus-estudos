# Exercício Python #018 - Seno, Cosseno e Tangente
# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
while True:
	try:
		angulo = float(input('Digite o valor do ângulo: '))
	except ValueError:
		print('O valor digitado não é válido para essa operação.')
	else:
		print(f'{'-'* 37}')
		print(f'|{'Ângulo':^8}|{'Seno':^8}|{'Cosseno':^8}|{'Tangente':^8}|')
		print(f'{'-'* 37}')
		print(f'|{angulo:^8.2f}|{sin(radians(angulo)):^8.2f}|{cos(radians(angulo)):^8.2f}|{tan(radians(angulo)):^8.2f}|')
		print(f'{'-'* 37}')

		break