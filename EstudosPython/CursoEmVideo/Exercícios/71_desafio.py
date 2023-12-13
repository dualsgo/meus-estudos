# Exercício Python #071 - Simulador de Caixa Eletrônico - Aula 00 até 15 - Mundo 2
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor_saque = int(input('Quanto deseja sacar? R$ '))
notas = 0

while True:

    if valor_saque >= 100:
        notas = valor_saque // 100
        valor_saque = valor_saque % 100
        print(f'Sacando {notas} notas de R$ 100')

    if valor_saque >= 50:
        notas = 0
        notas = valor_saque // 50
        valor_saque = valor_saque % 50
        print(f'Sacando {notas} notas de R$ 50')

    if valor_saque >= 20:
        notas = 0
        notas = valor_saque // 20
        valor_saque = valor_saque % 20
        print(f'Sacando {notas} notas de R$ 20')

    if valor_saque >= 10:
        notas = 0
        notas = valor_saque // 10
        valor_saque = valor_saque % 10
        print(f'Sacando {notas} notas de R$ 10')

    if valor_saque >= 5:
        notas = 0
        notas = valor_saque // 5
        valor_saque = valor_saque % 5
        print(f'Sacando {notas} notas de R$ 5')

    if valor_saque >= 2:
        notas = 0
        notas = valor_saque // 2
        valor_saque = valor_saque % 2
        print(f'Sacando {notas} notas de R$ 2')

    if valor_saque <= 1:
        break





