# Exercício Python #072 - Número por Extenso
# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
	try:
		print(f"Você digitou o número {extenso[int(input('Digite um valor entre 0 e 20: '))]}")
	except IndexError:
		print('Entre 0 e 20')
		continue
	except ValueError:
		print('Apenas valores numéricos.')
		continue
	break