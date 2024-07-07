# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

while True:
    try:
        número = float(input('Digite um valor: '))
        parte_inteira = número // 1
        parte_decimal = número % 1
        convertido = str(número)
        tamanho = len(convertido)
        tamanho_decimal = len(convertido[convertido.index('.'):])
        print(f'{"Número:":<10}\033[1;33m{número:>{tamanho}}\033[m\n'
              f'{"Inteiro:":<10}\033[1;31m{parte_inteira:<{tamanho}.1g}\033[m\n'
              f'{"Decimal:":<10}\033[1;32m{parte_decimal:>{tamanho}.{tamanho_decimal}g}\033[m')
        break

    except ValueError:
        print('Valor inválido!')