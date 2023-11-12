""" Desafio 004 - Dissecando uma variável (Aulas 01 a 06): Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele."""

# Passo 1: Ler algo pelo teclado. Para isso utilizamos uma vriável para armazenar os dados que serão inseridos através de uma função input()
print('\033[42mDigite algo:\033[m')
valor_digitado = input('')
# Passo 2: Exibir as informações. Para isso iremos criar um print com uma string formatada e usaremos os métodos aplicáveis.
# Observação: Iniciar a impressão de uma string formatada com três aspas triplas permite que a string abranja várias linhas e contenha substituições de variáveis.

# Verifica se a string inserida é numérica.
if valor_digitado.isnumeric():
    # Se for numérica, converte para um número inteiro.
    valor_inteiro = int(valor_digitado)
    print(f'O valor digitado é do tipo int: {valor_inteiro}')
    if valor_inteiro > 0:
        print(f'É um número inteiro positivo.')
    elif valor_inteiro < 0:
        print(f'É um número inteiro negativo.')
    else:
        print('É um número inteiro igual a zero.')
elif valor_digitado.replace('.', '', 1).isdigit():
    # Se for numérica com um único ponto decimal, converte para float.
    valor_float = float(valor_digitado)
    print(f'O valor digitado é do tipo float: {valor_float}')
    if valor_float > 0:
        print(f'É um número de ponto flutuante positivo.')
    elif valor_float < 0:
        print(f'É um número de ponto flutuante negativo.')
    else:
        print('É um número de ponto flutuante igual a zero.')
else:
    # Se não for numérica, exibe como uma string.
    print(f'O valor digitado é do tipo str: {valor_digitado}')
    print(f"""
    \033[31mO tipo de dado inserido é: {type(valor_digitado)}.\033[m
    \033[32mO valor só tem espaços? {valor_digitado.isspace()}.\033[m
    \033[33mO valor é numérico? {valor_digitado.isnumeric()}.\033[m
    \033[34mO valor é alfabético? {valor_digitado.isalpha()}.\033[m
    \033[35mO valor é alfanumérico? {valor_digitado.isalnum()}.\033[m
    \033[36mO VALOR ESTÁ EM MÍUSCULAS? {valor_digitado.isupper()}.\033[m
    \033[37mo valor está em minúsculas? {valor_digitado.islower()}.\033[m
    \033[38mO Valor Está Capitalizado? {valor_digitado.istitle()}.\033[m
    """)

