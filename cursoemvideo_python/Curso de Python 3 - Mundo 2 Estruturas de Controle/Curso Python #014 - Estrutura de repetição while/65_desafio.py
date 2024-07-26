# Exercício Python #065 - Maior e Menor valores - Aula 00 até 14 - Mundo 2
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

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


# Usando lista
valores = []
while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')

    while True:
        continuar = input('Deseja continuar? (S/N): ').strip().upper()
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Por favor, digite S ou N.')
        else:
            break

    if continuar == 'N':
        break

if valores:
    print(f'A média entre todos os {len(valores)} valores digitados é {sum(valores) / len(valores)}')
    print(f'O maior valor digitado foi {max(valores)}, enquanto o menor foi {min(valores)}.')
else:
    print('Nenhum valor foi digitado.')