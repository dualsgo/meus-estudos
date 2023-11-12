"""Desafio 071 - Simulador de Caixa Eletrônico (Aula 01 a 15): Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS.: Considere que o caixa possui cédulas de R$ 100, R$ 50, R$20, R$10, R$5 e R$ 2
"""
# Solicita o valor que será sacado
valor = int(input('Qual valor deseja sacar? '))
resto = valor  # Inicializa o resto com o valor total

# Inicia o loop enquanto ainda há cédulas a serem entregues
while resto != 0:
    # Verifica as condições para as cédulas de diferentes valores

    # Se o valor restante é maior ou igual a 100
    if resto >= 100:
        cedulas = resto // 100  # Calcula a quantidade de cédulas de R$ 100
        resto = resto % 100  # Calcula o resto após entregar as cédulas de R$ 100
        print(f'Sacando {cedulas} cédulas de R$ 100')
    # Se o valor restante é maior ou igual a 50
    elif resto >= 50:
        cedulas = resto // 50
        resto = resto % 50
        print(f'Sacando {cedulas} cédulas de R$ 50')
    # Se o valor restante é maior ou igual a 20
    elif resto >= 20:
        cedulas = resto // 20
        resto = resto % 20
        print(f'Sacando {cedulas} cédulas de R$ 20')
    # Se o valor restante é maior ou igual a 10
    elif resto >= 10:
        cedulas = resto // 10
        resto = resto % 10
        print(f'Sacando {cedulas} cédulas de R$ 10')
    # Se o valor restante é maior ou igual a 5
    elif resto >= 5:
        cedulas = resto // 5
        resto = resto % 5
        print(f'Sacando {cedulas} cédulas de R$ 5')
    # Se o valor restante é maior ou igual a 2
    elif resto >= 2:
        cedulas = resto // 2
        resto = resto % 2
        print(f'Sacando {cedulas} cédulas de R$ 2')

# Indica o final do processo
print('Finalizando!')

