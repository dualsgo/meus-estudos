# Exercício Python #063 - Sequência de Fibonacci v1.0
# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

termos = int(input('Digite a quantidade de termos que quer visualizar: '))

primeiro_termo = 0
segundo_termo = 1
contador = 0

while contador < termos:
    print(primeiro_termo, end=' ⮕ ' if contador < termos-1 else ' ⮕ FIM!')
    primeiro_termo, segundo_termo = segundo_termo, primeiro_termo + segundo_termo
    contador += 1

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