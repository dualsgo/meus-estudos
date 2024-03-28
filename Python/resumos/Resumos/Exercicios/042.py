# Exercício Python #042 - Analisando Triângulos v2.0
# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

while True:
	try:
		a, b, c = float(input('Segmento A: ')), float(input('Segmento B: ')), float(input('SegmentoC: '))
	except ValueError:
		print('Apenas valores numéricos')
	else:
		triangulo = a + b > c and a + c > b and a < b + c
		tipo = 'equilátero' if a == b == c else 'escaleno' if a != b != c != a else 'isósceles'

	print(f'{a}, {b} e {c}', f'formam um triângulo {tipo}!' if triangulo else 'não formam um triângulo!')
	break