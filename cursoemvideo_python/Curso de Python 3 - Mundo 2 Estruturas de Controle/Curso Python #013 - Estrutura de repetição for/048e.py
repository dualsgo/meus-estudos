# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = quantidade = 0
print('Múltiplos de 3 entre 1 e 500: ', end='')
for i in range(3, 501, 3):
	print(i, end=', ' if i < 498 else '.\n')
	if i % 2:
		soma += i
		quantidade += 1
print(f'A soma entre os {quantidade} números ímpares múltiplos de três entre 1 e 500 é igual a {soma}')

"""valores = [i for i in range(3, 499, 3) if i % 2 != 0]
print(f'A soma entre os {len(valores)} valores ímpares, múltiplos de 3 no intervalo ente 1 e 500 é {sum(valores)}.')

print(f'Os {len(valores)} valores considerados são:')
for i, v in enumerate(valores):
	print(v, end=', ' if i < len(valores)-1 else '.')"""