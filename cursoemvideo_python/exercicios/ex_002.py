""" Desafio 002 - Respondendo ao usuário (Aula 01 a 04): Faça um programa que leia o nome de uma pesoa e mostre uma mensagem de boas vindas."""

# Passo 1: Armazenar em uma variável a informação, utilizando a função input() para que o usuário digite o valor
print('\033[7mQual é o seu nome? \033[m')
# Solicita ao usuário que digite seu nome e armazena na variável 'nome'
nome = input('')

# Passo 2: Exibir o resultado utilizando a função print() e uma string formatada.
# Exibe a mensagem de boas-vindas com o nome digitado
print(
    f'\033[34mSeja bem-vindo, \033[1;32m{nome}\033[m\033[34m. É um prazer tê-lo por aqui!\033[m')
