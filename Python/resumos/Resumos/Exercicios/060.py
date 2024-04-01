# Exercício Python #060 - Cálculo do Fatorial
# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

while True:
    try:
        número = int(input('Digite um valor: '))
    except ValueError:
        print(f'Tipo de dado inválido!')

    else:
        print(f'{número}! = ', end='')
        produto = 1
        for _ in range(número, 0, -1):
            print(f'{_}', end=' x ' if _ > 1 else ' = ')
            produto *= _
        print(produto)
        break