# Exercício Python #003 - Somando dois números
# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

termo1 = int(input('Digite o primeiro valor: '))
termo2 = int(input('Digite o segundo valor: '))

soma = termo1 + termo2

print(f'\n{termo1:>10}\n{'+':<5}{termo2:>5}\n{'-'*10}\n'f'{soma:>10}')