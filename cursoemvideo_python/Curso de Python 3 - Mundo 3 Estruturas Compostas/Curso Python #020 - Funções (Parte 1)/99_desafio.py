# Exercício Python #099 - Função que descobre o maior - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep
lista_parametros = []


def cria_lista(quantidade, inicio, fim):
    if quantidade == 0:
        print(f'Nenhum valor informado!')
    elif quantidade == 1:
        print(f'Apenas um valor informado.')
    else:
        print(f'Sorteando {quantidade} números entre {inicio} e {fim}')
        for i in range(quantidade):
            lista_parametros.append(randint(inicio, fim))


cria_lista(randint(0, 10), randint(0, 99), randint(100, 999))


def maior(*varios_parametros):
    if len(lista_parametros) == 0:
        print()
    elif len(lista_parametros) == 1:
        print(f'{lista_parametros} é o único número informado.')
    else:
        print(f'Os {len(lista_parametros)} valores adicionados foram: ')
        for v in varios_parametros:
            sleep(.5)
            if v == varios_parametros[-1]:
                print(f'{v}.')
            else:
                print(v, end=', ')
        sleep(1)
        print(f'O menor valor da lista é o {min(varios_parametros)}')
        sleep(1)
        print(f'O maior valor da lista é o {max(varios_parametros)}')


# Usando * para desempacotar a lista ao passá-la como argumento
maior(*lista_parametros)