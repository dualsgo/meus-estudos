# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def valor_válido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido para essa operação!')


def sorteia_valores(quantidade_valores, inicio_intervalo, fim_intervalo):
	if inicio_intervalo >= fim_intervalo:
		print('Valores padrão para início e fim serão considerados: ')
		inicio_intervalo, fim_intervalo = 1, 100
	lista_valores = [randint(inicio_intervalo, fim_intervalo) for i in range(quantidade_valores)]
	return lista_valores


def somar_valores_pares(lista_valores_sorteados):
	soma_valores = 0
	valores_considerados = list()
	for valor_lista in lista_valores_sorteados:
		if valor_lista % 2 == 0:
			valores_considerados.append(valor_lista)
			soma_valores += valor_lista

	return soma_valores, valores_considerados


total_pares, lista_pares = somar_valores_pares(sorteia_valores(valor_válido('Digite a quantidade de valores que deseja sortear (Valor padrão é 5): '), valor_válido('Digite o início do intervalo (Valor padrão é 1):'), valor_válido('Digite o fim do intervalo (Valor padrão é 100): ')))

print('Os valores pares considerados foram: ')
for i, valor in enumerate(lista_pares, 1):
	print(valor, end=', ' if i < len(lista_pares) else '.\n')
print(f'A soma dos {len(lista_pares)} valores pares é {total_pares}.')