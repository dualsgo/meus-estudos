# Função para obter um valor numérico válido
def obter_valor_valido(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print("\033[1;31mValor inválido para essa operação. Tente novamente.\033[m")


# Função para converter o valor numérico para formato monetário
def converter_valor(valor_numerico):
	return f'{valor_numerico:.2f}'


# Funções para editar texto e moldura
def centralizar_texto(texto):
	print(f'{texto:^40}')


def molduras():
	print('-' * 40)


# Função para exibir menu
def menu():
	molduras()
	centralizar_texto('Banco Fictício')
	molduras()
	print('[1] Saque')
	print('[2] Depósito')
	print('[3] Extrato')
	molduras()


# Função para exibir o extrato
def exibir_extrato(saldo, depositos, saques):
	molduras()
	print(f'Saldo atual: R$ {converter_valor(saldo)}')
	molduras()

	print(f'Lista de saques:')
	for i, saque in enumerate(saques, 1):
		print(f'Saque {i} - R$ {converter_valor(saque)}')
	molduras()

	print(f'Lista de Depósitos:')
	for i, deposito in enumerate(depositos, 1):
		print(f'Depósito {i} - R$ {converter_valor(deposito)}')
	molduras()


# Função para escolher uma opção
def tipo_de_operacao(mensagem):
	valor_selecionado = obter_valor_valido(mensagem)

	while valor_selecionado not in [1, 2, 3]:
		print('\033[1;31mOpção inválida. Tente novamente.\033[m')
		valor_selecionado = obter_valor_valido(mensagem)

	return valor_selecionado


# Função com a operação de saque (correções feitas)
def sacando(saldo, saques, limite_saque, max_saques):
	valor_saque = obter_valor_valido('Valor que deseja sacar: R$ ')

	# Adicionada verificação de saldo e limite de saques
	if valor_saque > limite_saque:
		print(f"\033[1;31mO valor máximo permitido para saque é R$ {converter_valor(limite_saque)}.\033[m")
	elif valor_saque > saldo:
		print("\033[1;31mSaldo insuficiente para realizar o saque.\033[m")
	elif len(saques) >= max_saques:
		print(f"\033[1;31mVocê atingiu o limite máximo de {max_saques} saques diários.\033[m")
	else:
		print(f'Sacando R$ {converter_valor(valor_saque)}')
		saldo -= valor_saque
		saques.append(valor_saque)
	return saldo, saques


# Função com a operação de depósito (correções feitas)
def depositando(saldo, depositos):
	valor_deposito = obter_valor_valido('Valor que deseja depositar: R$ ')
	print(f'Depositando R$ {converter_valor(valor_deposito)}')
	saldo += valor_deposito
	depositos.append(valor_deposito)
	return saldo, depositos


# Função com as operações
def operacoes(opcao, saldo, saques, depositos, limite_saque, max_saques):
	if opcao == 1:
		molduras()
		centralizar_texto("SAQUE")
		molduras()
		saldo, saques = sacando(saldo, saques, limite_saque, max_saques)

	elif opcao == 2:
		molduras()
		centralizar_texto("DEPÓSITO")
		molduras()
		saldo, depositos = depositando(saldo, depositos)

	elif opcao == 3:
		molduras()
		centralizar_texto("EXTRATO")
		molduras()
		exibir_extrato(saldo, depositos, saques)

	return saldo, saques, depositos


def continuar(mensagem):
	while True:
		escolha = input(mensagem)

		if escolha.upper() == 'S':
			return True
		elif escolha.upper() == 'N':
			return False
		else:
			print('Opção inválida. Tente novamente.')


# Código principal (ajustes feitos)
saldo_conta = 2000
limite_saque = 500
max_saques = 3
lista_saques = []
lista_depositos = []

while True:
	menu()

	# Chamar a função de operações passando as variáveis necessárias
	opcao = tipo_de_operacao('Escolha a opção desejada: ')
	saldo_conta, lista_saques, lista_depositos = operacoes(opcao, saldo_conta, lista_saques, lista_depositos, limite_saque, max_saques)

	# Perguntar se o usuário deseja continuar
	if not continuar('Deseja continuar? S ou N: '):
		print('Obrigado por utilizar os nossos serviços!')
		break