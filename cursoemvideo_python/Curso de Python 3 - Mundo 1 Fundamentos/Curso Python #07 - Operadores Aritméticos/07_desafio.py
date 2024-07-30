# Exercício Python #007 - Média Aritmética - Aula 00 até 07 - Mundo 1
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

from emoji import emojize


def obtem_nota(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print(emojize(f':xis: Valores inválidos! :xis:', language='pt'))


primeira_nota = obtem_nota(emojize(':memorando: Digite a primeira nota: ', language='pt'))
segunda_nota = obtem_nota(emojize(':memorando: Digite a segunda nota: ', language='pt'))
média = (primeira_nota + segunda_nota) / 2


print(f'{'Primeira nota:':<15}{primeira_nota:>5}\n{'Segunda nota:':<15}{segunda_nota:>5}\n{'Média:':<15}{média:>5}')

print(f'{'\033[1;31mREPROVADO\033[m'}' if média < 5 else f'{'\033[1;33mEM RECUPERAÇÃO\033[m'}' if média < 7 else f'{'\033[1;32mAPROVADO\033[m'}')

