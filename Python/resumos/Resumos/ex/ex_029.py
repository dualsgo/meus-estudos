# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint
from time import sleep

while True:
	try:
		simulações = int(input('Quantas simulações deseja realizar? '))
		break
	except ValueError:
		print('Valor inválido!')

for carro in range(1, simulações+1):
	velocidade = randint(70, 90)

	multado = velocidade - 80 <= 0

	valor = 7 * (velocidade - 80)

	print(f'{f'Veículo {carro} - Velocidade registrada:':<30}{f'{velocidade}Km/h':>20}')

	print(f'\033[1;32mTenha um bom dia. Dirija com segurança.\033[m' if multado else f'\033[1;31mVocê foi multado em R$ {valor:.2f} por ultrapassar {valor/7}Km da velocidade permitida.\033[m')

	sleep(1)