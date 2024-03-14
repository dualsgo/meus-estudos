# Exercício Python #029 - Radar eletrônico - Aula 00 até 09 - Mundo 1
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint

# Tarefa 1: Ler a velocidade do carro.
velocidade = randint(40, 110)
print(f'RADAR: Sua velocidade é de {velocidade}Km/h')

velocidade_maxima = 80

# Tarefa 2: Definir o valor da multa
if velocidade > velocidade_maxima:
    print('Você foi multado!')

    acima_do_limte = velocidade - velocidade_maxima
    multa = acima_do_limte * 7

# Tarefa 3: Mostrar a mensagem dizendo se foi multado ou não
    print(f'O limite de velocidade é de 80Km/h. Você foi flagrado a {velocidade}Km/h.')
    print(f'O valor da multa é de R$ 7,00 por Km/h ultrapassado. Sua multa será de R$ {multa:.2f} por trafegar a {acima_do_limte}Km/h além do permitido.')
else:
    print('Você está dentro do limite permitido!')
