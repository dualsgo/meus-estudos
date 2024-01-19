# Exercício Python #044 - Gerenciador de Pagamentos - Aula 00 até 12 - Mundo 2
from emoji import emojize
#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print(emojize(':loja_de_conveniência: Lojas Guanabara', language='pt'))
# Tarefa 1: Receber o valor original e selecionar a forma de pagamento
valor_original = float(input('Digite o valor da compra: R$ '))
print(emojize('Escolha a forma de pagamento:', language='pt'))
print(emojize(':tecla_1: à vista dinheiro/cheque :nota_de_dólar:', language='pt'))
print(emojize(':tecla_2: à vista no cartão :cartão_de_crédito:', language='pt'))
print(emojize(':tecla_3: em até 2x no cartão :cartão_de_crédito:', language='pt'))
print(emojize(':tecla_4: 3x ou mais no cartão :cartão_de_crédito:', language='pt'))
escolha = int(input(''))
valor_final = valor_original
# Tarefa 2: Definir as condições para cada forma de pagamento
if escolha == 1:
    print('Você terá 10% de desconto')
    valor_final = valor_original - (valor_original * .1)
elif escolha == 2:
    print('Você terá 5% de desconto')
    valor_final = valor_original - (valor_original * .05)
elif escolha == 3:
    print('Você não terá desconto')
    valor_final = valor_original
    parcelas = 2
    valor_parcelado = valor_final / parcelas
    print(f'Parcelamento: {parcelas} vezes de R$ {valor_parcelado:.2f}')
elif escolha == 4:
    print('Você terá acréscimo de 20% de juros')
    print('Em quantas parcelas? 4 até 10 vezes')
    parcelas = int(input(''))
    valor_final = valor_original + (valor_original * .2)
    valor_parcelado = valor_final / parcelas
    print(f'Parcelamento: {parcelas} vezes de R$ {valor_parcelado:.2f}')
else:
    print('Escolha inválida!')
print(f'O valor final é R$ {valor_final:.2f}')

desconto = valor_original - valor_final
if desconto > 0:
    print(f'Desconto de R$ {desconto:.2f}')
elif desconto < 0 and escolha != 3:
    desconto = valor_final - valor_original
    print(f'Acréscimo de R$ {desconto:.2f}')
# Tarefa 3: Exibir o valor final