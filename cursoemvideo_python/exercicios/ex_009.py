"""Desafio 009 - Tabuada (Aula 01 a 07): Faça um programa que leia um número inteiro qualquer e mostre a sua dabuada."""

# Passo 1: Ler o número - Para isso armazenamos o valor recebido utilizando uma função input em uma variavel
print("""
=======================
=    T A B U A D A    =
=======================
""")
print('Digite um número:')
numero = int(input(''))
# Passo 2: Mostrar a tabuada desse número até 10 - Nesse exercicio exibiremos todos os resultados na mesma string formatada.
print(f"""
\033[7mA tabuada de {numero} até 10 é:\033[m

\033[1;31m{numero} X  0 = {numero * 0}\033[m
\033[1;32m{numero} X  1 = {numero * 1}\033[m
\033[1;33m{numero} X  2 = {numero * 2}\033[m
\033[1;34m{numero} X  3 = {numero * 3}\033[m
\033[1;35m{numero} X  4 = {numero * 4}\033[m
\033[1;36m{numero} X  5 = {numero * 5}\033[m
\033[1;37m{numero} X  6 = {numero * 6}\033[m
\033[1;31m{numero} X  7 = {numero * 7}\033[m
\033[1;32m{numero} X  8 = {numero * 8}\033[m
\033[1;33m{numero} X  9 = {numero * 9}\033[m
\033[1;34m{numero} X 10 = {numero * 10}\033[m""")
