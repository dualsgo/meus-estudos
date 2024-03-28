# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada
# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

try:
	numero = int(input('Digite um valor para ser analisado: '))

except ValueError:
	print("Digite apenas números inteiros.")

else:
	print(
		f'{'Você digitou':<15}{numero:>10}\n'
		f'{'Dobro':<15}{numero * 2:>10}\n'
		f'{'Triplo':<15}{numero * 3:>10}\n'
		f'{'Raiz quadrada':<15}{numero ** .5:>10.2f}')