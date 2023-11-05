"""Desafio 051 -  (Aula 01 a 13): Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética e no final mostre os 10 primeiros termos dessa progressão."""


"""
Uma PA, ou Progressão Aritmética, é uma sequência numérica em que a diferença entre cada par de termos consecutivos é constante. Essa diferença constante é chamada de "razão" da PA e é representada pela letra "r". A fórmula geral para uma PA é:

a_n = a_1 + (n - 1) * r

- a_n é o n-ésimo termo da PA.
- a_1 é o primeiro termo da PA.
- n é a posição do termo desejado na sequência.
- r é a razão da PA.

Por exemplo, considere a seguinte PA: 2, 4, 6, 8, 10. Neste caso:
- a_1 é 2 (o primeiro termo).
- r é 2 (a diferença constante entre os termos).
- Se quisermos encontrar o 4º termo (n = 4), podemos usar a fórmula:
a_4 = 2 + (4 - 1) * 2
2 + 3 * 2
2 + 6 = 8.
Assim, o 4º termo da PA é 8.

"""
termos = []  # Inicializa uma lista vazia chamada 'termos' para armazenar os termos da PA.

# Solicita ao usuário que insira o primeiro termo da PA e a razão.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

# Calcula o décimo termo da PA usando a fórmula geral (a_10 = a_1 + (10 - 1) * r).
decimo = primeiro + 10 * razao

# Usa um loop 'for' para gerar os 10 primeiros termos da PA e armazená-los na lista 'termos'.
for i in range(primeiro, decimo, razao):
    if i % 2 == 0:
        termos.append(f'\033[32m{i}\033[m')
    else:
        termos.append(f'\033[31m{i}\033[m')

# Imprime os termos da PA.
print(f'\033[1;31mOs termos são:\033[m')
for termo in termos:
    print(termo, end=', ')

# Imprime 'fim.' para indicar o final da lista de termos.
print('fim.')

