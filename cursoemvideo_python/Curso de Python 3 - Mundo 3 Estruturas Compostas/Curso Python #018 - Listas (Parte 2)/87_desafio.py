# Exercício Python #087 - Mais sobre Matriz em Python - Aula 00 até 18 - Mundo 3
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from random import randint
matriz = [[], [], []]
soma_pares = 0

for linha in range(3):
    for coluna in range(3):
        numero = randint(0, 99)
        print(f'Digite o valor da posição [{linha}][{coluna}] - {numero}')
        if numero % 2 == 0:
            soma_pares += numero
        matriz[linha].append(numero)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:2} ] ', end='')
    print()

print(f'\nA soma de todos os valores pares é {soma_pares}')

terceira_coluna = 0
for linha in range(3):
    terceira_coluna += matriz[linha][2]
print(f'A soma de todos os valores na terceira coluna é {terceira_coluna}')

maior_segunda_linha = max(matriz[1])
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

# Resumida

matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]

pares = coluna = 0
maior = max(matriz[1])
for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')
    for i, valor in enumerate(linha):
        pares += valor if valor % 2 == 0 else 0
        if i == 2:  # Se for a terceira coluna
            coluna += valor


print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {maior}')

# Atual

matriz = [[randint(0, 9) for valor in range(3)] for linha in range(3)]

soma_pares = soma_terceira_coluna = 0
maior_segunda_linha = max(matriz[1])

for linha in matriz:
	soma_terceira_coluna += linha[2]
	for valor in linha:

		if not valor % 2:
			soma_pares += valor

		print(f'[{valor:^3}]', end=' ')
	print('')

print(f'A soma de todos os valores pares é igual a: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')