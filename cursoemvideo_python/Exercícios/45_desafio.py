# Exercício Python #045 - GAME: Pedra Papel e Tesoura - Aula 00 até 12 - Mundo 2
# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
from emoji import emojize

# Tarefa 1: Receber a jogada do jogador e do computador
opcoes = [emojize(':punho_levantado:', language='pt'), emojize(':mão_levantada:', language='pt'), emojize(':mão_em_v_de_vitória:', language='pt')]
computador = randint(0, 2)
print(computador)
print('Jogador, faça a sua jogada:')

print(emojize(':tecla_0: PEDRA :punho_levantado:\n:tecla_1: PAPEL :mão_levantada:\n:tecla_2: TESOURA :mão_em_v_de_vitória:', language='pt'))
jogador = int(input(''))

while jogador > 2:
    print('Opção inválida!')
    jogador = int(input(''))

pedra = 0
papel = 1
tesoura = 2

print(emojize('JO :punho_levantado:', language='pt'), end=' ')
sleep(1)
print(emojize('KEN :mão_levantada:', language='pt'), end=' ')
sleep(1)
print(emojize('PO :mão_em_v_de_vitória:', language='pt'))
sleep(1)

# Tarefa 2: Definir as regras para cada combinação e exibir o vencedor


if jogador == computador:
    print('Deu empate!')
elif (jogador == pedra and computador == tesoura) or (jogador == tesoura and computador == papel) or (jogador == papel and computador == pedra):
    print(emojize('Jogador vence! :troféu:', language='pt'))
else:
    print(emojize('Computador vence! :troféu:', language='pt'))

print(f'Jogador {opcoes[jogador]} X {opcoes[computador]} Computador')
