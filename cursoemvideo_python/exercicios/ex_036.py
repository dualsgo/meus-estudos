"""Desafio 036 - (Aula 01 a 12): Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado."""

# Pré definindo as cores em um dicionário
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'fecha': '\033[m',
    'destaque': '\033[7m'}

print(f"""
      {cor["destaque"]}SIMULE O SEU EMPRÉSTIMO IMOBILIÁRIO{cor["fecha"]}
      """)
# Recebendo as informações necessária
valor_imovel = float(
    input(f'Digite o valor do imóvel: {cor["green"]}R$ {cor["fecha"]}'))
salario = float(
    input(f'Digite o valor do seu salário: {cor["green"]}R$ {cor["fecha"]}'))
anos = int(input(f'Digite o prazo que deseja pagar em anos: '))
# EXTRA - Pergunta ao usuário se possui valor de entrada. Converte o valor digitado para bool. Dessa forma se nada for digitado (ao pressionar enter) a string vazia será convertida para o equivalente a False
entrada = bool(input(
    'Possui valor de entrada? Digite 1 para sim caso contrário pressione ENTER'))
# Caso seja digitado algo (mesmo que não seja o numero sugerido no texto) acondiçã oserá atendida
if entrada:
    # a variável irá novamente solicitar que seja digitado o valor e deduzirá esse valor no valor do imovel que foi atribuido anteriormente
    entrada = float(input('Digite o valor da entrada: R$ '))
    valor_imovel -= entrada
# Salvamos o limite do valor das prestaçoes em uma variavel para fins de entendimento
limite_prestacao = salario * 0.3
# Calculamos o valor de cada prestação dividindo o valor total pela quantidade de meses. Considerando que recebemos o valor em anos precisamos multiplicar por 12
prestacao_mensal = valor_imovel / (anos * 12)
# Acaliamos se o valor das prestações é menor, igual ou maior que o limite e exibimos a mensagem correspondente
if prestacao_mensal <= limite_prestacao:
    print(
        f'{cor["green"]}O empréstimo foi aprovado. As parcelas mensais serão de R$ {prestacao_mensal:.2f}{cor["fecha"]}.')
else:
    print(f'{cor["red"]}O empréstimo não pode ser aprovado. O valor das parcelas mensais excede 30% do seu salário{cor["fecha"]}.')
