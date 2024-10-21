# OPERAÇÃO DE DEPÓSITO
# Valores positivos
# Armazenar depósitos em uma variável
# Exibir os depósitos no extrato

# OPERAÇÃO DE SAQUE
# Permitir no máximo 3 saques com limite de 500 reais por saque
# Caso o usuário não tenha saldo, deve exibir uma mensagem informando que não é possível sacar
# Armazenar os saques em uma variável para exibir no extrato

# EXTRATO
# Listar depósitos e saques
# Exibir saldo atualizado
# Exibir os valores no formato R$ XXX.XX,XX


def main():
     # Função para obter valores válidos
    def obter_valor_valido(mensagem_exibida):
        while True:
            try:
                return float(mensagem_exibida)
            except ValueError:
                print('O valor digitado não é válido para essa operação!')


    # Função para converter os valores para forma monetária
    def converter_valor(valor_para_converter):
        return f'R$ {valor_para_converter:.2f}'


    # Função para listar os elementos da lista de saques ou depósitos
    def exibir_itens_lista(lista):
        for indice, elemento in enumerate(lista, 1):
            print(f'{indice} - {elemento}')


    def cabecalho():
            print('-' * 40)
            print('BANCO IMAGINÁRIO'.center(40))
            print('-' * 40)
            
            
    def molduras(operacao):
            print('-' * 40)
            print(operacao)
            print('-' * 40)
    
    
    def opcoes():
        print('Escolha a opção desejada:')
        print('[1] Saque\n[2] Depósito\n[3] Extrato')

                
    def escolha(texto):
        while True:
            try:
                return int(input(texto))
            except ValueError:
                print('Opção inválida!')
    
    def exibir_menu():
        while True:
            cabecalho()
            molduras(opcoes())
            escolha('Digite a opção desejada: ')
            
            if escolha == 1:
                print('SAQUE')
            elif escolha == 2:
                print('DEPÓSITO')
            else:
                print('EXTRATO')







main()