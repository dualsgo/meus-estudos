"""Desafio 060 - Cálculo do Fatorial (Aula 01 a 14): Faça um programa que leia um número qualquer e mostre o seu fatorial:
EX.: 5! = 5 X 4 X 3 X 2 X 1 = 120
"""
from math import factorial
# Ler um número qualquer pelo teclado - Será usado nos três métodos
numero = int(input('Digite um número: '))

# USANDO MÓDULO
print(f'USANDO MÓDULO\nO fatorial de {numero} é {factorial(numero)}')

# USANDO FOR
print(f'USANDO FOR')
soma = 1
print(f'{numero}! = ', end='')
for fator in range(numero, 0, -1):
    print(fator, end='')
    print(' x ' if fator > 1 else ' = ', end='')
    soma *= fator
print(soma)
# Inicializar um contador e um acumulador
contador = numero
acumulador = 1

# USANDO WHILE
print('USANDO WHILE')
# Imprimir o início da expressão fatorial
print(f'{numero}! = ', end='')

# Iniciar um loop while, que irá multiplicar os números de 1 até numero
while contador > 0:
    # Imprimir o valor atual do contador
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    # Multiplicar o acumulador pelo valor atual do contador
    acumulador *= contador
    # Atualizar o contador, avançando para o próximo número
    contador -= 1

# Após o loop, imprimir o último número da sequência e o resultado do fatorial
print(acumulador)


