# Exercício Python #023 - Separando dígitos de um número - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from random import randint

# Tarefa 1: Ler um número (Irei usar um número aleatório sorteado)
numero = randint(0, 9999)
print(numero // 10)

# Tarefa 2: Mostrar na tela cada um dos dígitos separados
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
unidade_de_milhar = (numero // 1000) % 10

print(f'O número digitado foi: {numero}.')
print(f'Seus dígitos são:\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nUnidade de milhar: {unidade_de_milhar}')
