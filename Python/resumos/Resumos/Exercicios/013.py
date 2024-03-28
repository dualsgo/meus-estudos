# Exercício Python #013 - Reajuste Salarial
# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

while True:
	try:
		salario = float(input('Digite o valor do salário: R$    '))
	except ValueError:
		print('Valor digitado não é válido!')
	else:

		print(f'{'Salário atual':<24}{'R$':>5}{salario:>10.2f}')
		print(f'{'Percentual de aumento':<24}{'R$':>5}{salario * .15:>10.2f}')
		print(f'{'Salário com aumento':<24}{'R$':>5}{salario * 1.15:>10.2f}')
		break