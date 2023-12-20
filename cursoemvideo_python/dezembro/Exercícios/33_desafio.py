# Exercício Python #033 - Maior e menor valores - Aula 00 até 09 - Mundo 1
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from random import randint
# Tarefa 1: Ler três números
primeiro = randint(0, 999)
segundo = randint(0, 999)
terceiro = randint(0, 999)
maior = menor = 0

# Tarefa 2: Mostrar o maior e o menor
if primeiro < segundo < terceiro:
    print('Primeiro caso atendido')
    maior = terceiro
    menor = primeiro
if primeiro < segundo > terceiro:
    print('Segundo caso atendido')
    maior = segundo
    if primeiro > terceiro:
        menor = terceiro
    else:
        menor = primeiro
if primeiro > segundo > terceiro:
    print('Terceiro caso atendido')
    maior = primeiro
    if segundo > terceiro:
        menor = terceiro
    else:
        menor = primeiro
if primeiro > segundo < terceiro:
    print('Quarto caso atendido')
    menor = segundo
    if primeiro > terceiro:
        maior = primeiro
    else:
        maior = terceiro

print(f'Entre {primeiro}, {segundo} e {terceiro}.')
print(f'O maior é {maior} e o menor {menor}.')