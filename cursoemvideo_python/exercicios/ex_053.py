"""Desafio 053 -  (Aula 01 a 13):
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

# Ler uma frase
reverso = ''  # Variável para armazenar a versão invertida da frase
compara = ''  # Variável para armazenar a versão original da frase
frase = str(input('Digite a frase: ')).strip().upper()  # Lê a frase, remove espaços em branco e converte para letras maiúsculas
print(frase)  # Imprime a frase original

# Loop para inverter a frase
for letra in frase:
    reverso = letra + reverso
    compara = compara + letra

# Verifica se a versão invertida é igual à versão original
if reverso == compara:
    print(f'{frase} ao contrário é {reverso}:\nÉ UM PALÍNDROMO!')
else:
    print(f'{frase} ao contrário é {reverso}:\nNÃO É UM PALÍNDROMO!')

# USANDO FATIAMENTO SEM FOR frase[::-1]