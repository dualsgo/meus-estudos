# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

from emoji import emojize

def obtem_valore(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(emojize('Valor inválido! Tente novamente. :xis:', language='pt'))


primeiro_termo = obtem_valore(emojize(':ábaco: Digite o primeiro termo: ', language='pt'))

segundo_termo = obtem_valore(emojize(':ábaco: Digite o segundo termo: ', language='pt'))

soma = primeiro_termo + segundo_termo

print(emojize(':ábaco: Calculando... ', language='pt'))

print(emojize(f'{primeiro_termo:>10}\n{'+':<1}{segundo_termo:>9}\n{soma:>10}', language='pt'))