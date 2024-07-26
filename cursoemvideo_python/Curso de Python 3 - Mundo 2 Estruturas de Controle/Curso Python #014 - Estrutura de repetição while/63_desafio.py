# Exercício Python #063 - Sequência de Fibonacci v1.0 - Aula 00 até 14 - Mundo 2
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

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

"""
for i in range(termos):

	if i == 0:
		a = i
		print(a, end=' - ')
	elif i == 1:
		b = i
		print(b, end=' - ')
	else:
		termo = a + b
		a = b
		b = termo
		print(termo, end=' ⮕ ' if i < termos-1 else ' ⮕ FIM!')"""