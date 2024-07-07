# Exercício Python #064 - Tratando vários valores v1.0
# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

valores = list()
while True:
	valor = int(input('Digite um valor: 999 Encerra '))
	if valor != 999:
		valores.append(valor)
	else:
		break

print(f'A soma entre todos os {len(valores)} valores é {sum(valores)}')