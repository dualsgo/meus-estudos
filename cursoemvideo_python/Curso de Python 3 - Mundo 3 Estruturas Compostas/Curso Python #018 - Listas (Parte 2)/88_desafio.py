# Exercício Python #088 - Palpites para a Mega Sena - Aula 00 até 18 - Mundo 3
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = []  # Lista principal

quantidade_jogos = int(input('Digite a quantidade de jogos que deseja simular: '))

for jogo in range(quantidade_jogos):
    bilhete = []  # Lista com cada bilhete de seis números

    while len(bilhete) < 6:
        n = randint(1, 60)
        if n in bilhete:
            n = randint(1, 60)
        else:
            bilhete.append(n)

        jogos.append(bilhete[:])

    bilhete.sort()
    print(f'Jogo {jogo+1}: {bilhete}')
    sleep(1)
    bilhete.clear()


    # V2

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

# V3

while True:
	try:
		quantidade_de_jogos = int(input('Quantos jogos deseja realizar? '))
		break
	except ValueError:
		print('Essa valor não é válido para essa operação!')

jogos = []

for sorteio in range(quantidade_de_jogos):
	bilhete = []

	while True:
		valor = randint(1, 60)

		if valor not in bilhete:
			bilhete.append(valor)

		if len(bilhete) == 6:
			bilhete.sort()
			jogos.append(bilhete)
			break

for _, bilhetes in enumerate(jogos, 1):
	print(f'{f'{_}º JOGO':^30}')
	print(f'{'-'*30}')
	for valor in bilhetes:
		print(f'{valor:^5}', end='')

	print(f'\n{'-'*30}')