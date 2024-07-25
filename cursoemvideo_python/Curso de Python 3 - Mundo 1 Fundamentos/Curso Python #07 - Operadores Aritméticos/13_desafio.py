# Exercício Python #013 - Reajuste Salarial - Aula 00 até 07 - Mundo 1
# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

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

# Versão 2


while True:
	try:
		salario = float(input('Digite o valor do salário: R$    '))
	except ValueError:
		print('Valor digitado não é válido!')
	else:

		print(f'{'Salário atual':<24}{'R$':>5}{salario:>10.2f}')
		print(f'{'Percentual de aumento':<24}{'R$':>5}{salario * .15:>10.2f}')
		print(f'{'Salário com aumento':<24}{'R$':>5}{salario * 1.15:>10.2f}')
		break

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

# Versão 2 

produto = str(input("Nome do produto: ")).strip().title()

while True:
	try:
		preco = float(input("Valor do produto: R$ "))
		qtde_parcelas = int(input("Quantidade de parcelas:\n1 À vista ou 2 até 12x com juros "))

		while qtde_parcelas not in range(1, 12):
			qtde_parcelas = int(input('Digite novamente: '))

		if qtde_parcelas == 1:
			print(
				f"\n{'Descrição do produto:':<25}{produto:>10}\n"
				f"{'-' * 35}\n"
				f"{'Valor:':<20}{'R$':>5}{preco:>10.2f}\n"
				f"{'Desconto à vista:':<20}{'(%)':>5}{'10':>10}\n"
				f"{'Valor do desconto:':<25}{preco * .1:>10.2f}\n"
				f"{'-' * 35}\n"
				f"{'Valor final:':<20}{'R$':>5}{preco * .9:>10.2f}\n")

		elif 1 < qtde_parcelas <= 12:
			valor_parcela = preco / qtde_parcelas

			# Taxa de juros
			taxa = 4 + qtde_parcelas
			juros_ao_mes = taxa / qtde_parcelas

			preco_juros = preco + (preco * taxa / 100)

			# Parcela com juros
			parcelas_juros = valor_parcela * juros_ao_mes
			#
			total = preco_juros + parcelas_juros

			print(
				f"\n{'Produto:':<10}{produto:>25}\n"
				f"{'-' * 35}\n"
				f"{'Valor:':<20}{'R$':>5}{preco:>10.2f}\n"
				f"{'Taxa de juros:':<20}{'(%)':>5}{taxa:>10.2f}\n"
				f"{'-' * 35}\n"
				f"{'Valor final:':<20}{'R$':>5}{preco_juros:>10.2f}\n"
				f"{'-' * 35}\n"
				f"{'Nº de parcelas:':<20}{'R$':>5}{qtde_parcelas:>10.0f}\n"
				f"{'Juros ao mês:':<20}{'(%)':>5}{juros_ao_mes:>10.2f}\n"
				f"{'Valor por parcela:':<20}{'R$':>5}{parcelas_juros:>10.2f}\n"
				f"{'-' * 35}\n")

		break

	except ValueError:
		print('O valor fornecido não é válido. Digite novamente... ')