# Exercício Python #053 - Detector de Palíndromo
# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
print('Palíndromo' if frase == frase[::-1] else 'Não é palíndromo')