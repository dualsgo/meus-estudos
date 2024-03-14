# Exercício Python #085 - Listas com pares e ímpares - Aula 00 até 18 - Mundo 3
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

from random import randint

lista_principal = []
pares = []
impares = []

for i in range(7):
    lista_principal.append(randint(0, 99))

for numero in lista_principal:
    pares.append(numero) if numero % 2 == 0 else impares.append(numero)

print(f'Todos os valores:')
for valor in lista_principal:
    print(valor, end=', ')
    if valor == lista_principal[-1]:
        print(f'{valor}.')

pares.sort()
lista_principal.append(pares[:])

impares.sort()
lista_principal.append(impares[:])

print('PARES')
for par in pares:
    print(par, end=', ')
    if par == pares[-1]:
        print(f'{par}.')

print('ÍMPARES')
for impar in impares:
    print(impar, end=', ')
    if impar == impares[-1]:
        print(f'{impar}.')