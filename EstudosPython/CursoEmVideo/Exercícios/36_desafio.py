# Exercício Python #036 - Aprovando Empréstimo - Aula 00 até 12 - Mundo 2
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

# Tarefa 1: Perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar
valor_imovel = int(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos_pagando = int(input('Digite a quantidade de anos que deseja pagar: '))

# Tarefa 2: Verificar se a prestação mensal é maior que 30% do salário
limite = salario * .3
prestacoes = anos_pagando * 12
valor_prestacoes = valor_imovel / prestacoes

if valor_prestacoes >= limite:
    print('\033[1;31mNão será possível aprovar o seu empréstimo. O valor das prestações é superior ao limite de 30% do seu salário.\033[m')
    print(f'Valor das prestações: \033[1;31mR$ {valor_prestacoes:.2f}\033[m')
else:
    print('\033[1;32mParabéns! Seu empréstimo foi aprovado. Confira as condições:\033[m')
# Tarefa 3: Após a verificação, mostrar se o empréstimo foi aprovado ou negado.
    print(f'O imóvel avaliado em \033[1;32mR$ {valor_imovel:.2f}\033[m será quitado em \033[1;32m{anos_pagando}\033[m anos.')
    print(f'Cada uma das \033[1;32m{prestacoes}\033[m parcelas custará \033[1;32mR$ {valor_prestacoes:.2f}\033[m')