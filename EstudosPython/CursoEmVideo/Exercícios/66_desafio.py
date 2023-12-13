# Exercício Python #066 - Vários números com flag - Aula 00 até 15 - Mundo 2
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
quantidade = 0

while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        print(f'A soma entre todos os {quantidade} números digitados é {soma}.')
        break
    soma += numero
    quantidade += 1