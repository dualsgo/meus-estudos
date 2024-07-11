# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

while True:
	try:
		nome = input('Digite o seu nome completo: ').strip().title()

		if nome.replace(' ', '').isalpha():
			primeiro, último = nome.split()[0], nome.split()[-1]
			print(
				f'{'Nome:':<10}{nome:^{len(nome)}}\n'
				f'{'Primeiro:':<10}{primeiro:.<{len(nome)}}\n'
				f'{'Último:':<10}{último:.>{len(nome)}}')
		else:
			print('Somente caracteres alfabéticos e espaço (Não pode estar em branco ou conter somente espaço)')
			continue

		break
	except Exception:
		print('ERRO! Tente novamente.')