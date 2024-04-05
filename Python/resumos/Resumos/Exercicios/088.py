# Exercício Python #088 - Palpites para a Mega Sena
# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

while True:
    try:
        jogos = int(input('Quantos jogos deseja simular? '))
    except ValueError:
        print(f'Valor inválido.')
        continue
    break

bilhetes = []
for _ in range(jogos):
    numeros_unicos = set()
    while len(numeros_unicos) < 6:
        numeros_unicos.add(randint(1, 60))
    bilhete = sorted(list(numeros_unicos))
    bilhetes.append(bilhete)

for ordem, jogo in enumerate(bilhetes, 1):
    print(f'{f" Jogo {ordem} ":=^23}')
    print(*[f'{valor:^3}' for valor in jogo], sep=' ', end='\n')