# Exercício Python #010 - Conversor de Moedas - Aula 00 até 07 - Mundo 1
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

# 1 USD = 5,56 BRL
# 1 EUR = 6,05 BRL

from emoji import emojize

while True:
	try:
		BRL = float(input(emojize(':cifrão: Digite o valor em BRL: ', language='pt')))
		USD = BRL / 5.56
		EUR = BRL / 6.05

		print(emojize(f'''Na cotação atual (03/07/2024):
:dinheiro_voando: {BRL:.2f} BRL
:nota_de_dólar: {USD:.2f} USD
:nota_de_euro: {EUR:.2f} EUR''', language='pt'))
		break

	except ValueError:
		print(f'Valor inválido!')

# Fazer um conversor com menu

def menu():
	while True:
		try:
			escolha = int(input(f'Qual a moeda: [1] Real [2] Dólar [3] Euro\n'))
			while escolha != 1 and escolha != 2 and escolha != 3:
				print('Apenas 1, 2 ou 3')
				escolha = int(input(f'Qual a moeda: [1] Real [2] Dólar [3] Euro\n'))

			else:
				print('Prosseguindo...')
				while True:
					try:
						print(f'Converter {valor_monetario:.2f} para qual moeda:')
						if escolha == 1:
							opção = int(input('[1] Dólar [2] Euro\n'))
						elif escolha == 2:
							opção = int(input('[1] Real [2] Euro\n'))
						elif escolha == 3:
							opção = int(input('[1] Real [2] Euro\n'))
						else:
							print('Opção inválida')
							continue
						break
					except ValueError:
						print('Opção inválida!')
				return escolha, opção
		except:
			print('Tipo de dado inválido')


def valor(msg):
	while True:
		try:
			return float(input(msg))
		except ValueError:
			print('Tipo de dado inválido')


def conversão(v, e, o):

	if e == 1:
		print(f'{valor_monetario:.2f} BRL = ', end='')
		if o == 1:
			print('USD ', end='')
			return v / 5.56
		elif o == 2:
			print('EUR ', end='')
			return v / 5.90
	elif e == 2:
		print(f'{valor_monetario:.2f} USD = ', end='')
		if o == 1:
			print('BRL ', end='')
			return v / 0.18
		elif o == 2:
			print('EUR ', end='')
			return v / 0.92
	elif e == 3:
		print(f'{valor_monetario:.2f} EUR = ', end='')
		if o == 1:
			print('BRL ', end='')
			return v / 0.17
		elif o == 2:
			print(f'USD ', end='')
			return v / 1.09

valor_monetario = valor('Digite o valor: ')
de, para = menu()
valor_convertido = conversão(valor_monetario, de, para)
print(f'{valor_convertido:.2f}')

# Versão 2

while True:
    carteira = float(input('Digite quanto possui na carteira: R$ '))
    print('Qual moeda deseja converter?')
    print('[1] R$ - Real')
    print('[2] U$ - Dólar')
    print('[3]  € - Euro')
    converter = int(input(''))
    while converter == 1 or 2 or 3:
        if converter == 1:
            print('Deseja converter R$ - Real para qual moeda?')
            print('[1] U$ - Dólar')
            print('[2]  € - Euro')
            para = int(input(''))
            if para == 1:
                print('Converter R$ - Real para U$ - Dólar')
                cotacao_dolar = 4.90
                dolar = carteira / cotacao_dolar
                print(
                    f'Você possui R$ {carteira:.2f}. Na cotação atual (US$ 1,00 = R$ 3.27) você pode comprar US$ {dolar:.2f}.')
            continuar = int(input('[1] Continuar ou [2] Encerrar'))
            while continuar != 1 or 2:
                print('Opção inválida!')
                continuar = int(input('[1] Continuar ou [2] Encerrar'))
                if continuar == 2:
                    print('Encerrando o programa!')
                    break
                else:
                    continue


carteira = float(input('Digite quanto possui na carteira: R$ '))

cotacao_dolar = 4.90
cotacao_euro = 5.36
cotacao_peso = 72.89

dolar = carteira / cotacao_dolar
euro = carteira / cotacao_euro
peso = carteira * cotacao_peso

print(f'Você possui R$ {carteira:.2f}. Na cotação atual (US$ 1,00 = R$ 3.27) você pode comprar US$ {dolar:.2f}.')
print('')
print(f'Você possui R$ {carteira:.2f}. Na cotação atual (1,00 € = R$ 5.36) você pode comprar {euro:.2f} €.')
print('')
print(f'R$ {carteira:.2f} equivalem a $ {peso:.2f} pesos argentinos.')