# Exercício Python #052 - Números primos - Aula 00 até 13 - Mundo 2
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from random import randint  # Importa a função randint para gerar um número aleatório

# Tarefa 1: Ler um número
numero = randint(1, 99)  # Gera um número aleatório entre 1 e 99
divisores = 0  # Inicializa o contador de divisores

print(f'Você escolheu o número {numero}.')

# Tarefa 2: Verificar se é primo ou não:
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1
        print(f'\033[1;32m{i}\033[m', end=', ')  # Exibe os divisores em verde
    else:
        print(f'\033[1;31m{i}\033[m', end=', ')  # Exibe os não divisores em vermelho

print('fim da lista.')

print(f'Ao todo são {divisores} divisores.')

primo = divisores == 2  # Verifica se o número de divisores é igual a 2, indicando que é primo

if primo:
    print('É UM NÚMERO PRIMO!')
else:
    print('NÃO É UM NÚMERO PRIMO!')
