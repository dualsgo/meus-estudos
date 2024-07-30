# Exercício Python #075 - Análise de dados em uma Tupla - Aula 00 até 16 - Mundo 3
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Importa a função randint da biblioteca random
from random import randint

# Gera uma tupla de 4 números aleatórios entre 0 e 9
numeros = (
    randint(3, 9),
    randint(3, 9),
    randint(3, 9),
    randint(3, 9)
)

print(f'Os números são: ', end='')
for numero in numeros:
    print(numero, end=' ')

print(f'\nO 9 apareceu quantas vezes? {numeros.count(9)}')

mensagem_3 = (f'\033[1;32mO número 3 apareceu no primeiro no índice {numeros.index(3)}.\033[m' if 3 in numeros else '\033[1;31mO número 3 não aparece na tupla.\033[m')
print(mensagem_3)

print('Os números pares são:', end=' ')
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')


# Versão 2 para corrigir

"""while True:
	try:
		tupla = tuple(int(input('Digite um valor: ')) for i in range(5))
		break
	except ValueError:
		print(f'Apenas números inteiros!')


pares = tuple(p for p in tupla if p % 2 == 0)
nove = tupla.count(9) if 9 in tupla else None
três = tupla.index(3) if 3 in tupla else None

print(f'A) Quantas vezes apareceu o valor 9?', f'\033[1;32m{nove} vezes.\033[1m' if nove is not None else f'\033[1;32mNenhuma vez.\033[m')
print(f'B) Em que posição foi digitado o primeiro valor 3?', f'\033[1;32mPosição {três+1}.\033[m' if três is not None else '\033[1;32mElemento não está na tupla.\033[m')
print(f'C) Quais foram os números pares? \033[1;32mForam {pares}\033[m')"""