# Exercício Python #080 - Lista ordenada sem repetições
# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for r in range(5):
    valor = int(input('Valor: '))
    if r == 0:
        lista.append(valor)
        print('Primeiro valor adicionado!')
    else:
        if valor > lista[-1]:
            lista.append(valor)
            print(f'Valor adicionado no fim da lista.')
        elif valor < lista[0]:
            lista.insert(0, valor)
            print('Valor adicionado no início da lista.')
        else:
            for i in range(len(lista) - 1):
                if lista[i] < valor <= lista[i + 1]:
                    lista.insert(i + 1, valor)
                    print(f'Valor adicionado na posição {i+1}')
                    break

print(lista)