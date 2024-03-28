# Exercício Python #022 - Analisador de Textos
# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome para analise: ').strip().title().split()

print(f'{'Nome digitado:':<20}{' '.join(nome):>30}')
print(f'{'Quantidade letras:':<20}{len(''.join(nome)):>30}')
print(f'{'Nome MAIÚSCULO:':<20}{' '.join(nome).upper():>30}')
print(f'{'Nome MINÚSCULO:':<20}{' '.join(nome).lower():>30}')
print(f'{'Primeiro nome:':<20}{nome[0]:>30}')
print(f'{'Quantidade letras:':<20}{len(nome[0]):>30}')




"""nome = input('Digite o seu nome para analisarmos: ').strip()

tamanho_nome = len(nome) - nome.count(' ')
primeiro_nome = nome[:nome.find(' ')].title()

print(f'{'O seu nome completo é:':<25}{nome.title():>25}')
print(f'Seu nome tem {tamanho_nome} letras')
print(f'{'Em maiúsculas:':<25}{nome.upper():>25}')
print(f'{'Em minúsculas:':<25}{nome.lower():>25}')
print(f'{'Seu primeiro nome é:':<25}{primeiro_nome:>25}')
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras')
"""