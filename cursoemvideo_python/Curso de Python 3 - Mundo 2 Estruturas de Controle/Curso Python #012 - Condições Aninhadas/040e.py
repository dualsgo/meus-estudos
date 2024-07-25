# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:
# - Média abaixo de 5,0: REPROVADO
# - Média entre 5,0 e 6,9: RECUPERAÇÃO
# - Média 7,0 ou superior: APROVADO
from emoji import emojize
from time import sleep


def obtem_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print('O valor deve estar entre 0 e 10')
        except ValueError:
            print('Apenas números são aceitos')


notas = [obtem_nota(f'Digite a {i}ª nota: ') for i in range(1, 5)]
média = sum(notas) / len(notas)
avaliação = emojize(f'\033[1;31mREPROVADO :livro_fechado:\033[m' if média < 5 else '\033[1;33mEM RECUPERAÇÃO :livro_azul:\033[m' if média < 7 else '\033[1;32mAPROVADO :livro_verde:\033[m', language='pt')

print(f'{'-'*30}')
for i, nota in enumerate(notas, 1):
	print(f'{f'{i}ª Nota':<10}{nota:>20.2f}')
	sleep(1)
print(f'{'-'*30}')
print(f'{'Situação:':<10}{avaliação:^20}')