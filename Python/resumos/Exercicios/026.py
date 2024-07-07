# Exercício Python #026 - Primeira e última ocorrência de uma string
# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from unidecode import unidecode

frase = unidecode(input('Digite uma frase para analisarmos: ').strip().title())

for letra in frase:
    print(f'\033[31m{letra}\033[m' if letra in 'aA' else letra, end='')

print(f'\n{'Quantidade de "a":':<30}{frase.lower().count("a"):>2}')
print(f'{'A primeira posição de "a":':<30}{frase.lower().find("a")+1:>2}')
print(f'{'A última posição de "a":':<30}{frase.lower().rfind("a")+1:>2}')