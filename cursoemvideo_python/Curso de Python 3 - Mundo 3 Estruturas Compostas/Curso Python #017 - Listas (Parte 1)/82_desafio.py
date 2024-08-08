# Exercício Python #082 - Dividindo valores em várias listas - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


def obter_valores_válidos(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido!')


lista_de_valores = []
while True:
	lista_de_valores.append(obter_valores_válidos('Digite um valor: '))
	while True:
		continuar = input('Outro valor? S/N ').strip().upper()
		if continuar in 'SN':
			break

	if continuar == 'N':
		break


pares = [valor for valor in lista_de_valores if valor % 2 == 0]
ímpares = [valor for valor in lista_de_valores if valor not in pares]

print('Lista principal:')
for i, v in enumerate(lista_de_valores, 1):
	print(v, end=', ' if i < len(lista_de_valores) else '.')
print('\nLista de números pares:')
for i, v in enumerate(pares, 1):
	if pares:
		print(v, end=', ' if i < len(pares) else '.')
	else:
		print('Lista vazia!')
print('\nLista de números ímpares:')
for i, v in enumerate(ímpares, 1):
	if ímpares:
		print(v, end=', ' if i < len(ímpares) else '.')
	else:
		print('Lista vazia!')