# Exercício Python #100 - Funções para sortear e somar - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from random import randint
from time import sleep
numeros = []


def sorteia(quantidade):
    for v in range(quantidade):
        numeros.append(randint(0, 9))
    print(f'A lista final é a seguinte: {numeros}')


def somar_pares():
    soma_pares = 0
    for v in numeros:
        if v % 2 == 0:
            soma_pares += v
    print(f'A soma entre todos os valores pares presentes na lista é {soma_pares}')


sorteia(int(input('Digite a quantidade de números que deseja sortear: ')))

somar_pares()