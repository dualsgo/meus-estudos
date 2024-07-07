# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

while True:
	try:
		angulo = radians(float(input('Digite o valor do ângulo:')))
		seno = sin(angulo)
		cosseno = cos(angulo)
		tangente = tan(angulo)
		print(f'{'Seno:':<12}{seno:>5.2f}\n{'Cosseno:':<12}{cosseno:>5.2f}\n{'Tangente:':<12}{tangente:>5.2f}')
		break
	except ValueError:
		print('Valor inválido!')