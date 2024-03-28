# Exercício Python #007 - Média Aritmética
# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

try:
	primeira_nota = float(input('Digite a primeira nota: '))
	segunda_nota = float(input('Digite a segunda nota: '))
	media = (primeira_nota + segunda_nota) / 2

except Exception as e:
	print(f'Ocorreu o erro: {e}')

else:
	print(
		f'{'Primeira nota:':<15}{primeira_nota:>15}\n'
		f'{'Segunda nota:':<15}{segunda_nota:>15}\n'
		f'{'-' * 30}\n'
		f'{'A média é:':<15}{media:>15.2f}')