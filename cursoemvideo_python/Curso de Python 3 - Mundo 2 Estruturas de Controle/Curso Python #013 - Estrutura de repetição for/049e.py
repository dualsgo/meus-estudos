# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

def tabuada(mensagem):
	while True:
		try:
			fator = int(input(mensagem))
			for i in range(1, 11):
				print(f'{fator:^3} x {i:^3} = {fator * i:3}')
			break
		except ValueError:
			print('Valor de tipo inválido.')


tabuada('Digite o valor que deseja verificar a tabuada: ')