# Exercício Python #030 - Par ou Ímpar? - Aula 00 até 09 - Mundo 1
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from random import randint
# Tarefa 1: Sortear um número
numero = randint(0, 99)

# Tarefa 2: Verificar se é par ou ímpar
par = numero % 2 == 0

print(f"O número {numero} é PAR!" if par else f'O número {numero} é ÍMPAR!')

# Versão 2 - Com validação

while True:
	try:
		número = int(input('Digite um valor (diferente de zero): '))
		if not número:
			continue
		print(f'{número} é', '\033[1;31mÍMPAR\033[m' if número % 2 else '\033[1;32mPAR\033[m')
		break
	except ValueError:
		print('Valor de tipo não válido para essa operação.')