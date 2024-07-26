# Exercício Python #044 - Gerenciador de Pagamentos - Aula 00 até 12 - Mundo 2
#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
from emoji import emojize


def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print('Valor não pode ser zero ou negativo.')
        except ValueError:
            print('Tipo de dado inválido.')

valor = obter_valor('Valor da compra: R$ ')

while True:
    try:
        forma_de_pagamento = int(input('Escolha a forma de pagamento: [1] Dinheiro [2] Cartão [3] PIX: '))
        if forma_de_pagamento in [1, 2, 3]:
            break
        else:
            print('Opção inválida!')
    except ValueError:
        print('Tipo de dado inválido.')

if forma_de_pagamento == 1:
    desconto = 0.10
    valor_final = valor - (valor * desconto)
    print('Forma de pagamento: Dinheiro')

elif forma_de_pagamento == 2:
    while True:
        try:
            tipo_cartao = int(input('Tipo de cartão: [1] Débito [2] Crédito: '))
            if tipo_cartao in [1, 2]:
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Tipo de dado inválido.')

    if tipo_cartao == 1:
        desconto = 0.10
        valor_final = valor - (valor * desconto)
        print('Forma de pagamento: Cartão Débito')

    elif tipo_cartao == 2:
        while True:
            try:
                cartao_credito = int(input('Opção de crédito: [1] À Vista [2] Parcelado: '))
                if cartao_credito in [1, 2]:
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Tipo de dado inválido.')

        if cartao_credito == 1:
            desconto = 0.05
            valor_final = valor - (valor * desconto)
            print('Forma de pagamento: Cartão Crédito à Vista')

        elif cartao_credito == 2:
            while True:
                try:
                    parcelamento = int(input('Parcelamento: [1] 2X Sem Juros [2] 3X até 10X com Juros: '))
                    if parcelamento in [1, 2]:
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('Tipo de dado inválido.')

            if parcelamento == 1:
                valor_final = valor
                parcela = valor / 2
                print('Forma de pagamento: Cartão Crédito Parcelado em 2X Sem Juros')

            elif parcelamento == 2:
                while True:
                    try:
                        parcelas = int(input('Número de parcelas (3 a 10): '))
                        if 3 <= parcelas <= 10:
                            break
                        else:
                            print('Opção inválida!')
                    except ValueError:
                        print('Tipo de dado inválido.')

                total_com_juros = valor + (valor * 0.20)
                valor_final = total_com_juros
                parcela = total_com_juros / parcelas
                print(f'Forma de pagamento: Cartão Crédito Parcelado em {parcelas}X com Juros')

elif forma_de_pagamento == 3:
    desconto = 0.10
    valor_final = valor - (valor * desconto)
    print('Forma de pagamento: PIX')

print(f'{"Valor:":<15} R$ {valor:.2f}')
if forma_de_pagamento != 2 or (forma_de_pagamento == 2 and tipo_cartao == 2 and parcelamento == 1):
    print(f'{"Desconto:":<15} R$ {valor * desconto:.2f}')
print(f'{"Valor final:":<15} R$ {valor_final:.2f}')

if forma_de_pagamento == 2 and tipo_cartao == 2 and cartao_credito == 2:
    print(f'{"Valor da parcela:":<15} R$ {parcela:.2f}')
    print(f'{"Número de parcelas:":<15} {parcelas}')