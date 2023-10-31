"""Desafio 037 -  (Aula 01 a 12): Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base numérica da conversão.
- 1. Binário
- 2. Octal
- 3. Hexadecimal
"""
# Pré definindo as cores em um dicionário
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}
print("""
      CONVERTENDO VALORES DECIMAIS""")
# Receber o numero digitado pelo usuário
numero = int(input('Digite um número: '))
# Dar ao usuário as opções disponíveis
opcao = int(input(f"""
Escolha a base numérica para comverter o número {cor["green"]}{numero}{cor["fecha"]}:
{cor["destaque"]}1 - BINÁRIO{cor["fecha"]}
{cor["destaque"]}2 - OCTAL{cor["fecha"]}
{cor["destaque"]}3 - HEXADECIMAL{cor["fecha"]}
"""))

# EXTRA - Validação para garantir que utilize uma das opções sugeridas
while opcao == 0 or opcao >= 4:
    opcao = int(input(f"""
{cor["red"]}Você digitou uma opção inválida!{cor["fecha"]}
    
Escolha a base numérica para comverter o número {cor["destaque"]}{numero}{cor["fecha"]}:
{cor["destaque"]}1 - BINÁRIO{cor["fecha"]}
{cor["destaque"]}2 - OCTAL{cor["fecha"]}
{cor["destaque"]}3 - HEXADECIMAL{cor["fecha"]}
"""))
print(f'Você escolheu a opção {cor["green"]}{opcao}{cor["fecha"]}.')

# Converter utilizando funções integradas
if opcao == 1:
    print(f'{cor["green"]}{numero}{cor["fecha"]} em binário é {cor["green"]}{bin(numero)}{cor["fecha"]}.')
elif opcao == 2:
    print(f'{cor["green"]}{numero}{cor["fecha"]} em octal é {cor["green"]}{oct(numero)}{cor["fecha"]}.')
elif opcao == 3:
    print(f'{cor["green"]}{numero}{cor["fecha"]} em hexadecimal é {cor["green"]}{hex(numero)}{cor["fecha"]}.')
    
# EXTRA - Método sem as funções integradas
