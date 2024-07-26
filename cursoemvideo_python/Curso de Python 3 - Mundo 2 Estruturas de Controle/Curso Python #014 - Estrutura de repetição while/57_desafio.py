# Exercício Python #057 - Validação de Dados - Aula 00 até 14 - Mundo 2
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

condição = True
while condição:
	sexo = input('F ou M ').strip().upper()
	condição = sexo == 'F' or sexo == 'M'
	if condição:
				# Sendo F ou M
		print('\033[1;35mSexo feminino registrado com sucesso!\033[m' if sexo == 'F' else '\033[1;34mSexo masculino registrado com sucesso!\033[m')
		print('Programa finalizado!')
		condição = False
		print('Encerrando...')
	else:
		print('Sexo inválido. Digite novamente: M ou F ')


