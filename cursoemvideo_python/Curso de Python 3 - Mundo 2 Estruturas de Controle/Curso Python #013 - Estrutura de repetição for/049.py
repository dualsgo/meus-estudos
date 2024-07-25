# Exercício Python #049 - Tabuada v.2.0
# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

v = int(input('Digite o valor: '))
for a in range(1, 11):
	print(f'{v:2} x {a:2} = {v*a:2}')