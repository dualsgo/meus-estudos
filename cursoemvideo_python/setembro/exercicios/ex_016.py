"""Desafio 016 - Quebrando um número (Aula 01 a 08): Crie um programa que leia um número inteiro e mostre a sua porção inteira.
"""
# Passo 1: Importaremos o método trunc para exibir apenas a parte inteira do número que for digitado
from math import trunc
# Passo 2: Ler o número - Utilizamos uma variável para armazenar o valor solicitando que o usuario digite um número com a função input e a função int para converter a string para inteiro

print('Digite um número qualquer:')
numero = float(input(''))
# Exibimos o valor
print('\033[1;42mMétodo usando math\033[m')

print(f"""
O número digitado foi: \033[1;31m{numero}\033[m
A parte inteira é: \033[1;32m{trunc(numero):.2f}\033[m
A parte decimal é: \033[1;33m{numero - trunc(numero):.2f}\033[m
""")

# Método sem usar o módulo
print('\033[1;42mMétodo sem usar o módulo math\033[m')
# Uma opção é usar a função int() a outra é realizar as operações matemáticas.

# A parte inteira é resultado da divisão inteira do número digitado por 1. Assim será exibido o próprio número, porém somente a parte inteira
numero_inteiro = numero // 1

# A parte decimal logo é número digitado menos a parte inteira
numero_decimal = numero - (numero // 1)
print(f"""
O número digitado foi: \033[1;31m{numero}\033[m
A parte inteira é: \033[1;32m{numero_inteiro:.2f}\033[m
A parte decimal é: \033[1;33m{numero_decimal:.2f}\033[m""")
