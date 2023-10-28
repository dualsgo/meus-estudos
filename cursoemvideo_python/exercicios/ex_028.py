"""Desafio 028 - Jogo de Adivinhação V.1.0 (Aula 01 a 10): Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário acertou ou errou."""

# Passo 1: Fazer o computador pensar em um número - Para isso usaremos a biblioteca random. Importaremos apenas o método randint
from random import randint
print("""
      \033[1;41mJOGO DA ADIVINHAÇÃO\033[m
      """)
# Passo 2: Pedir para o usuário descobrir qual é esse número - Para isso o usuário precisa entrar com o seu palpite através da função input atribuída a uma variável
print('\033[1mEm qual número estou pensando? Entre 0 e 5... Valendo!\033[m')

# A variável número armazena o valor sorteado. Os argumentos definem o intervalo entre os números, nesse caso entre 0 e 5.
numero = randint(0, 5)

# A variável palpite armazena o valor digitado pelo usuário.
palpite = int(input(''))

# Passo 3: Escrever na tela se o usuário acertou ou errou - Para isso usaremos a estrutura condicional if else. Para fins de entendimento criamos uma variável que irá receber a comparação entre o número pensado pelo computador e o número digitado pelo usuário.

verificacao = palpite == numero  # Compara os valores e retorna True ou False

if verificacao:  # Se for True
    print(
        f'\033[1;42mAcertou miseravi!\033[m Estava mesmo pensando no número {numero}')
else:  # Se for False
    print(
        f'\033[1;43mErrou feio, errou rude\033[m. Não estava pensando no número \033[1;32m{palpite}\033[m e sim no \033[1;31m{numero}\033[m.')
