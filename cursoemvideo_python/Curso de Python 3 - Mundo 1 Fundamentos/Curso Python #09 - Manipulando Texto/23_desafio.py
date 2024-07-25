# Exercício Python #023 - Separando dígitos de um número - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from random import randint

# Tarefa 1: Ler um número (Irei usar um número aleatório sorteado)
numero = randint(0, 9999)
print(numero // 10)

# Tarefa 2: Mostrar na tela cada um dos dígitos separados
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
unidade_de_milhar = (numero // 1000) % 10

print(f'O número digitado foi: {numero}.')
print(f'{'-' * 23}')
print(f'{'M':^5}|{'C':^5}|{'D':^5}|{'U':^5}')
print(f'{'-' * 23}')
print(f'{unidade_de_milhar:^5}|{centena:^5}|{dezena:^5}|{unidade:^5}')
print(f'{'-' * 23}')
# Versão 2 - Analisando a entrada do usuário

while True:
    número = input('Digite um número entre 0 e 9999: ')

    if número.isdigit() and 0 <= int(número) <= 9999:
        # Preenche com zeros à esquerda até ter 4 caracteres
        editado = número.zfill(4)
        separar = editado.replace('', ' ').split()

        # Exibe os resultados formatados
        print(f'{"Unidade:":10}{separar[-1]}\n'
              f'{"Dezena:":10}{separar[-2]}\n'
              f'{"Centena:":10}{separar[-3]}\n'
              f'{"Milhar:":10}{separar[-4]}\n')
        break
    else:
        print('Por favor, digite um número válido entre 0 e 9999.')
