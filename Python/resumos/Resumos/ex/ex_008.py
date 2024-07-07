# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

def conversões(m):
	print(
		f'\033[1m{'Kilômetros:':<15}{m / 1000:>12}{'km':<3}\n'
		f'{'Hectometros:':<15}{m / 100:>11}{'hm':<3}\n'
		f'{'Decâmetros:':<15}{m / 10:>10}{'dam':<3}\n'
		f'{'Metros:':<15}{m:>10}{'m':<3}\n'
		f'{'Decímetros:':<15}{m * 10:>10}{'dm':<3}\n'
		f'{'Centímetros:':<15}{m * 100:>10}{'cm':<3}\n'
		f'{'Milímetros:':<15}{m * 1000:>10}{'mm':<3}\033[m')


while True:
	try:
		metros = float(input('Digite o valor da medida em metros: '))
		conversões(metros)
		break
	except ValueError:
		print('O valor informado não é válido para essa operação!')