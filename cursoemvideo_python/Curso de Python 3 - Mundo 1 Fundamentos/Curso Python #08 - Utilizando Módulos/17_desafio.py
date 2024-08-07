# Exercício Python #017 - Catetos e Hipotenusa - Aula 00 até 08 - Mundo 1
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de uma triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

"""O teorema de Pitágoras descreve a relação entre os lados de um triângulo retângulo. Ele afirma que, para qualquer triângulo retângulo com lados de comprimento a e b, e hipotenusa de comprimento c, a2 + b2 = c2"""

from emoji import emojize
from math import hypot

# Tarefa 1: Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
cateto_oposto = float(input(emojize(':régua_triangular: Digite o comprimento do cateto oposto: ', language='pt')))
cateto_adjacente = float(input(emojize(':régua_triangular: Digite o comprimento do cateto adjacente: ', language='pt')))

# Tarefa 2: Calcular e mostrar o comprimento da hipotenusa.
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f'O comprimento da hipotenusa de cateto oposto {cateto_oposto} e cateto adjacente {cateto_adjacente} é {hipotenusa:.2f}.')


# Versão 2


def comprimento(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido!')


oposto = comprimento('Comprimento do cateto oposto: ')
adjacente = comprimento('Comprimento do cateto adjacente: ')
hipotenusa = (oposto ** 2 + adjacente ** 2) ** .5

print(f'{'Cateto oposto:':<20}{oposto:>10.3g}\n{'Cateto adjacente:':<20}{adjacente:>10.3g}\n{'Hipotenusa:':<20}{hipotenusa:>10.3g}')
