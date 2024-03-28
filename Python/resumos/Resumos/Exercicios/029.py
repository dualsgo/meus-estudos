# Exercício Python #029 - Radar eletrônico
# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


from time import sleep
from random import randint

def multa(vel):
    vel -= 80
    if vel > 0:
        return vel * 7

print('RADAR ELETRÔNICO')

for i in range(6):
    velocidade = randint(70, 95)
    sleep(1)
    excesso = multa(velocidade)
    if excesso is None:
        print(f'Velocidade: {velocidade} km/h - Está no limite de velocidade. Boa viagem.')
    else:
        print(f'Velocidade: {velocidade} km/h - {excesso} km acima do limite de velocidade. Multa: R$ {excesso:.2f}')