# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


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