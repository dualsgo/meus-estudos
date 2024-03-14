# Exercício Python #095 - Aprimorando os Dicionários - Aula 00 até 19 - Mundo 3
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from random import randint
jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    for jogo in range(jogos):
        print(f'Gols marcados na {jogo + 1}º partida: ')
        jogador["gols"].append(randint(0, 4))

    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())

    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

media = jogador["total"] / jogos

print(f'{"Nome":^10}|{"Gols":^15}|{"Total":^10}|{"Média":^10}')

for i, v in enumerate(jogadores):
    print(f'{v["nome"]:^10}|{str(v["gols"]):^15}|{v["total"]:^10}|{media:^10}')

# Loop para visualizar estatisticas individualmente
while True:
    ident = int(input('Digite o ID do jogador:'))

    # Verifica se o ID é válido
    if 0 <= ident < len(jogadores):
            print(
                f'{jogadores[ident]["nome"]}, jogou {len(jogadores[ident]["gols"])} partidas e marcou {jogadores[ident]["total"]} gols. Média de {media} gols por partida.')
            for ind, gol in enumerate(jogadores[ident]['gols'], 1):
                print(f'Partida {ind} - {gol} gols')
    else:
        # Caso o ID seja inválido, exibe uma mensagem de erro
        print('ID do aluno inválido. Tente novamente.')

    continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        break