# Exercício Python #081 - Extraindo dados de uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


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

print(f'A lista com {len(lista_de_valores)} valores em ordem decrescente é: ')
lista_de_valores.sort(reverse=True)
for i, v in enumerate(lista_de_valores, 1):
	print(v, end=', ' if i < len(lista_de_valores) else '.')
print(f'\nO valor 5 {f'não ' if 5 not in lista_de_valores else ''}está na lista!')