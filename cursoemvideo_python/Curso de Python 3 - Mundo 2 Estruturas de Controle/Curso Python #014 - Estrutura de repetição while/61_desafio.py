# Exercício Python #061 - Progressão Aritmética v2.0 - Aula 00 até 14 - Mundo 2
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

while True:
	try:
		primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
		razão = int(input('Digite a razão da progressão: '))
		contador = 0
		termo = primeiro_termo
		while contador < 10:
			print(f'{termo} ⮕ ' if contador < 9 else f'{termo} ⮕ FIM!', end='')
			contador += 1
			termo += razão
		break
	except ValueError:
		print('Tipo de dado inválido!')

