# Exercício Python #054 - Grupo da Maioridade - Aula 00 até 13 - Mundo 2
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from time import sleep  # Importa a função sleep para pausas temporizadas
from random import randint  # Importa a função randint para gerar anos de nascimento aleatórios
from datetime import date  # Importa a classe date para obter o ano atual

ano_atual = date.today().year  # Obtém o ano atual

maiores = menores = 0  # Inicializa os contadores de maiores e menores de idade

for i in range(1, 8):  # Loop para iterar sobre 7 pessoas
    print(f'Pessoa {i}, seu ano de nascimento é: ', end='')
    sleep(1)  # Pausa por 1 segundo
    ano_nascimento = randint(1950, 2023)  # Gera um ano de nascimento aleatório entre 1950 e 2023
    print(ano_nascimento)
    idade = ano_atual - ano_nascimento  # Calcula a idade
    print(f'{idade} anos de idade')
    sleep(1)  # Pausa por 1 segundo
    if idade >= 21:
        print('\033[1;32mMaior de idade\033[m')  # Exibe em verde se for maior de idade
        maiores += 1
    else:
        print('\033[1;31mMenor de idade\033[m')  # Exibe em vermelho se for menor de idade
        menores += 1
    sleep(1)  # Pausa por 1 segundo

print(f'Ao todo temos {menores} menores e {maiores} maiores de idade.')
