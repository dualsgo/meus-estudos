# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = soma = maior = menor = 0
condição = True
while condição:
		try:
			print(f'{'-' * 30}')
			número = int(input('\033[1mDigite um valor:\033[m '))

			contador += 1
			soma += número

			if contador == 1:
				maior = menor = número
			else:
				if número > maior:
					maior = número
				elif número < menor:
					menor = número

			while True:
				print(f'Você digitou o valor {número}')
				print(f'{'-' * 30}')
				continuar = input('[S] Sim [N] Não').strip().upper()
				if continuar == 'S':
					break
				elif continuar == 'N':
					condição = False
					break
				else:
					continue


		except ValueError:
			print('Este valor não e válido para essa operação.')

média = soma / contador
print(f'{'-' * 30}')
if contador == 1:
	print(f'Apenas o valor {contador} foi digitado.')
	print(f'A média é ele mesmo, além de ser o maior e o menor.')
else:
	print(f'Foram digitados {contador} valores.')
	print(f'A média entre eles é {média}')
	print(f'O maior valor digitado foi {maior}')
	print(f'O menor valor digitado foi {menor}')
print(f'{'-' * 30}')