# Exercício Python #034 - Aumentos múltiplos
# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

try:
	salario = float(input('Digite seu salário: R$ '))
except ValueError:
	print(f'Apenas valores numéricos.')
else:
	print(f'{'Salário atual:':<15}{'R$':>3}{salario:>10.2f}')
	print(f'{'AUMENTO':<15}{'10%' if salario < 1250 else '15%':>3}{salario * (0.10 if salario < 1250 else .15):>10.2f}')
	print(f'{'-'*28}')
	print(f'{'Novo salário:':<15}{'R$':>3}{salario * (1.10 if salario < 1250 else 1.15):>10.2f}')