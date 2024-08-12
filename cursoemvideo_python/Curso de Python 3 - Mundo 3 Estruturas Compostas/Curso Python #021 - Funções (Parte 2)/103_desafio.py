# Exercício Python #103 - Ficha do Jogador - Aula 00 até 21 - Mundo 3
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def nome_valido(mensagem):
	while True:
		entrada = input(mensagem).strip().title()
		if entrada.replace(' ', '').isalpha():
			return entrada
		else:
			print('Nome inválido. Nao são permitidos números nem caracteres especiais.')


def valor_valido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')


def ficha(nome, gols):
	print(f'{'-'*33}')
	print(f'|{'JOGADOR':^15}|{'GOLS MARCADOS':^15}|')
	print(f'{'-'*33}')
	print(f'|{nome:^15}|{gols:^15}|')
	print(f'{'-'*33}')


ficha(nome_valido('Digite o nome do jogador: '), valor_valido('Digite a quantidade de gols marcados: '))