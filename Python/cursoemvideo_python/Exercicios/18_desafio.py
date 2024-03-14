# Exercício Python #018 - Seno, Cosseno e Tangente - Aula 00 até 08 - Mundo 1
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

# Tarefa 1: Ler o ângulo
angulo = int(input('Digite um ângulo qualquer: (0º a 360º) '))

# Tarefa 2: Mostrar na tela os valores de seno, cosseno e tangente
angulo_radiano = radians(angulo)

# Arredondar os resultados para 2 casas decimais
seno = round(sin(angulo_radiano), 2)
cosseno = round(cos(angulo_radiano), 2)
tangente = round(tan(angulo_radiano), 2)

print(f'O seno do ângulo {angulo}º é ≈ {seno}.')
print(f'O cosseno do ângulo {angulo}º é ≈ {cosseno}.')
print(f'A tangente do ângulo {angulo}º é ≈ {tangente}.')

# ROUND - Seu propósito é arredondar um número para um número inteiro ou para um número específico de casas decimais