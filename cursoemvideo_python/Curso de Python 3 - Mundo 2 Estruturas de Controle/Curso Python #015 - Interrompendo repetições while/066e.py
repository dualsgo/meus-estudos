# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


quantidade = soma = 0

while True:
	try:
		número = int(input('Digite um valor: '))

		if número != 999:
			soma += número
			quantidade += 1
		else:
			print(f'Programa encerrado!')
			if quantidade >= 1:
				print(f'Apenas o valor {soma} foi digitado')
			else:
				print(f'Foram digitados {quantidade} valores e a soma entre eles é {soma}')
			break

	except ValueError:
		print('Erro')