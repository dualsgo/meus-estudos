"""Desafio 008 - Conversor de medidas (Aula 01 a 07): Escreva um programa que leia um valor em metros e o exiba convertido em centimetros."""

# Passo 1: Ler o valor em metros - Armazenamos o valor convertido para float em uma variável
print('\033[7mCONVERSOR DE MEDIDAS\033[m')
print('Digite um valor em metros para convertê-lo:')
metros = float(input(''))
# Passo 2: Converter o valor para centimetros e exibi-lo - Utilizamos uma variável para realizar a conversão e armazenar o valor. Para isso multiplicamos o calor digitado por 100.
centimetros = int(metros * 100)
print(f"""
Você digitou {metros}m.
Este valor equivale a {centimetros}cm""")
