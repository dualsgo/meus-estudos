# Exercício Python #085 - Listas com pares e ímpares
# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
for _ in range(7):
    try:
        valor = int(input('Digite um valor: '))
        lista[0 if valor % 2 == 0 else 1].append(valor)
    except ValueError:
        print('Valor inválido!')
print(lista)