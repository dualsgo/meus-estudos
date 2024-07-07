# Exercício Python #036 - Aprovando Empréstimo
# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado


try:
	valor_imovel = float(input('Digite o valor do imóvel: R$'))
	renda = float(input('Digite o valor do salário: R$'))
	prazo_anos = int(input('Prazo em anos: '))
except ValueError:
	print('Valores inválidos para essa operação.')
else:
	anos_meses = prazo_anos * 12
	parcelas = valor_imovel / anos_meses
	limite = renda * .3
	verifica = limite >= parcelas

	if verifica:
		print(f'Aprovado')
		print(f'{'Valor imóvel:':<15}{'R$':>5}{valor_imovel:>10.2f}')
		print(f'{'Prazo (meses):':<15}{anos_meses:>9}{' meses':>6}')
		print(f'{'Valor parcelas:':<15}{'R$':>5}{parcelas:>10.2f}')

	else:
		print(f'Recusado')