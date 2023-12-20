""" Desafio 018 - Seno, Cosseno e Tangente (Aula 00 a 08): Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

# Passo 1: Importar os módulos necessários da biblioteca math
from math import sin, cos, tan, radians

# Passo 2: Ler o ângulo informado pelo usuário
print('\033[7mDigite o ângulo para saber o seno, cosseno e a tangente:\033[m\n')
angulo = float(input(''))

# Passo 3: Calcular os valores do seno, cosseno e tangente
seno = sin(radians(angulo))  # Calcula o seno do ângulo em graus
cosseno = cos(radians(angulo))  # Calcula o cosseno do ângulo em graus
tangente = tan(radians(angulo))  # Calcula a tangente do ângulo em graus

# Passo 4: Exibir os resultados
print(f"""
Você digitou o ângulo {angulo} graus.
O seno desse ângulo é: {seno:.2f}.
O cosseno desse ângulo é: {cosseno:.2f}.
A tangente desse ângulo é: {tangente:.2f}""")


# MÉTODO SEM MÓDULO