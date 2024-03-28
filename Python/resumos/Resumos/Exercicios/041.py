# Python Exercício #041 - Classificando Atletas
# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year

repetir = True
while repetir:
	try:
		idade = atual - int(input('Digite o ano de nascimento: '))
	except ValueError:
		print('Ano de nascimento inválido: ')
	else:
		categoria = 'MIRIM' if idade < 10 else 'INFANTIL' if idade < 14 else 'JÚNIOR' if idade < 19 else 'SÊNIOR' if idade < 25 else 'MASTER'

	if 4 < idade < 81:
		print(f'Idade: {idade} ANOS - Categoria: {categoria}')
		repetir = False
	else:
		print(f'Idade fora do intervalo permitido (5 ATÉ 80 ANOS). ')