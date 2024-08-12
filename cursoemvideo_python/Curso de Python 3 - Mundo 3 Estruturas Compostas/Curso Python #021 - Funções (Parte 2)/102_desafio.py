# Exercício Python #102 - Função para Fatorial - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def valor_valido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')


def mostrar():
	while True:
		print('Exibir o cálculo?')
		continuar = input('[S] SIM [N] NÃO').strip().upper()
		if continuar not in ['S', 'N']:
			print('Digite S ou N')
		else:
			if continuar == 'S':
				return True
			else:
				return False


def fatorial(valor, mostrar_calculo):
	"""
	Calcula o fatorial de um número
	:param valor: número a ser calculado
	:param mostrar_calculo: exibe ou não o cálculo
	"""
	resultado = 1
	if mostrar_calculo:
		print(f'{valor}! = ', end='')
		for i in range(valor, 0, -1):
			print(i, end=' x ' if i > 1 else f' = ')
			resultado *= i
		print(resultado)
	else:
		for i in range(valor, 0, -1):
			resultado *= i
		print(f'{valor}! = {resultado}')


fatorial(valor_valido('Digite o número a calcular... '), mostrar())