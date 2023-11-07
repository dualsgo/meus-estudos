"""Desafio 063 - Sequência de Fibonacci (Aula 01 a 14): Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência Fibonacci
EX: 0 > 1 > 1 > 2 > 3 > 5 > 8
"""

# Número de termos
termos = int(input('Quantos termos deseja visualizar? '))
contador = 1
termo = 0
anterior = 1  # Inicializar o termo anterior

while contador <= termos:
    print(f'{contador}º termo - {termo}')
    # Calcula o próximo termo a partir dos dois anteriores
    proximo = termo + anterior
    # Atualiza os valores do termo e do termo anterior
    anterior = termo
    termo = proximo
    contador += 1


