# Exercício Python #051 - Progressão Aritmética - Aula 00 até 13 - Mundo 2
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

while True:
	try:
		primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
		razão = int(input('Digite a razão da prograssão: '))
		décimo_termo = razão*10
		for i, v in enumerate(range(primeiro_termo, décimo_termo+1, razão), 1):
			print(f'{i} ⮕ ' if v < 10 else f'{i} ⮕ FIM!', end='')
		break
	except ValueError:
		print('Tipo de dado inválido!')
