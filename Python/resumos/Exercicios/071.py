# Exercício Python #071 - Simulador de Caixa Eletrônico
# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

saque = int(input('Digite o valor que deseja: R$'))
cinquenta = vinte = dez = um = 0
resto = saque
while resto != 0:
	if resto >= 50:
		cinquenta = resto // 50
		resto = saque % 50
		print(f'{cinquenta} cédulas de R$ 50,00')

	if resto >= 20:
		vinte = resto // 20
		resto = saque % 20
		print(f'{vinte} cédulas de R$ 20,00')

	if resto >= 10:
		dez = resto // 10
		resto = saque % 10
		print(f'{dez} cédulas de R$ 10,00')

	if 0 < resto < 10:
		um = resto // 1
		resto = saque % 1
		print(f'{um} cédulas de R$ 1,00')