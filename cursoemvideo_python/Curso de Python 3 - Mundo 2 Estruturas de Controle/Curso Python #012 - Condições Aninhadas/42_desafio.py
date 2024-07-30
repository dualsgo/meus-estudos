# Exercício Python #042 - Analisando Triângulos v2.0 - Aula 00 até 12 - Mundo 2
# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# Tarefa 1: Ler três retas
a = int(input('Digite o valor do segmento A: '))
b = int(input('Digite o valor do segmento B: '))
c = int(input('Digite o valor do segmento C: '))

# Tarefa 2: Avaliar se formam um triângulo
print('\033[1;32mPara que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois\033[m')
triangulo = a < b + c and c < b + a and b < a + c
print(triangulo)
print(f'\033[1mA {a} < B {b} + C {c}')
print(f'B {b} < C {c} + A {a}')
print(f'C {c} < A {a} + B {b}\033[m\n')

# Tarefa 2: Definir as condições para cada topo de triângulo

# EQUILÁTERO: todos os lados iguais
equilatero = a == b == c
# ESCALENO: todos os lados diferentes
escaleno = a != b and b != c and a != c
# ISÓSCELES: dois lados iguais, um diferente
isosceles = not equilatero and not escaleno


if triangulo:
    print(f'\033[1mOs segmentos de comprimento a = {a}, b = {b} e c = {c} podem formar um\033[m', end=' ')
    if equilatero:
        print('\033[1;31mTRIÂNGULO EQUILÁTERO - TODOS OS LADOS IGUAIS\033[m')
    elif escaleno:
        print('\033[1;31mTRIÂNGULO ESCALENO - TODOS OS LADOS DIFERENTES\033[m')
    elif isosceles:
        print('\033[1;31mTRIÂNGULO ISÓSCELES - DOIS LADOS IGUAIS E UM DIFERENTE\033[m')
else:
    print(f'Não é possível formar um triângulo com os segmentos a = {a}, b = {b} e c = {c}.')

# Versão 2 - Mais simple e om validação

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

# Versão mais completa
from emoji import emojize


def segmento_reta(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Erro...')


def verificação(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return True
	else:
		return False


def tipo_triangulo(a, b, c):
	if a == b == c == a:
		return 'EQUILÁTERO'
	elif a != b != c != a:
		return 'ESCALENO'
	else:
		return 'ISÓSCELES'


segmento_a = segmento_reta(emojize(':régua_reta: Comprimento do segmento A: ', language='pt'))
segmento_b = segmento_reta(emojize(':régua_reta: Comprimento do segmento B: ', language='pt'))
segmento_c = segmento_reta(emojize(':régua_reta: Comprimento do segmento C: ', language='pt'))
triangulo = verificação(segmento_a, segmento_b, segmento_c)

print(
	emojize(f'Os segmentos de reta de comprimento \033[1;33m{segmento_a:.3g}, {segmento_b:.3g} e {segmento_c:.3g}\033[m '
			f'{"\033[1;32mPODEM FORMAR :régua_triangular:\033[m" if triangulo else "\033[1;31mNÃO PODEM FORMAR\033[m"} '
			f'um triângulo{f" do tipo {tipo_triangulo(segmento_a, segmento_b, segmento_c)}" if triangulo else "!"}', language='pt')
)