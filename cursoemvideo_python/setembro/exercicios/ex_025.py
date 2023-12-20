"""Desafio 025 - Procurando uma string dentro de outra (Aula 01 a 09): Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'
"""
# Passo 1: Ler o nome da pessoa
print("""\033[1;42mERA SÓ MAIS UM SILVA...\033[m""")
nome = str(input('Digite o nome da pessoa: ')).strip()

# Passo 2: Verificar se 'SILVA' está no nome ao transformar a string em maíusculas para fazer a comparação independente da forma que for digitada
tem_silva = 'SILVA' in nome.upper()

# Passo 3: Exibir o resultado - Sendo usado condições para exibir strings diferentes em vez de somente True ou False
if tem_silva:
    print('\033[1;33mSim, o nome contém "SILVA".\033[m')
else:
    print('\033[1;36mNão, o nome não contém "SILVA".\033[m')
