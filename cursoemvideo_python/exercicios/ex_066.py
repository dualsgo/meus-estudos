"""Desafio 066 - Vários números com flag (Aula 01 a 15): Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de para da. No final, mostre quantos números foram digitados e qual foi a soma entre ekes (desconsiderando o flag)
"""
# Inicializando os contadores
contador = 0  # Contador de quantidade de números digitados
acumulador = 0  # Contador de valores (Soma)

# Inicia o loop infinito
while True:
    # Recebe o valor digitado
    numero = int(input('\033[1;32mDigite um número:\033[m \033[1;31m(999 para sair) \033[m'))
    print(f'{contador + 1}º valor: {numero}')

    # Verifica se o valor é 999
    if numero == 999:
        break  # Se for, para o loop

    # Se não, incrementa a quantidade de números digitados
    contador += 1
    # E soma o valor do número
    acumulador += numero

# Exibe a quantidade total de números digitados e a soma deles
print(f'Foram digitados \033[1;32m{contador}\033[m números. A soma entre eles é \033[1;32m{acumulador}\033[m.')
