# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. °F = (°C x 1.8) + 32

while True:
	try:
		celsius = float(input('Temperatura em Celsius ºC: '))
		fahrenheit = celsius * 1.8 + 32
		print(f'{'Temperatura em Celsius:':<30}ºC{celsius:>10.1f}\n{'Temperatura em Fahrenheit:':<30}ºF{fahrenheit:>10.1f}')
		break
	except ValueError:
		print('Valor inválido!')