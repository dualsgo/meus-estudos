# Exercício Python #046 - Contagem regressiva
# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for _ in range(10, 0, -1):
	print(f'{_:2}')
	sleep(1)