# Exercício Python #077 - Contando vogais em Tupla
# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('camisa', 'caderno', 'caderno', 'cadeira', 'lapis',
            'aprender', 'programar', 'linguagem', 'trabalhar',
            'praticar', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nAs vogais de "{palavra}" são: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')