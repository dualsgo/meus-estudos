"""Desafio 008 - Conversor de medidas (Aula 01 a 07): Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milímetros."""

# Passo 1: Ler o valor em metros - Armazenamos o valor convertido para float em uma variável
print('\033[7mCONVERSOR DE MEDIDAS\033[m')
print('Digite um valor em metros para convertê-lo:')
metros = float(input(''))
# Passo 2: Converter o valor para centimetros e exibi-lo - Utilizamos uma variável para realizar a conversão e armazenar o valor. Para isso multiplicamos o calor digitado por 100.
km = metros / 1000
hm = metros / 100
dam = metros / 10
m = metros
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f"""
Você digitou {metros}m.
Este valor equivale a:
\033[1;32m{km}km (Quilômetro)
{hm}hm (Hectômetro)
{dam}dam (Decâmetro)\033[m
{metros}m (Metros)
\033[1;31m{dm}dm (Decímetro)
{cm}cm (Centrímetro)
{mm}mm (Milímetro)\033[m
""")
