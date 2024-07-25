# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida


def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Tipo de dado inválido.')

peso = obter_valor('Digite o peso em Kg: ')
while 0 > peso or peso > 200:
    print('Peso inválido!')
    peso = obter_valor('Digite o peso em Kg: ')

altura = obter_valor('Digite a altura em cm: ')
while 0 > altura or altura > 300:
    print('Altura inválida!')
    altura = obter_valor('Digite a altura em cm: ')

if altura >= 100:
    altura = altura / 100

imc = round(peso / (altura * altura), 2)

categoria = (
    'Abaixo do peso' if imc < 18.5 else
    'Peso ideal' if imc < 25 else
    'Sobrepeso' if imc < 30 else
    'Obesidade' if imc < 40 else
    'Obesidade mórbida'
)

print(f'{"Peso:":<10}{f"{peso:.2f} Kg":>20}')
print(f'{"Altura:":<10}{f"{altura:.2f} m":>20}')
print(f'{"IMC:":<10}{imc:>20}')
print('-' * 30)
print(f'{"Categoria:":<10}{categoria:>20}')