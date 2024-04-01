# Exercício Python #081 - Extraindo dados de uma Lista
# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
	try:
		valor = int(input('Valor: '))
	except ValueError:
		print(f'Valor inválido')
		continue
	lista.append(valor)
	continuar = ''
	while continuar not in ('S', 'N'):
		continuar = input('Continuar? S/N ').strip().upper()

	if continuar == 'S':
		continue
	if continuar == 'N':
		break

print(f'Quantidade de valores: {len(lista)}')
print(f'Lista em ordem decrescente: {', '.join(sorted(lista, reverse=True))}')
print(f'O valor 5', f'foi digitado!' if 5 in lista else f'não foi digitado')