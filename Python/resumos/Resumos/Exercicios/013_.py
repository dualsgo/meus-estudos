produto = str(input("Nome do produto: ")).strip().title()

while True:
	try:
		preco = float(input("Valor do produto: R$ "))
		qtde_parcelas = int(input("Quantidade de parcelas:\n1 À vista ou 2 até 12x com juros "))

	except ValueError:
		print('O valor fornecido não é válido. Digite novamente... ')


	else:
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