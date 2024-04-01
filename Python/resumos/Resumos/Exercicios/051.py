# Exercício Python #051 - Progressão Aritmética
# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Agora a razão: '))
décimo = (razão * 10) + 1
print(f'Os dez primeiros termos da progressão de razão {razão} são:')

for contador, acumulador in enumerate(range(primeiro, décimo,  razão), 1):
	print(f'{acumulador} ⮕ ' if contador < 10 else f'{acumulador} ⮕ FIM!', end='')