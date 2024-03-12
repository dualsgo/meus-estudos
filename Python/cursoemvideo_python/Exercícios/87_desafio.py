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