# Exercício Python #066 - Vários números com flag - Aula 00 até 15 - Mundo 2
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando a flag).


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


# Com lista

valores = []
while True:
    try:
        valor = int(input('Digite um valor: 999 Encerra'))
        if valor == 999:
            break
        valores.append(valor)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')

if not valores:
    print('Nenhum valor foi digitado.')
else:
    print(f'A soma entre todos os {len(valores)} valores é {sum(valores)}')