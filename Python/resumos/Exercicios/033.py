# Exercício Python #033 - Maior e menor valores
# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

maior = float('-inf')
menor = float('inf')

for _ in range(3):
	numero = int(input(f'Digite o {_+1}º valor: '))
	if numero > maior:
		maior = numero
	if numero < menor:
		menor = numero

print(f'Maior: {maior}')
print(f'Menor: {menor}')