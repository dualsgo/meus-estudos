# Exercício Python #098 - Função de Contador - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def valor_válido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Valor inválido para essa operação!')


def contador(inicio, fim, passo):

        if passo == 0:
            print('Passo não pode ser zero!')
            passo += 1

        if inicio > fim:
            passo -= passo * 2

        if inicio < fim and passo > 0:
            print('CONTAGEM PROGRESSIVA!')
            for número in range(inicio, fim + 1, passo):
                print(número, end=', ')
            else:
                print('FIM!')

        elif inicio > fim and passo < 0:
            print('CONTAGEM REGRESSIVA!')
            for número in range(inicio, fim - 1, passo):
                print(número, end=', ')
            else:
                print('FIM!')

        else:
            print('Os parâmetros fornecidos não geram uma contagem válida!')


print('Contagem de 1 até 10, de 1 em 1')
sleep(1)

for i in range(11):
    sleep(.5)
    print(i, end=', ' if i < 10 else '.\n')

sleep(1)
print('Contagem de 10 até 0, de 2 em 2')

for i in range(10, -1, -2):
    sleep(.5)
    print(i, end=', ' if i > 0 else '.\n')

sleep(1)
print('Agora é sua vez! Contagem personalizada')
sleep(1)

iniciar = valor_válido('Digite o início da contagem: ')
finalizar = valor_válido('Digite o fim da contagem: ')
iterador = valor_válido('Digite o passo da contagem: ')
contador(iniciar, finalizar, iterador)