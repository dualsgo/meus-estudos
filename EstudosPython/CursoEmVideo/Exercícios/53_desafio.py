# Exercício Python #053 - Detector de Palíndromo - Aula 00 até 13
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Tarefa 1: Ler a palavra ou frase
frase = str(input('Digite a palavra ou frase: ')).strip().upper()
frase_palavras = frase.split()
frase_sem_espaco = ''.join(frase_palavras)
frase_invertida = frase_sem_espaco[::-1]
print(f'A frase {frase_sem_espaco} ao contrário é {frase_invertida}')
palindromo = frase_sem_espaco == frase_invertida
if palindromo:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')

