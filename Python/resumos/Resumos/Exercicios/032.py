
# Exercício Python #032 - Ano Bissexto
# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
from random import randint

atual = date.today().year

for i in range(11):
	ano = randint(2000, 2024)
	bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
	if bissexto:
		print(f'{ano} - É bissexto!')
	else:
		print(f'{ano} - Não é bissexto!')