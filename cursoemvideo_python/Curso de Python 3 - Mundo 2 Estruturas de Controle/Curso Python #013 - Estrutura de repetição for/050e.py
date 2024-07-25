# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

acumulador = contador = 0
for número in range(1, 7):
	while True:
		try:
			valor = int(input(f'Digite o {número}º valor: '))
			if valor % 2:
				print('\033[1;31mValor ímpar desconsiderado\033[m')
			else:
				print('\033[1;32mValor par considerado\033[m')
				acumulador += valor
				contador += 1
			break
		except ValueError:
			print('Você digitou um valor de tipo inválido!')
print(f'Entre os 6 números, consideramos {contador} e a soma entre eles é igual a {acumulador}.')

# Com lista
nmbrs = [int(input('Digite um número: ')) for i in range(6)]
soma = [i for i in nmbrs if i % 2 == 0]
print(f'A soma entre os {len(soma)} números pares digitados é {sum(soma)}')