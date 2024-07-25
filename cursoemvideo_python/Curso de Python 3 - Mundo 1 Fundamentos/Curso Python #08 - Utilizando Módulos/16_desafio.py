# Exercício Python #016 - Quebrando um número - Aula 00 até 08 - Mundo 1
# Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.

# Tarefa 1: Ler um número pelo teclado.
from math import trunc
numero = float(input('Digite um número: '))

# Tarefa 2: Mostrar na tela a sua porção inteira.
print(f'A parte inteira do número {numero} é {trunc(numero)}.')
print(f'A parte decimal é {numero - trunc(numero):.3f}.')

# Versão 2

while True:
    try:
        número = float(input('Digite um valor: '))
        parte_inteira = número // 1
        parte_decimal = número % 1
        convertido = str(número)
        tamanho = len(convertido)
        tamanho_decimal = len(convertido[convertido.index('.'):])
        print(f'{"Número:":<10}\033[1;33m{número:>{tamanho}}\033[m\n'
              f'{"Inteiro:":<10}\033[1;31m{parte_inteira:<{tamanho}.1g}\033[m\n'
              f'{"Decimal:":<10}\033[1;32m{parte_decimal:>{tamanho}.{tamanho_decimal}g}\033[m')
        break

    except ValueError:
        print('Valor inválido!')
