# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

flag = 999
contador = soma = 0

while True:
	try:
		print(f'{'-'*30}')
		número = int(input('\033[1mDigite um valor:\033[m \033[7;37;40m 999 encerra \033[m '))

		if número == flag:
			print(f'Programa encerrado!')
			print(f'{'-' * 30}')
			if contador:
				if contador == 1:
					print(f'Apenas um valor foi digitado! Foi o valor {soma}')
				elif contador > 1:
					print(f'Foram digitados {contador} valores! A soma entre eles é {soma}')
			else:
				print(f'Nenhum valor foi digitado!')
			break

		contador += 1
		soma += número
		print(f'{'-'*30}')
		print(f'{f'{contador}º valor: {número}':^30}')
		print(f'{f'A soma é {soma}':^30}')

	except ValueError:
		print('Este valor não e válido para essa operação.')