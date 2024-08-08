# Exercício Python #078 - Maior e Menor valores na Lista - Aula 00 até 17 - Mundo 3
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


def obter_valores(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(f'Ops, apenas valores numéricos...')


valores = [obter_valores(f'Digite o {i}º valor: ') for i, valor in enumerate(range(5), 1)]

print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == max(valores):
		print(índice, end='... ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == min(valores):
		print(índice, end='... ')

# Versão 2

from random import randint

lista = [randint(1, 10) for valores in range(5)]
posições_maior = []
posições_menor = []

maior = max(lista)
menor = min(lista)

for posição, valor in enumerate(lista, 1):
	if valor == maior:
		posições_maior.append(posição)
	if valor == menor:
		posições_menor.append(posição)

print(f'O maior valor é o {maior}: Apareceu nas posições: {posições_maior}')
print(f'O menor valor é o {menor}: Apareceu nas posições: {posições_menor}')