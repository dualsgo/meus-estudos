# Exercício Python #022 - Analisador de Textos - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

# Tarefa 1: Ler o nome completo
nome = str(input('Digite seu nome completo: ')).strip().title()
print(nome)

# Tarefa 2: Mostrar as informações solicitadas

# Em maísculas
em_maiusculas = nome.upper()
print(f'{nome} em MAIÚSUCULAS é: {em_maiusculas}')

# Em minúsculas
em_minusculas = nome.lower()
print(f'{nome} em mínusculas é: {em_minusculas}')

# Quantidade de letras do nome completo
nome_separado = nome.split()
primeiro_nome = nome_separado[0] # Definindo primeiro nome
comprimento_primeiro_nome = len(primeiro_nome)
nome_junto = ''.join(nome_separado)
comprimento_nome = len(nome_junto)
print(f'Desconsiderando os espaços, {nome} tem {comprimento_nome} letras.')

# Quantidade de letras do primeiro nome
print(f'O primeiro nome é {primeiro_nome} e possui {comprimento_primeiro_nome} letras.')