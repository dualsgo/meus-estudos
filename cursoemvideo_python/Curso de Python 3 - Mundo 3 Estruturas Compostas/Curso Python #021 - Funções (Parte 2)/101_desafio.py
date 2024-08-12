# Exercício Python #101 - Funções para votação - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def valor_valido(mensagem):
	while True:
		try:
			entrada = int(input(mensagem))
			if 1924 < entrada < 2024:
				return entrada
			else:
				print('Ano fora do intervalo permitido...')
		except ValueError:
			print('Apenas valores numéricos!')


def voto(ano_de_nascimento):
	idade = 2024 - ano_de_nascimento
	if idade < 16:
		print(f'Idade: {idade} anos - Não tem idade suficiente para votar!')
	elif idade == 16 or idade == 17 or idade > 70:
		print(f'Idade: {idade} anos - Voto facultativo!')
	else:
		print(f'Idade: {idade} anos - Voto obrigatório!')


voto(valor_valido('Digite o seu ano de nascimento: '))