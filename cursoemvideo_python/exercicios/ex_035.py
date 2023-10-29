"""Desafio 028 - Analisando Triângulo V1.0 (Aula 01 a 10): Desenvolva um programa que leia o comprimento o segmento de três retas e diga ao usuário se elas podem formar um triângulo. """

# Ler o comprimento das retas - Atribuiremos a uma variável, uma lista e cada elemento da lista receberá um valor para representar um lado

a = int(input('Digite um valor para o A lado do triângulo: '))
b = int(input('Digite um valor para o B lado do triângulo: '))
c = int(input('Digite um valor para o C lado do triângulo: '))

# A soma de dois dos três lados do triângulo deve ser maior que o terceiro lado
triangulo = a + b > c and a + c > b and b + c > a

if triangulo:
    print(
        f'\033[7;32;40mOs lados de tamanho {a}, {b} e {c} podem formar um triângulo!\033[m')
else:
    print(
        f'\033[7;31;40mOs lados de tamanho {a}, {b} e {c} não podem formar um triângulo!\033[m')
