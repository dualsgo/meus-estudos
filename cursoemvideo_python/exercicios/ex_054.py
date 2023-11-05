"""Desafio 054 -  (Aula 01 a 13):
Crie um programa que leia o ano de nascimento de sete pessoas e no final mostre quantas pessoas já são maiores de 21 anos e quantos não são."""
# import randint para sortear um ano aleatório
from random import randint
# import date para pegar o ano atual no sistema
from datetime import date
# import sleep para gerar uma pausa entre os print
from time import sleep
# Definindo o ano atual
ano_atual = date.today().year
# Contadores para maior e menor iniciado com valor zero
maior = 0
menor = 0
# Definindo o loop com intervalo de 7
for i in range(8):
    # Sorteia o ano
    ano = randint(1980, 2023)
    # Dá uma pausa
    sleep(1)
    # Define a maioridade
    maioridade = ano_atual - ano
    # Se for maior ou igual a 21
    if maioridade >= 21:
        # Exibe a mensagem e acrescenta 1 ao contador de maiores
        print(f'Nascido em \033[1;32m{ano}\033[m tem \033[1;32m{maioridade}\033[m anos: \033[1;32mÉ MAIOR DE IDADE!\033[m')
        maior += 1
    else:
        # Senão exibe a mensagem e acrescenta no contador de menores
        print(f'Nascido em \033[1;31m{ano}\033[m tem \033[1;31m{maioridade}\033[m anos: \033[1;31mÉ MENOR DE IDADE!\033[m')
        menor += 1
print(f'Ao todo temos:\n\033[1;32m{maior} maiores de 21 anos\033[m\n\033[1;31m{menor} menores de 21 anos\033[m')
