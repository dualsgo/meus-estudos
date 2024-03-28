# Exercício Python #050 - Soma dos pares
# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

from random import randint

valores = [randint(1, 10) for i in range(6)]
pares = [v for v in valores if v % 2 == 0]
print(f'A soma entre os {len(pares)} valores pares adicionados é {sum(pares)}.')
for v, i in enumerate(valores):
	print(f'\033[31m{i}\033[m' if i in pares else f'{i}', end=', ' if v < len(valores)-1 else '.')