# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = 0
while salário <= 0:
	try:
		salário = float(input('Digite o valor do salário: R$ '))
		aumento = .10 if salário < 1250 else .15
		print(
			f'{'Salário atual:':<20}R${salário:>8.2f}\n'
			f'{'Aumento:':<20}{aumento:>10.2%}\n'
			f'{'Valor do aumento':<20}R${salário*aumento:>8.2f}\n'
			f'{'-' * 30}\n'
			f'{'Salário atualizado:':<20}R${salário * (1+aumento):>8.2f}')
	except ValueError:
		print(f'Apenas valores numéricos.')