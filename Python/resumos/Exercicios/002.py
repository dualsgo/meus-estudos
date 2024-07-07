# Exercício Python #002 - Respondendo ao Usuário
# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite o seu nome: ').strip().title()

print(f'Olá, \033[32m{nome}\033[m. É um prazer ter você por aqui!')