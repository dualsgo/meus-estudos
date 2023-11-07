"""Desafio 061 - Progressão aritimética V.2.0 (Aula 01 a 14): Refaça o desafio 051, lendo o primeiro termo e a razõa de uma PA mostrando os 10 primeiros termos da prograssão usando while.
"""

# Ler o primeiro termo da PA e a razão
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
decimo = 1

# Mostrar os 10 primeiros termos
while decimo <= 10:
    print(termo, end=', ')
    termo += razao
    decimo += 1
print('FIM')
