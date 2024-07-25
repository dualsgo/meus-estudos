# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-o mostrando uma mensagem na tela:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais


def obter_valor(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Tipo de dado inválido para essa operação.')


primeiro = obter_valor('Digite o primeiro valor: ')
segundo = obter_valor('Digite o segundo valor: ')
verificação = 'O primeiro valor é o maior!' if primeiro > segundo else 'O segundo valor é o maior' if primeiro < segundo else 'Os valores são iguais!'
print(verificação)