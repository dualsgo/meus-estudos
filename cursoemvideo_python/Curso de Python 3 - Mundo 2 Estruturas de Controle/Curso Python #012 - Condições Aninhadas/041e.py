# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
from emoji import emojize


def obtem_idade(mensagem):
	while True:
		try:
			ano_nascimento = int(input(mensagem))
			if 1980 <= ano_nascimento <= 2015:
				return ano_nascimento
			else:
				print("O ano deve estar entre 1980 e 2015")
		except ValueError:
			print('Apenas números são aceitos')


ano_atual = date.today().year
idade = ano_atual - obtem_idade('Digite o seu ano de nascimento: ')

categorias = emojize(
	f'MIRIM :bebê:' if idade < 10
	else 'INFANTIL :criança:' if idade < 14
	else 'JÚNIOR :menino:' if idade < 19
	else 'SÊNIOR :pessoa:' if idade < 25
	else 'MASTER :homem_cabelo_branco:', language='pt')

print(f'{'Idade:':<10}{idade:>15}\n{'Categoria:':<10}{categorias:>15}')