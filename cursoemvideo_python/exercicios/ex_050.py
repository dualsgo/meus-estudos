"""Desafio 050 -  (Aula 01 a 13): Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o."""
# Extra - Os números serão dados pelo computador de forma aleatória
from random import randint
pares = []
su = 0
cont = 0
# Ler seis números
for i in range(6):
    i = randint(0,99)
# Se for par será adicionado a lista
    if i % 2 == 0:
        pares.append(i)

        cont += i # Soma os valores
        su += 1 # Soma a frequencia

# Irá somar somente os que atenderem a condição
soma = sum(pares)
print('Os números são:')
for numero in pares:
    print(numero, end=', ')
print('fim.')
print(f'A soma dos números é: {soma}.')
print(f'{su} sum e {cont} cont')