# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome_completo = input('Digite o seu nome: ').strip().title()
nome_separado = nome_completo.split()

maiúsculas = nome_completo.upper()
minúsculas = nome_completo.lower()
tamanho_nome = len(''.join(nome_separado))
tamanho_primeiro_nome = len(nome_separado[0])

print(f'{'Em MAIÚSUCULAS:':<20}{maiúsculas:>30}')
print(f'{'Em minúsuculas:':<20}{minúsculas:>30}')
print(f'{'Tamanho do nome completo:':<30}{tamanho_nome:>20}')
print(f'{'Tamanho do primeiro nome:':<30}{tamanho_primeiro_nome:>20}')