# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from emoji import emojize

def opção():
	while True:
		global escolha
		escolha = int(input(emojize(':memorando: Sua escolha: ', language='pt')))
		if escolha == 1:
			dobro = número * 2
			return dobro
		elif escolha == 2:
			triplo = número * 3
			return triplo
		elif escolha == 3:
			raiz = número ** .5
			return raiz
		else:
			print(emojize(':xis: Opção inválida! :xis:', language='pt'))
			continue

while True:
	try:
		número = int(input(emojize(':memorando: Digite um valor: ', language='pt')))
		print(emojize(f'Escolha uma opção:\n[1] Dobro\n[2] Triplo\n[3] Raiz Quadrada', language='pt'))
		resultado = opção()
		break
	except ValueError:
		print(emojize(':xis: Valor inválido! :xis:', language='pt'))
print(f'Você escolheu: {'Dobro' if escolha == 1 else 'Triplo' if escolha == 2 else 'Raiz quadrada'}')
print(f'{'Número:':<12}{número:>5}\n{'Resultado:':<12}{resultado:>5}')