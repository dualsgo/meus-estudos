# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

while True:
	try:
		elementos = int(input('Digite a quantidade de elementos que deseja visualizar: '))
		primeiro = 0
		segundo = 1
		enéssimo = elementos
		for e in range(enéssimo):
			próximo = primeiro + segundo
			print(primeiro, end=' - ' if e < enéssimo -1 else ' - FIM!')
			primeiro, segundo = segundo, primeiro + segundo
		break
	except ValueError:
		print('Este valor é de um tipo inválido para essa operação. Tente novamente')