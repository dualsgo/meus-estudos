# Exercício Python #077 - Contando vogais em Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Tupla de palavras
palavras = ("abacaxi", "banana", "carro", "dente", "elefante", "futebol", "gato", "hotel", "igreja", "janela", "ketchup", "limonada", "macaco", "navio", "olho", "pizza", "quarto", "roda", "sapato", "tigre")

for palavra in palavras:
	print(f'\nPalavra: {palavra}', end=' - ')
	for vogal in palavra:
		print(vogal if vogal in 'aeiou' else ' ', end='')