"""Desafio 010 - Conversor de moedas (Aula 01 a 07): Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considerar US$ 1,00 = R$ 3,27"""

# Passo 1: Ler um valor fornecido pelo usuário - Para isso iremos armazenar o valor digitado pelo usuário em uma variável, convertendo a string para float
print("""
\033[7m$$$$$$$$$$$$$$$$$$$$$$$\033[m
\033[7m$$\033[m \033[1mC O N V E R S O R\033[m \033[7m$$\033[m
\033[7m$$$$$$$$$$$$$$$$$$$$$$$\033[m""")
print('Digite o valor que possui em R$ (REAL/BRL)')
carteira = float(input(''))

# Passo 2: Converter o valor realizando a operação matemática correspondente - Para isso criaremos uma variável que irá armazenar o resultado do cálculo

real = carteira  # Armazena o valor que digitado pelo usuário
dolar = 3.27  # Armazena o valor atual do dolar em real
convertido = real / dolar  # Armazena a conversão

# Passo 3: Exibir o resultado - As variáveis estão formatadas para exibir duas casas decimais
print(f"""
\033[1mVocê possui\033[1m \033[1;32mR$ {real:.2f}.\033[m
\033[1mNa cotação atual você consegue comprar\033[m \033[1;31mU$ {convertido:.2f}.\033[m
""")
