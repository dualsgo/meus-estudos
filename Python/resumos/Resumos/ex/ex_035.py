# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# a soma das medidas de dois deles é sempre maior que a medida do terceiro

def segmento_reta(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Erro...')

def verificação(a, b, c):
		return '\033[1;32mPODEM FORMAR\033[m' if a + b > c and a + c > b and b + c > a else '\033[1;31mNÃO PODEM FORMAR\033[m'



segmento_a = segmento_reta('Comprimento do segmento A: ')
segmento_b = segmento_reta('Comprimento do segmento B: ')
segmento_c = segmento_reta('Comprimento do segmento C: ')
triangulo = verificação(segmento_a, segmento_b, segmento_c)

print(f'Os segmentos de reta de comprimento \033[1;33m{segmento_a:.3g}, {segmento_b:.3g} e {segmento_c:.3g}\033[m {triangulo} um triângulo!')