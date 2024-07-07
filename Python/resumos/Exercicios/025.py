# Exercício Python #025 - Procurando uma string dentro de outra
# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('Tem "Silva" no nome!' if 'Silva' in input('Digite seu nome: ').strip().title() else 'Não tem "Silva" no nome!')