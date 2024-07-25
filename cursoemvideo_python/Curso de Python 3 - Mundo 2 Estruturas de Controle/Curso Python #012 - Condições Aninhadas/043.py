# Exercício Python #043 - Índice de Massa Corporal
# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida


try:
	peso_kg = float(input('Peso em Kg: '))
	altura_metros = float(input('Altura em metros: '))

except ValueError:
	print(f'Erro! Valores inválidos para essa operação.')

else:
	imc = round(peso_kg / (altura_metros * altura_metros), 2)
	categoria = 'Abaixo do peso' if imc < 18.5 else 'Peso ideal' if imc < 25 else 'Sobrepeso' if imc < 30 else 'Obesidade' if imc < 40 else 'Obesidade mórbida'


	print('-' * 55)
	print(f'|{'Peso (Kg)':^10}|{'Altura (m)':^10}|{'IMC':^10}|{'Categoria':^20}|')
	print('-' * 55)
	print(f'|{peso_kg:^10}|{altura_metros:^10.2f}|{imc:^10}|{categoria:^20}|')
	print('-' * 55)