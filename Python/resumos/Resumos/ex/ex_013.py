# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

from emoji import emojize

while True:
	try:
		salário = float(input(emojize(':cifrão: Digite o salário: R$ ', language='pt')))
		aumento = salário * .15
		salário_com_aumento = salário + aumento
		print(emojize(f':nota_de_dólar:{'Salário atual:':<18}\033[1;32mR${salário:>10.2f}\033[m\n:nota_de_dólar:{'Aumento 15%':<18}\033[1;32mR${aumento:>10.2f}\033[m\n{'-' * 30}\n:dinheiro_voando:{'Novo salário:':<18}\033[1;32mR${salário_com_aumento:>10.2f}\033[m', language='pt'))
		break
	except ValueError:
		print('Valor inválido! Tente novamente.')

# EXTRA: Leia o preço de um produto e mostre o valor dele a vista com 10% de desconto e parcelado com 8% de aumento.

total_a_pagar = 0

while True:
	try:
		preço = float(input(emojize(':cifrão: Digite o valor do produto: R$ ', language='pt')))
		break
	except ValueError:
		print('Valor inválido!')


while True:
	try:
		forma_de_pagamento = int(input('[1] A vista (Desconto de 10%)\n'
									   '[2] Parcelado (Acréscimo de 8%)'))
		if forma_de_pagamento == 1:
			print(f'Será descontado 10%')
			total_a_pagar = preço * .9
		elif forma_de_pagamento == 2:
			print(f'Será cobrado 8% de juros')
			total_a_pagar = preço * 1.08
		else:
			print(f'Opção inválida')
			continue
		break

	except ValueError:
		print(f'Valor inválido!')

print(emojize(f':nota_de_dólar:{'Preço:':<18}\033[1;32mR${preço:>10.2f}\033[m\n{'-' * 30}\n:dinheiro_voando:{'Novo preço:':<18}\033[1;32mR${total_a_pagar:>10.2f}\033[m', language='pt'))