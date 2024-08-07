# Exercício Python #034 - Aumentos múltiplos - Aulas 00 até 09 - Mundo 1
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Simulador de aumento')
# Tarefa 1: Perguntar o salário de um funcionário
salario_atual = float(input('Digite o seu salário atual: R$ '))

# Tarefa 2: Calcular o valor do aumento
quinze_porcento = salario_atual <= 1250
dez_porcento = salario_atual > 1250

# Se for menor ou igual a 1250, aumenta 15%
if quinze_porcento:
    aumento = 0.15
    print('Seu aumento será de 15%')
# Se for maior que 1250, aumenta 10%
else:
    aumento = 0.10
    print('Seu aumento será de 10%')

novo_salario = salario_atual + (salario_atual * aumento)
print(f'O seu salário de R$ {salario_atual:.2f} com aumento será R$ {novo_salario:.2f}')

# Versão 2 - Com validação

salário = 0
while salário <= 0:
	try:
		salário = float(input('Digite o valor do salário: R$ '))
		aumento = .15 if salário <= 1250 else .10
		print(
			f'{'Salário atual:':<20}R${salário:>8.2f}\n'
			f'{'Aumento:':<20}{aumento:>10.2%}\n'
			f'{'Valor do aumento':<20}R${salário*aumento:>8.2f}\n'
			f'{'-' * 30}\n'
			f'{'Salário atualizado:':<20}R${salário * (1+aumento):>8.2f}')
	except ValueError:
		print(f'Apenas valores numéricos.')
