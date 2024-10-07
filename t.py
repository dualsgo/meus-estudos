saldo = 0
extrato = []
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    # Verifica se o valor do depósito é positivo
    if valor > 0:
        # Adiciona o valor ao saldo
        saldo += valor
        # Registra a operação no extrato
        extrato.append(f"Depósito: R$ {valor:.2f}")
        # Exibe mensagem de sucesso
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        # Exibe mensagem de erro se o valor for negativo ou zero
        print("Erro: O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, numero_saques
    if numero_saques < LIMITE_SAQUES:
        if valor > 0:
            if valor <= limite_saque:
                if saldo >= valor:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    numero_saques += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Erro: Saldo insuficiente.")
            else:
                print(f"Erro: O valor do saque excede o limite de R$ {limite_saque:.2f}.")
        else:
            print("Erro: O valor do saque deve ser positivo.")
    else:
        print(f"Erro: Número máximo de saques diários ({LIMITE_SAQUES}) atingido.")

def exibir_extrato():
    print("\n=============== EXTRATO ===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=======================================")

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
