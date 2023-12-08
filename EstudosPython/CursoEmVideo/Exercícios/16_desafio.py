# Exercício Python #016 - Quebrando um número - Aula 00 até 08 - Mundo 1
# Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.

# Tarefa 1: Ler um número pelo teclado.
from math import trunc
numero = float(input('Digite um número: '))

# Tarefa 2: Mostrar na tela a sua porção inteira.
print(f'A parte inteira do número {numero} é {trunc(numero)}.')
print(f'A parte decimal é {numero - trunc(numero):.3f}.')
