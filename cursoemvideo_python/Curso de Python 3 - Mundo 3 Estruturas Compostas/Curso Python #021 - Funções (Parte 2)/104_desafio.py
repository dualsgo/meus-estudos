# Exercício Python #104 - Validando entrada de dados em Python - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leia_int(mensagem):
	while True:
		valor = input(mensagem)
		try:
			float(valor)
			print(f'Você digitou o valor: {valor}')
			break
		except ValueError:
			print('Este valor não é um número.')


leia_int('Digite um valor inteiro: ')