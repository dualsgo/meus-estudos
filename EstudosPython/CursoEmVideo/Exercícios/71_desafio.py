# Exercício Python #071 - Simulador de Caixa Eletrônico - Aula 00 até 15 - Mundo 2
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


from emoji import emojize

# Mensagem de boas-vindas
print(emojize(':banco::moeda: BANCO GUANABARA :moeda::banco:', language='pt'))

# Solicita ao usuário o valor desejado para saque
valor_saque = int(input(emojize(':símbolo_de_caixa_automático: Quanto deseja sacar? R$ ', language='pt')))

# Variável para armazenar a quantidade de cédulas
cedulas = 0

# Loop para calcular as cédulas necessárias
while True:
    if valor_saque >= 100:
        cedulas = valor_saque // 100
        valor_saque %= 100
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 100', language='pt'))

    elif valor_saque >= 50:
        cedulas = valor_saque // 50
        valor_saque %= 50
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 50', language='pt'))

    elif valor_saque >= 20:
        cedulas = valor_saque // 20
        valor_saque %= 20
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 20', language='pt'))

    elif valor_saque >= 10:
        cedulas = valor_saque // 10
        valor_saque %= 10
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 10', language='pt'))

    elif valor_saque >= 5:
        cedulas = valor_saque // 5
        valor_saque %= 5
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 5', language='pt'))

    elif valor_saque >= 2:
        cedulas = valor_saque // 2
        valor_saque %= 2
        print(emojize(f':nota_de_dólar: Sacando {cedulas} cédulas de R$ 2', language='pt'))

    else:
        # Quando não há mais cédulas a serem sacadas, encerra o loop
        print(emojize(':rosto_com_cifrões: RETIRE O SEU DINHEIRO', language='pt'))
        break

# Mensagem de agradecimento ao usuário por utilizar os serviços do banco
print(emojize('Obrigado por utilizar os nossos serviços!', language='pt'))


