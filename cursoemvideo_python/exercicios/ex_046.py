"""Desafio 046 - Contagem regressiva (Aula 01 a 13): Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício indo de 0 até 10, com uma pausa de 1 segundo entre els."""


# Importar a biblioteca que irá mostrar as mensagens com pausa
from time import sleep
# sleep(1)
# Cores
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}
print('CONTAGEM REGRESSIVA!')
# Criar a contagem regressiva - Usamos a iteração -1
for i in range(10, -1, -1):
    print(f'{cor["red"]}{i}, ', end='') # Exibe o valor atual da iteração
    sleep(1) # define o intervalo de um segundo
print('FELIZ ANO NOVO!')

