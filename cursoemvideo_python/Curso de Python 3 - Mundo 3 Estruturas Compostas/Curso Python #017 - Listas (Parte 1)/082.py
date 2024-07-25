# Exercício Python #082 - Dividindo valores em várias listas
# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
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

pares = [valor for valor in lista if valor % 2 == 0]
ímpares = [valor for valor in lista if valor % 2]

print(f'Lista: {lista}')
print(f'Pares: {pares}')
print(f'ímpares: {ímpares}')