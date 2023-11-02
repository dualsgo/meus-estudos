"""Desafio 043 - Índice de massa corporal  (Aula 01 a 12): Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}

print(f"""{cor['destaque']}IMC -ÍNDICE DE MASSA CORPORAL{cor['fecha']}""")
# Ler o peso e a altura em metros
print('Digite o seu peso: Kg')
peso = float(input(''))
print('Digite a sua altura: m')
altura = float(input(''))

# Calcular o IMC
imc = peso / altura ** 2
print(f'{cor["destaque"]}Seu IMC é: {cor["green"]}{imc:.2f}{cor["fecha"]}')

# Categorizar com base na tabela
if imc < 17:
    print(f'{cor["destaque"]}Você está{cor["fecha"]} {cor["yellow"]}MUITO ABAIXO DO PESO{cor["fecha"]}')
elif imc < 18.49:
    print(f'{cor["destaque"]}Você está{cor["fecha"]} {cor["yellow"]}ABAIXO DO PESO{cor["fecha"]}')
elif imc < 24.99:
    print(f'{cor["destaque"]}Você está no{cor["fecha"]} {cor["green"]}PESO IDEAL{cor["fecha"]}')
elif imc < 29.99:
    print(f'{cor["destaque"]}Você está com{cor["fecha"]} {cor["yellow"]}SOBREPESO{cor["fecha"]}')
elif imc < 34.99:
    print(f'{cor["destaque"]}Você se enquadra em{cor["fecha"]} {cor["red"]}OBESIDADE I{cor["fecha"]}')
elif imc < 39.99:
    print(f'{cor["destaque"]}Você se enquadra em{cor["fecha"]} {cor["red"]}OBESIDADE II - SEVERA{cor["fecha"]}')
else:
    print(f'{cor["destaque"]}Você se enquadra em{cor["fecha"]} {cor["red"]}OBESIDADE III - MÓRBIDA{cor["fecha"]}')
