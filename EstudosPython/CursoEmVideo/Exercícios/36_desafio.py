# Exercício Python #036 - Aprovando Empréstimo - Aula 00 até 12
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

# Tarefa 1: Perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar
valor_imovel = int(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos_pagando = int(input('Digite a quantidade de anos que deseja pagar: '))

# Tarefa 2: Verificar se a prestação mensal é maior que 30% do salário
limite = salario * .3
prestacoes = anos_pagando * 12
valor_prestacoes = valor_imovel / prestacoes

if valor_prestacoes > limite:
    print('Não será possível aprovar o seu empréstimo. O valor das prestações é superior ao limite de 30% do seu salário.')
else:
    print('Parabéns! Seu empréstimo foi aprovado. Confira as condições:')
# Tarefa 3: Após a verificação, mostrar se o empréstimo foi aprovado ou negado.
    print(f'O imóvel avaliado em R$ {valor_imovel:.2f} será quitado em {anos_pagando} anos.')
    print(f'Cada uma das {prestacoes} parcelas custará R$ {valor_prestacoes:.2f}.')