# Exercício Python #080 - Lista ordenada sem repetições - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
maior = menor = 0

for indice in range(5):
    valor = int(input(f'Digite o valor do índice {indice}: '))

    if indice == 0:
        maior = menor = valor
        lista.append(valor)

    elif valor > maior:
        maior = valor
        lista.append(valor)

    elif valor < maior:
        if valor < menor:
            lista.insert(0, valor)
            menor = valor

        elif valor > menor:
            lista.insert(1, valor)

    print(maior)
    print(menor)

print(lista)