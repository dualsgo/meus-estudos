# Exercício Python #035 - Analisando Triângulo v1.0
# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Para formar um triângulo, a soma de cada dois lados deve ser sempre maior que a medida do terceiro lado

while True:
	try:
		a, b, c = float(input('A: ')), float(input('B: ')), float(input('C: '))
	except ValueError:
		print('Apenas valores numéricos: ')
	else:
		triangulo = a + b > c and a + c > b and a < b + c

	print(f'{a}, {b} e {c}', 'formam um triângulo!' if triangulo else 'não formam um triângulo!')
	break