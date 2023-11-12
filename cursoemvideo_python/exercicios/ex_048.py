"""Desafio 048 - Soma ímpares (Aula 01 a 13): Faça um programa que calcule a soma entre todos os número ímpares que são multiplos de três e que se encontram no interválo de 1 até 500."""
from random import randint
# Coletar os números do intervalo - Salvaremos em uma lista
multiplos_tres = []
multiplos = 0
intervalo = randint(1,999)
# Criaremos o laço de repetição para realizar a contagem
for i in range(3, intervalo, 3):
    # Verificaremos se o número é ímpar e múltiplo de 3 para decidir se será adicionado à lista
    if i % 2 == 1:  # Se o número for divisível por 3 e for ímpar
        multiplos_tres.append(i) # CONTADOR
        multiplos += 1 # ACUMULADOR

# Imprimir os valores sem colchetes
# Imprime o texto sem quebra de linha e com um espaço em branco no final
print('Os valores são:', end=' ')

# Itera sobre os elementos da lista 'multiplos_tres'
for numero in multiplos_tres:
    # Imprime cada número seguido de uma vírgula e um espaço, sem quebra de linha
    print(f'\033[32m{numero}\033[m', end=', ')
# Imprime a string 'e fim.' para indicar o final da lista, seguido por uma quebra de linha
print('e fim.')  # Para imprimir uma quebra de linha


# Calcular a soma dos valores
soma = sum(multiplos_tres)
print(f'A soma entre todos os {multiplos} valores ímpares que são múltiplos de 3 entre 1 e {intervalo} é: {soma}.')


