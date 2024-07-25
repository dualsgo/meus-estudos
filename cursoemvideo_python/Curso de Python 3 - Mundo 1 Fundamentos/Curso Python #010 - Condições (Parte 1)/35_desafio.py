# Exercício Python #035 - Analisando Triângulo v1.0 - Aula 00 até 09 - Mundo 1
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# b + c > a
from random import randint
# Tarefa 1: Ler três retas
a = randint(1, 99)
b = randint(1, 99)
c = randint(1, 99)

# Tarefa 2: Avaliar se formam um triângulo
print('Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois')
triangulo = b + c > a and b + a > c and a + c > b

print(f'A {a} + B {b} > C {c}')
print(f'B {b} + C {c} > A {a}')
print(f'C {c} + A {a} > B {b}')

if triangulo:
    print(f'Os segmentos de comprimento a={a}, b={b} e c={c} podem formar um triângulo!')
else:
    print(f'Não é possível formar um triângulo com os segmentos a={a}, b={b} e c={c}.')
    
    
# Versão 2 - Com validaçãO

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