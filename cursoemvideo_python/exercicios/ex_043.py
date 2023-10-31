"""Desafio 043 -  (Aula 01 a 12): Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""
print("""IMC -ÍNDICE DE MASSA CORPORAL""")
# Ler o peso e a altura em metros
print('Digite o seu peso: Kg')
peso = float(input(''))
print('Digite a sua altura: m')
altura = float(input(''))
# Calcular o IMC
imc = peso / altura ** 2
# Categorizar com base na tabela
print(f'Seu IMC é: {imc:.1f}.')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
