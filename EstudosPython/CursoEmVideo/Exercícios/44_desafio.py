# Exercício Python #044 - Gerenciador de Pagamentos
#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

# Tarefa 1: Receber o valor original e selecionar a forma de pagamento
valor_original = float(input('Digite o valor da compra: R$ '))
print('Escolha a forma de pagamento:')
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
escolha = int(input(''))
valor_final = valor_original
# Tarefa 2: Definir as condições para cada forma de pagamento
if escolha == 1:
    valor_final = valor_original - (valor_original * .1)
    print('[1] à vista dinheiro/cheque: 10% de desconto')
elif escolha == 2:
    valor_final = valor_original - (valor_original * .05)
    print('[2] à vista no cartão: 5% de desconto')
elif escolha == 3:
    valor_final = valor_original
    print('[3] em até 2x no cartão: preço formal')
elif escolha == 4:
    valor_final = valor_original + (valor_original * .2)
    print('[4] 3x ou mais no cartão: 20% de juros')
else:
    print('Escolha inválida!')
print(f'O valor final é R$ {valor_final:.2f}')

desconto = valor_original - valor_final
if desconto > 0:
    print(f'Desconto de R$ {desconto:.2f}')
else:
    desconto = valor_final - valor_original
    print(f'Acréscimo de R$ {desconto:.2f}')
# Tarefa 3: Exibir o valor final