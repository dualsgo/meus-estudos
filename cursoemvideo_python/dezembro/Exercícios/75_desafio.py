# Exercício Python #075 - Análise de dados em uma Tupla - Aula 00 até 16 - Mundo 3
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Importa a função randint da biblioteca random
from random import randint

# Gera uma tupla de 4 números aleatórios entre 0 e 9
numeros = (
    randint(0, 9),
    randint(0, 9),
    randint(0, 9),
    randint(0, 9)
)

# Imprime os números da tupla
print(f'Os números são: ', end='')
for numero in numeros:
    print(numero, end=' ')

print('')  # Pula uma linha após os números

# Conta quantas vezes o número 9 aparece na tupla
print(f'O 9 apareceu quantas vezes? {numeros.count(9)}')

# Verifica se o número 3 está presente na tupla e imprime a posição (caso esteja)
# ou uma mensagem indicando que não está presente
mensagem_3 = (f'\033[1;32mO número 3 apareceu no primeiro no índice {numeros.index(3)}.\033[m' if 3 in numeros else '\033[1;31mO número 3 não aparece na tupla.\033[m')
print(mensagem_3)

# Imprime os números pares da tupla (exceto o zero)
print('Os números pares são:', end=' ')
for numero in numeros:
    if numero % 2 == 0 and numero != 0:
        print(f'{numero}', end=' ')

