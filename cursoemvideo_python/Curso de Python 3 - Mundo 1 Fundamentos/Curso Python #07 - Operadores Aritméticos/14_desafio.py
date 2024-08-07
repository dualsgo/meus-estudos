# Exercício Python #014 - Conversor de Temperaturas - Aula 00 até 07 - Mundo 1
# Escreva um programa que converta uma temperatura digitada em °C para °F

# Fórmula °F = °C x 9  5 + 32
# Fórmula °C = 5 ÷ 9 (°C - 32)

# Tarefa 1: Receber a temperatura em °C
while True:
	try:
		celsius = float(input('Temperatura em Celsius ºC: '))
		fahrenheit = celsius * 1.8 + 32
		print(f'{'Temperatura em Celsius:':<30}ºC{celsius:>10.1f}\n{'Temperatura em Fahrenheit:':<30}ºF{fahrenheit:>10.1f}')
		break
	except ValueError:
		print('Valor inválido!')

# Versão 2

f = c = 0

while True:
	try:
		temperatura = float(input('Digite a temperatura: '))
		c_ou_f = 2
		while 0 != c_ou_f != 1:
			c_ou_f = int(input(
				f'{'-'*30}\n'
				f'[0] Converter de °C para °F\n'
				f'[1] Converter de °F para °C\n'
				f'{'-'*30}'))

		if c_ou_f:
			f = (temperatura - 32) * (5/9)
			print(f'{temperatura}°F corresponde a {f:.1f}°C')
		else:
			c = (temperatura * 1.8) + 32
			print(f'{temperatura}°C corresponde a {c:.1f}°F')
		break

	except ValueError:
		print('Valor inválido. Tente novamente.')
