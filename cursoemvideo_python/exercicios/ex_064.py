"""Desafio 064 -  Tratando vários valores v.1.0 (Aula 01 a 14): Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar 999 que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag
"""
# Ler o primeiro numero
acumulador = 0
contador = 0
numero = int(input('Digite um número: 999 finaliza '))
while numero != 999:
    acumulador += numero
    contador += 1
    numero = int(input('Digite um número: 999 finaliza '))
print(f'Foram digitados {contador} números.')
print(f'A soma entre eles é {acumulador}')