# Exercício Python #014 - Conversor de Temperaturas
# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. °F = (°C x 1.8) + 32

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