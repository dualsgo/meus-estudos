# Exercício Python #043 - Índice de Massa Corporal - Aula 00 até 12 - Mundo 2
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre sua posição, conforme a tabela abaixo:

# O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m), conforme a seguinte fórmula: IMC = peso / (altura x altura). O resultado de IMC é dado em kg/m 2.

# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

# Tarefa 1: Receber o peso e a altura para calcular o imc
peso = float(input('Digite seu peso: Kg'))
altura = float(input('Digite sua altura em metros: m'))


# Tarefa 2: Formar a tabela com as condições para categorizar o imc
imc = peso / (altura * altura)
print(f'Seu IMC é {imc:.1f}.', end= ' ')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
# Tarefa 3: Exibir o resultado