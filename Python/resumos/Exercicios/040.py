# Exercício Python #040 - Aquele clássico da Média
# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

while True:
	try:
		media = (float(input('Nota 1: ')) + float(input('Nota 2: '))) / 2
	except ValueError:
		print('Valores inválidos.')
	else:
		print(f'Média: {media}', 'APROVADO' if media >= 7 else 'RECUPERAÇÃO' if media >= 5 else 'REPROVADO')
		break