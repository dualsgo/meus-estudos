"""Desafio 074 - Menor e maior valores em Tupla (Aula 01 a 16): Crie um programa que irá gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

# Criar a tupla e atribuir cinco números aleatórios
from random import randint

lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# Método 1
print('Os números sorteados, são:')
for item in lista:
    print(item, end=', ')
print('FIM!')
print(f'O maior número da lista é {max(lista)}')
print(f'E o menor número da lista é {min(lista)}')
# Método 2
em_ordem = sorted(lista)
print(f'{em_ordem}')
print(f'O maior é {em_ordem[-1]}')
print(f'O menor é {em_ordem[0]}')