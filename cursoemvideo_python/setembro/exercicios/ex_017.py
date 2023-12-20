"""Desafio 017 - Catetos e Hipotenusa (Aula 01 a 08): Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
"""
# Usando o módulo
# Passo 1: Importar o módulo - Usaremos o módulo hypot

from math import hypot

# Passo 2: Ler os dados necessários - Usando uma variável para cada informação, utilizando input para que o usuário entre com os dados.

print('Digite o comprimento do cateto oposto: ')
cateto_oposto = float(input(''))
print('Digite o comprimento do cateto adjacente: ')
cateto_adjacente = float(input(''))
print('\n\033[7m###################################\033[m\n')
# Passo 3: Exibir a hipotenusa utilizando o módulo
print(f"""MÉTODO COM MÓDULO

O cateto oposto vale \033[1;31m{cateto_oposto}\033[m.
O cateto adjacente vale \033[1;32m{cateto_adjacente}\033[m.
Portanto, a hipotenusa vale aproximadamente \033[1;33m{hypot(cateto_oposto, cateto_adjacente):.2f}\033[m.
""")
print('\033[7m###################################\033[m\n')

# Sem utilizar os módulos
# Realizar e exibir o comprimento da hipotenusa - A hipotenusa é igual à raiz quadrada da soma dos catetos ao quadrado”.
# Lembrando que existe um módulo para mostrar a raiz quadrada sqrt()
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)
print(f"""MÉTODO SEM MÓDULO

O cateto oposto vale \033[1;31m{cateto_oposto}\033[m.
O cateto adjacente vale \033[1;32m{cateto_adjacente}\033[m.
Portanto, a hipotenusa vale aproximadamente \033[1;33m{hipotenusa:.2f}\033[m.
""")
