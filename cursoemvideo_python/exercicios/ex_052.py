"""Desafio 052 -  (Aula 01 a 13):
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

Um número primo é um número natural maior que 1 que só é divisível por 1 e por ele mesmo. Em outras palavras, um número primo não possui divisores além de 1 e ele próprio."""

# Entrar com o número
numero = int(input('Digite o número: '))
divisores = 0
for i in range(1, numero+1):
# Verifica quantos divisores há entre 1 e o número verificando se a divisão possui resto. Se nao possuir adiciona a lista de divisores
    if numero % i == 0:
        divisores += 1
        print(f'\033[32m{i}\033[m', end=', ')
    else:
        print(f'\033[31m{i}\033[m', end=', ')
# Quantidade de divisores
if divisores == 2:
    print(f'\n\n\033[32m{numero} É PRIMO!\nPossui {divisores} divisores.\033[m')
else:
    print(f'\n\033[31m{numero} NÃO É PRIMO!\nPossui {divisores} divisores.\033[m')

