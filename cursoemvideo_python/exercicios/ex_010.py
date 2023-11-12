"""Desafio 010 - Conversor de moedas (Aula 01 a 07): Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considerar US$ 1,00 = R$ 3,27"""

# Passo 1: Ler um valor fornecido pelo usuário - Para isso iremos armazenar o valor digitado pelo usuário em uma variável, convertendo a string para float
print("""
\033[7;43m$$$$$$$$$$$$$$$$$$$$$$$\033[m
\033[7;42m$$\033[m \033[1mC O N V E R S O R\033[m \033[7;43m$$\033[m
\033[7;42m$$$$$$$$$$$$$$$$$$$$$$$\033[m""")
print('Digite o valor que possui em R$ (REAL/BRL)')
carteira = float(input(''))

# Passo 2: Converter o valor realizando a operação matemática correspondente - Para isso criaremos uma variável que irá armazenar o resultado do cálculo

real = carteira  # Armazena o valor que digitado pelo usuário
# Calcula a quantidade de dólares que a pessoa pode comprar dividindo o valor em reais pela taxa de câmbio (R$ 4,94 por dólar).
dolar = real / 4.94
# Calcula a quantidade de euros que a pessoa pode comprar dividindo o valor em reais pela taxa de câmbio (R$ 5,33 por euro).
euro = real / 5.33
real_dolar = real / dolar  # Armazena a conversão
real_euro = real / euro


# Passo 3: Exibir o resultado - As variáveis estão formatadas para exibir duas casas decimais
print(f"""
\033[1mVocê possui\033[1m \033[1;32mR$ {real:.2f}.\033[m
\033[1mNa cotação atual você consegue comprar\033[m \033[1;31mU$ {real_dolar:.2f}\033[m
\033[1mNa cotação atual você consegue comprar\033[m \033[1;31m € {real_euro:.2f}\033[m

""")
