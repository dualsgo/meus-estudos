# Exercício Python #098 - Função de Contador - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        print('PASSO ZERO INVÁLIDO! SERÁ CONVERTIDO PARA 1')
        passo = 1

    print(f'Contagem de {inicio} até {fim} a cada {passo}')
    if inicio > fim:
        for i in range(inicio, fim-1, -passo):
            sleep(.5)
            print(f'{i}.' if i - fim < passo else f'{i}, ', end='')

    else:
        for i in range(inicio, fim+1, passo):
            sleep(.5)
            print(f'{i}.' if fim - i <= passo else f'{i}, ', end='')



print('Contagem de 1 até 10, de 1 em 1')
for i in range(11):
    sleep(.5)
    if i == 10:
        print(f'{i}.')
    else:
        print(i, end=', ')

sleep(1)
print('Contagem de 10 até 0, de 2 em 2')
for i in range(10, -1, -2):
    sleep(.5)
    if i == 0:
        print(f'{i}.')
    else:
        print(i, end=', ')
    sleep(.5)

print('Agora é sua vez! Contagem personalizada')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))