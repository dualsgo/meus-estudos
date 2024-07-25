# Exercício Python #078 - Maior e Menor valores na Lista
# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

while True:
	try:
		valores = [int(input(f'Digite o valor {i}: ')) for i, valor in enumerate(range(5), 1)]
	except ValueError:
		print(f'Ops, apenas valores numéricos. Reiniciando...')
		continue
	else:
		break


print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == max(valores):
		print(índice, end='... ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == min(valores):
		print(índice, end='... ')