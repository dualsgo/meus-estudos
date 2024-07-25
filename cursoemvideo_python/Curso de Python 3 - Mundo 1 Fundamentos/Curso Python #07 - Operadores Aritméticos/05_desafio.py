# Exercício Python #005 - Antecessor e Sucessor - Aula 00 até 07 - Mundo 1
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

from emoji import emojize

while True:
	try:
		número = int(input(emojize(':memorando: Digite um valor: ', language='pt')))
		sucessor = número + 1
		antecessor = número - 1
		print(emojize(f':seta_para_a_esquerda:\033[1;31m{antecessor:^5}\033[m:seta_para_a_esquerda:\033[1;33m{número:^5}\033[m:seta_para_a_direita:\033[1;32m{sucessor:^5}\033[m:seta_para_a_direita:', language='pt'))
		break
	except ValueError:
		print(emojize(':xis: Apenas números inteiros! :xis:', language='pt'))
