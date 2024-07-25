# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
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