# Exercício Python #028 - Jogo da Adivinhação v.1.0 - Aula 00 até 09 - Mundo 1
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
from emoji import emojize
# Tarefa 1: Fazer o computador pensar em um número entre 0 e 5
computador = randint(0, 5)

# Tarefa 2: O usuário deve tentar descobrir o número
usuario = int(input(emojize('Em qual número o computador está pensando? :rosto_pensativo:', language='pt')))

# Tarefa 3: Escrever na tela se o usuário acertou ou errou
print(f'Você chutou o número {usuario}.')
sleep(1)
print('O computador pensou no número...', end=' ')
sleep(1)
print(f'{computador}')
sleep(1)
acertou = computador == usuario

if acertou:
    print(emojize('ACERTOU! :rosto_pensativo:', language='pt'))
else:
    print(emojize('ERROU! :rosto_furioso:', language='pt'))
