"""Desafio 045 -  GAME PEDRA PAPEL E TESOURA (Aula 01 a 12): Crie um programa que faça o computador jogar Jokenpô com você. """

# Importar a biblioteca random
import random
# Cores
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}
print(f"""
        \033[7mPEDRA, PAPEL OU TESOURA!\033[m
""")

# Define as opções em uma lista
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

# Usuário entra com a sua mão
usuario = input("""
Escolha uma das opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA

""")

# Define a jogada do usuário baseado no número selecionado atribuindo a um índice da lista
if int(usuario) == 1:
    usuario = jokenpo[0]
elif int(usuario) == 2:
    usuario = jokenpo[1]
elif int(usuario) == 3:
    usuario = jokenpo[2]

# Computador sorteia a sua mão
computador = random.choice(jokenpo)

# Compara para verificar o vencedor
print(f'Você escolheu {usuario} e o PC escolheu {computador}\n')
if computador == jokenpo[0]:
    if usuario == jokenpo[1]:
        print(
            f'{cor["green"]}O USUÁRIO VENCEU:{cor["fecha"]} {usuario} vence {computador}')
    elif usuario == jokenpo[2]:
        print(
            f'{cor["red"]}O COMPUTADOR VENCEU:{cor["fecha"]} {computador} vence {usuario}')
    else:
        print(f'{cor["yellow"]}EMPATE!{cor["fecha"]}')
elif computador == jokenpo[1]:
    if usuario == jokenpo[0]:
        print(
            f'{cor["red"]}O COMPUTADOR VENCEU:{cor["fecha"]} {computador} vence {usuario}')
    elif usuario == jokenpo[2]:
        print(
            f'{cor["green"]}O USUÁRIO VENCEU:{cor["fecha"]} {usuario} vence {computador}')
    else:
        print(f'{cor["yellow"]}EMPATE!{cor["fecha"]}')
elif computador == jokenpo[2]:
    if usuario == jokenpo[0]:
        print(
            f'{cor["green"]}O USUÁRIO VENCEU:{cor["fecha"]} {usuario} vence {computador}')
    elif usuario == jokenpo[1]:
        print(
            f'{cor["red"]}O COMPUTADOR VENCEU:{cor["fecha"]} {computador} vence {usuario}')
    else:
        print(f'{cor["yellow"]}EMPATE!{cor["fecha"]}')
