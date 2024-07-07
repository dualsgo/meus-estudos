# Exercício Python #075 - Análise de dados em uma Tupla
# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
while True:
	try:
		tupla = tuple(int(input('Digite um valor: ')) for i in range(5))
	except ValueError:
		print(f'Apenas números inteiros!')
		continue
	else:
		break


pares = tuple(p for p in tupla if p % 2 == 0)
nove = tupla.count(9) if 9 in tupla else None
três = tupla.index(3) if 3 in tupla else None

print(f'A) Quantas vezes apareceu o valor 9?', f'\033[1;32m{nove} vezes.\033[1m' if nove is not None else f'\033[1;32mNenhuma vez.\033[m')
print(f'B) Em que posição foi digitado o primeiro valor 3?', f'\033[1;32mPosição {três+1}.\033[m' if três is not None else '\033[1;32mElemento não está na tupla.\033[m')
print(f'C) Quais foram os números pares? \033[1;32mForam {pares}\033[m')