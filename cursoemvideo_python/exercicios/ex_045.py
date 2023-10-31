"""Desafio 045 -  (Aula 01 a 12): Crie um programa que faça o computador jogar Jokenpô com você. """

import random
print("""
        PEDRA, PAPEL OU TESOURA!
""")
# Importar biblioteca random
# Define as opções
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
# Usuário entra com a sua mão
usuario = int(input("""
Escolha uma das opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA

"""))
if usuario == 1:
    usuario = jokenpo[0]
elif usuario == 2:
    usuario = jokenpo[1]
elif usuario == 3:
    usuario = jokenpo[2]
# Computador sorteia a sua mão
computador = random.choice(jokenpo)
# Compara para verificar o vencedor
print(f'Você escolheu {usuario} e o PC escolheu {computador}\n')
if computador == jokenpo[0]:
    if usuario == jokenpo[1]:
        print(f'Usuario venceu: {usuario} vence {computador}')
    elif usuario == jokenpo[2]:
        print(f'Computador venceu: {computador} vence {usuario}')
    else:
        print('EMPATE!')
elif computador == jokenpo[1]:
    if usuario == jokenpo[0]:
        print(f'Computador venceu: {computador} vence {usuario}')
    elif usuario == jokenpo[2]:
        print(f'Usuario venceu: {usuario} vence {computador}')
    else:
        print('EMPATE!')
elif computador == jokenpo[2]:
    if usuario == jokenpo[0]:
        print(f'Usuario venceu: {usuario} vence {computador}')
    elif usuario == jokenpo[1]:
        print(f'Computador venceu: {computador} vence {usuario}')
    else:
        print('EMPATE!')
