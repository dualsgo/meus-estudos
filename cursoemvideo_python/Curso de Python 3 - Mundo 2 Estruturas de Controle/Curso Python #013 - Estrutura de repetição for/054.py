# Exercício Python #054 - Grupo da Maioridade
# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
from random import randint

atual = date.today().year

pessoas = [randint(1988, 2024) for p in range(6)]

for i, v in enumerate(pessoas, 1):
	idade = atual - v
	print(f'{i}ª pessoa - Idade: {idade} -', 'maior de idade' if idade > 17 else 'menor de idade')