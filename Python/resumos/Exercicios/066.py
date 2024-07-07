# Exercício Python #066 - Vários números com flag
# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

valores = []
while True:
    try:
        valor = int(input('Digite um valor: 999 Encerra'))
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')
        continue
    if valor == 999:
        break
    valores.append(valor)

if not valores:
    print('Nenhum valor foi digitado.')
else:
    print(f'A soma entre todos os {len(valores)} valores é {sum(valores)}')