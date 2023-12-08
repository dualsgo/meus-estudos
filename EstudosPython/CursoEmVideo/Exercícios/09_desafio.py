# Exercício Python #004 - Dissecando uma Variável - Aula 00 até 07 - Mundo 1
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
from emoji import emojize
from time import sleep

# Tarefa 1: Ler um número.
numero = int(input(emojize(':teclado: Digite o valor: ', language='pt')))

# Tarefa 2: Criar a tabuada.
print(emojize(f'Tabuada de :sinal_de_multiplicação: {numero}', language='pt'))
sleep(1)
print(emojize(f'{numero} :sinal_de_multiplicação: {1:2} = {numero * 1:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {2:2} = {numero * 2:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {3:2} = {numero * 3:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {4:2} = {numero * 4:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {5:2} = {numero * 5:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {6:2} = {numero * 6:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {7:2} = {numero * 7:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {8:2} = {numero * 8:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {9:2} = {numero * 9:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {10:2} = {numero * 10:2}', language='pt'))

