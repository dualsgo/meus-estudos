"""Desafio 072 - Número por extenso (Aula 01 a 16): Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostrá-lo por extenso.
"""

# Tupla totalmente preenchida
numeros = (
'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Loop principal
while True:
    # Ler um número entre zero e vinte
    numero = int(input('Digite um número entre 0 e 20: '))

    # Valida se o número digitado está entre 0 e 20
    if 0 <= numero <= 20:
        print(
            f'O número digitado foi \033[1;31m{numero}\033[m e por extenso se escreve \033[1;31m{numeros[numero]}\033[m')

        # Pergunta se o usuário deseja ver outro número
        continuar = input('Deseja ver outro número? S/N ')

        # Verifica se o usuário deseja continuar o programa
        if continuar in 'Ss':
            print('Certo! Vamos ao próximo')
        else:
            print('O programa será encerrado!')
            break
    else:
        print('DIGITE NOVAMENTE!')
