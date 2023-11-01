"""Desafio 044 - Gerenciador de pagamentos (Aula 01 a 12): Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- dinheiro/pix: 10% de desconto
- crédito à vista/débito: 5% de desconto
- Parcelado 2X no cartão: Sem juros
- Parcelado 3X até 10X: 20% de juros"""
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}

# Solicitar o valor
print('Digite o valor da sua compra:')
valor = float(input('R$ '))
# Solicitar a forma de pagamento
metodo = int(input(f"""
Selecione a forma de pagamento: 
{cor['destaque']}[1]{cor['fecha']} - {cor['green']}Dinheiro/PIX{cor['fecha']}
{cor['destaque']}[2]{cor['fecha']} - {cor['yellow']}Cartão{cor['fecha']}

"""))
# Exibir os valores atualizados baseados na forma de pagamento
print(f'{cor["destaque"]}O valor da sua compra foi{cor["fecha"]} {cor["green"]}R$ {valor:.2f}{cor["fecha"]}\n')
if metodo == 1:
    print(f'{cor["green"]}Pagando em DINHEIRO ou PIX você recebe 10% DE DESCONTO!{cor["fecha"]}\n')
    print(f'{cor["destaque"]}O valor da sua compra fica{cor["fecha"]} {cor["green"]}R$ {valor - (valor * .1):.2f}{cor["fecha"]}')
elif metodo == 2:
    print(f'{cor["destaque"]}Você escolheu pagamento em cartão. Selecione a opção desejada: {cor["fecha"]}')
    forma = int(input(f"""
{cor['destaque']}[1]{cor['fecha']} - {cor['green']}Débito{cor['fecha']}
{cor['destaque']}[2]{cor['fecha']} - {cor['yellow']}Crédito{cor['fecha']}

"""))
    if forma == 1:
        print(f'{cor["green"]}Pagando no cartão de DÉBITO você recebe 5% DE DESCONTO!{cor["fecha"]}\n')
        print(f'{cor["destaque"]}O valor da sua compra fica{cor["fecha"]} {cor["green"]}R$ {valor - (valor * .05):.2f}{cor["fecha"]}')
    else:
        credito = int(input(f"""
{cor['destaque']}[1]{cor['fecha']} - {cor['green']}À vista{cor['fecha']}
{cor['destaque']}[2]{cor['fecha']} - {cor['yellow']}Parcelado{cor['fecha']}

"""))
        if credito == 1:
            print(f'{cor["green"]}Pagando no cartão de CRÉDITO À VISTA você recebe 5% DE DESCONTO!{cor["fecha"]}\n')
            print(f'{cor["destaque"]}O valor da sua compra fica{cor["fecha"]} {cor["green"]}R$ {valor - (valor * .05):.2f}{cor["fecha"]}')
        else:
            parcelamento = int(input(f"""
{cor['destaque']}[1]{cor['fecha']} - {cor['green']}2 vezes sem juros{cor['fecha']}
{cor['destaque']}[2]{cor['fecha']} - {cor['yellow']}3 a 10 vezes com juros{cor['fecha']}

"""))
            if parcelamento == 1:
                print(
                    f'{cor["yellow"]}Pagando no cartão de crédito parcelado em 2 vezes não há desconto nem cobrança de juros!{cor["fecha"]}')
                print(
                    f'{cor["destaque"]}O valor da sua compra é{cor["fecha"]} {cor["green"]}R$ {valor:.2f}{cor["fecha"]} {cor["destaque"]}e cada parcela será de{cor["fecha"]} {cor["green"]}R$ {valor / 2:.2f}{cor["fecha"]}')
            else:
                parcelas = int(input(f'{cor["destaque"]}Digite o número de parcelas: 3 a 10{cor["fecha"]}'))
                print(f'{cor["red"]}Pagando no cartão de crédito parcelado de 3 a 10 vezes serão cobrados 20% de juros!{cor["fecha"]}')

                print(f"""
{cor['destaque']}O valor da sua compra é{cor['fecha']} {cor['green']}R$ {valor:.2f}{cor['fecha']}
{cor['destaque']}O valor final da compra com 20% de juros será{cor['fecha']} {cor['red']}R$ {valor + (valor * .2):.2f}{cor['fecha']}
{cor['destaque']}Parcelando em{cor['fecha']} {cor['red']}{parcelas}{cor['fecha']} {cor['destaque']}vezes com juros, cada parcela será{cor['fecha']} {cor['red']}R$ {(valor + (valor * .2)) / parcelas:.2f}{cor['fecha']}""")
else:
    print('OPÇÃO INVÁLIDA!')
    metodo = int(input(f"""Selecione a forma de pagamento: 
{cor['destaque']}[1]{cor['fecha']} - {cor['green']}Dinheiro/PIX{cor['fecha']}
{cor['destaque']}[2]{cor['fecha']} - {cor['yellow']}Cartão{cor['fecha']}

"""))
