# Exercício Python #044 - Gerenciador de Pagamentos
# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


valor = float(input('Valor a ser pago: R$ '))
print(
"""
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros
""")
forma = int(input(''))

print(f'Valor da compra: R$ {valor:.2f} ', end='')
if forma == 1:
	desconto = .1
	final = valor * desconto
	print(f'à vista dinheiro/cheque: 10% de desconto')
	print(f'Valor do desconto: R$ {valor * desconto:.2f}')
	print(f'Valor a ser pago: R$ {valor - final:.2f}')

if forma == 2:
	desconto = .05
	final = valor * desconto
	print(f'à vista no cartão: 5% de desconto')
	print(f'Valor do desconto: R$ {valor * desconto:.2f}')
	print(f'Valor a ser pago: R$ {valor - final:.2f}')

if forma == 3:
	parcelas = valor / 2
	print(f'em até 2x no cartão: preço formal')
	print(f'Valor por parcela: 2 vezes de R$ {parcelas:.2f}')
	print(f'Valor a ser pago: R$ {valor:.2f}')

if forma == 4:
	parcelamento = int(input('Parcelas: 3 até 12 '))
	juros = valor * .2
	final = valor + (valor * .2)
	parcelas = final / parcelamento
	print(f'3x ou mais no cartão: 20% de juros')
	print(f'Valor dos juros: R$ {juros:.2f}')
	print(f'Valor por parcela: {parcelamento} vezes de R$ {parcelas:.2f}')
	print(f'Valor a ser pago: R$ {final:.2f}')