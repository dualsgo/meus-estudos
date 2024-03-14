# Exercício Python #074 - Maior e menor valores em Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Importa a função randint da biblioteca random
from random import randint

# Gera uma tupla de 5 números aleatórios entre 0 e 99
numeros_sorteados = (
    randint(0, 60),
    randint(0, 60),
    randint(0, 60),
    randint(0, 60),
    randint(0, 60)
)

# Cria uma tupla ordenada a partir dos números gerados
tupla_ordenada = sorted(numeros_sorteados)

# Encontra o menor e o maior número na tupla original
menor_numero = min(numeros_sorteados)
maior_numero = max(numeros_sorteados)

# Imprime os números sorteados
print(f'Os números sorteados foram: ', end='')
for numero in numeros_sorteados:
    print(numero, end=' ')
print('')  # Pula uma linha após os números sorteados

# Imprime o menor e o maior número
print(f'O menor é {menor_numero} e o maior é {maior_numero}')

# Imprime os números em ordem crescente
print(f'Em ordem: {tupla_ordenada}')

