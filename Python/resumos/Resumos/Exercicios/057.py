# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

condição = True
while condição:
	sexo = input('F ou M ').strip().upper()
	condição = sexo == 'F' or sexo == 'M'
	if condição:
		condição = False
		print('Encerrando...')
	else:
		print('Inválido!')