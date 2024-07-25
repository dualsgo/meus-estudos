# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep
for i in range(10, -1, -1):
	sleep(1)
	print(i if i > 0 else emojize('BOOM! :fogos_de_artifício:', language='pt'))