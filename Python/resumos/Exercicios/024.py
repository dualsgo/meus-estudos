# Exercício Python #024 - Verificando as primeiras letras de um texto
# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = input('Digite o nome da cidade: ').strip().title().split()[0]
print('Começa com Santo."' if nome == 'Santo' else 'Não começa com "Santo".')