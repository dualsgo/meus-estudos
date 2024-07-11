# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

while True:
    número = input('Digite um número entre 0 e 9999: ')

    if número.isdigit() and 0 <= int(número) <= 9999:
        # Preenche com zeros à esquerda até ter 4 caracteres
        editado = número.zfill(4)
        print(type(editado))
        separar = editado.replace('', ' ').split()

        # Exibe os resultados formatados
        print(f'{"Unidade:":10}{separar[-1]}\n'
              f'{"Dezena:":10}{separar[-2]}\n'
              f'{"Centena:":10}{separar[-3]}\n'
              f'{"Milhar:":10}{separar[-4]}\n')
        break
    else:
        print('Por favor, digite um número válido entre 0 e 9999.')