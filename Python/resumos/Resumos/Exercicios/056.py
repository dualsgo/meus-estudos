# Exercício Python #056 - Analisador completo4
# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

média_idade = 0
nome_velho = ''
idade_velho = 0
quantidade_mulheres = 0

while True:
	try:
		for i in range(1, 5):
			print('-' * 10)
			print(f'{i}ª pessoa:')
			print('-' * 10)
			nome = input('Digite o nome: ').strip().title()
			sexo = input('Digite o sexo: ').strip().upper()
			idade = int(input('Digite a idade: '))
	except ValueError:
		print(f'Você indicou um valor inválido. Revise...')

	else:
		if sexo == 'F' and idade < 20:
			quantidade_mulheres += 1
		if sexo == 'M' and idade > idade_velho:
			nome_velho = nome
			idade_velho = idade

		média_idade += idade
		break

print(f'A média de idade do grupo é {média_idade / 4} anos.')
print(f'O homem mais velho é o {nome_velho} com {idade_velho} anos.')
print(f'Ao todo temos {quantidade_mulheres} mulheres com menos de 20 anos.')