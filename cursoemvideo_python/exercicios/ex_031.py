"""Desafio 031 - Custo da Viagem (Aula 01 a 10): Desenvolva um programa que pergunte a distância de uma viagem em Km.

- Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas."""

print("""
      \033[1mTABELA DE PREÇOS\033[m
      \033[31mAté 200Km - R$ 0,50 por Km\033[m
      \033[32m +  200Km - R$ 0,45 por Km\033[m
      """)
# Passo 1: Perguntar a distância - Atribuindo o valor a uma variável por meio de um input
distancia = int(input('Distância: '))
# Passo 2: Calcular o preço da passagem - Considerando R$ 0,50 para viagens de até 200Km e R$ 0,45 para viagens mais longas
print(f'Sua viagem será de \033[1m{distancia}Km\033[m.')
if distancia <= 200:
    valor = distancia * .5
    print(f'Você deverá pagar \033[1mR$ {valor:.2f}\033[m.')
else:
    valor = distancia * .45
    print(f'Você deverá pagar \033[1mR$ {valor:.2f}\033[m.')
