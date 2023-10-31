"""Desafio 044 -  (Aula 01 a 12): Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- dinheiro/pix: 10% de desconto
- crédito à vista/débito: 5% de desconto
- Parcelado 2X no cartão: Sem juros
- Parcelado 3X até 10X: 20% de juros"""

# Solicitar o valor
print('Digite o valor da sua compra:')
valor = float(input('R$ '))
# Solicitar a forma de pagamento
metodo = int(input("""
Selecione a forma de pagamento: 
[1] - Dinheiro/PIX
[2] - Cartão

"""))
# Exibir os valores atualizados baseados na forma de pagamento
print(f'O valor da sua compra foi R$ {valor:.2f}\n')
if metodo == 1:
    print('Pagando em DINHEIRO ou PIX você recebe 10% DE DESCONTO!\n')
    print(f'O valor da sua compra fica R$ {valor - (valor * .1):.2f}')
elif metodo == 2:
    print('Você escolheu pagamento em cartão. Selecione a opção desejada: ')
    forma = int(input("""
[1] - Débito
[2] - Crédito

"""))
    if forma == 1:
        print('Pagando no cartão de DÉBITO você recebe 5% DE DESCONTO!\n')
        print(f'O valor da sua compra fica R$ {valor - (valor * .05):.2f}')
    else:
        credito = int(input("""
[1] - À vista
[2] - Parcelado

"""))
        if credito == 1:
            print('Pagando no cartão de CRÉDITO À VISTA você recebe 5% DE DESCONTO!\n')
            print(f'O valor da sua compra fica R$ {valor - (valor * .05):.2f}')
        else:
            parcelamento = int(input("""
[1] - 2 vezes sem juros
[2] - 3 a 10 vezes com juros

"""))
            if parcelamento == 1:
                print(
                    'Pagando no cartão de crédito parcelado em 2 vezes não há desconto nem cobrança de juros!')
                print(
                    f'O valor da sua compra é R$ {valor:.2f} e cada parcela será de R$ {valor / 2:.2f}')
            else:
                parcelas = int(input('Digite o número de parcelas: 3 a 10'))
                print(
                    'Pagando no cartão de crédito parcelado de 3 a 10 vezes serão cobrados 20% de juros!')
                print(f"""
O valor da sua compra é R$ {valor:.2f}
O valor final da compra com 20% de juros será R$ {valor + (valor * .2):.2f}
Parcelando em {parcelas} vezes com juros, cada parcela será R$ {(valor + (valor * .2)) / parcelas:.2f}""")
else:
    print('OPÇÃO INVÁLIDA!')
    metodo = int(input("""Selecione a forma de pagamento: 
1 - Dinheiro/PIX
2 - Cartão

"""))
