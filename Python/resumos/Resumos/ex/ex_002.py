# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

from emoji import emojize as e

nome = input(e(':pessoa: Digite o seu nome: ', language='pt')).strip().title()

print(e(f'Olá, \033[1m{nome}\033[m. É um prazer te conhecer! :rosto_festivo:', language='pt'))

# Podemos executar o mesmo comando em apenas uma instrução. Nesse caso o valor não é armazenado e se perde.
print(f'É um prazer te conhecer, {input('Nome: ')}!')