# Exercício Python #055 - Maior e menor da sequência - Aula 00 até 13 - Mundo 2
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Simples
import random
pesos = [round(random.uniform(60.0, 180.0), 1) for h in range(5)]
for pessoa, peso in enumerate(pesos, 1):
	print(f'Pessoa {pessoa}: {peso:>8}kg')

# Completo
from random import randint
from time import sleep

pesado = float('-inf')
leve = float('inf')

while True:
    try:
        print(f'{"-"*20}')
        print(f'{"PESSOA":^10}{"PESO KG":^10}')
        print(f'{"-"*20}')
        for pessoa in range(1, 6):
            sleep(1)
            peso = randint(40, 200)
            print(f'{pessoa:^10}{peso:^10.2f}Kg')
            if peso > pesado:
                pesado = peso
            if peso < leve:
                leve = peso
        print(f'A pessoa mais pesada pesa {pesado:>10.2f}Kg')
        print(f'A pessoa mais leve pesa {leve:>10.2f}Kg')
        break
    except Exception as e:
        print(f'ERRO: {e}')