# Exercício Python #093 - Cadastro de Jogador de Futebol - Aula 00 até 19 - Mundo 3
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep

jogadores = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    for jogo in range(jogos):
        jogador["gols"].append(int(input(f'Quantos gols na partida {jogo + 1}? ')))
    jogador["total"] = sum(jogador["gols"])

    jogadores.append(jogador.copy())

    continuar = str(input('Continuar? S/N ')).strip().upper()

    if continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

sleep(1)

# Calcula a média corretamente
for i, v in enumerate(jogadores):
    media = v["total"] / len(v["gols"])
    print(f'{v["nome"]}, jogou {len(v["gols"])} partidas e marcou {v["total"]} gols. Média de {media:.2f} gols por partida.')
    sleep(1)
    for ind, gol in enumerate(v['gols']):
        print(f'Partida {ind + 1} - {gol} gols')
        sleep(1)