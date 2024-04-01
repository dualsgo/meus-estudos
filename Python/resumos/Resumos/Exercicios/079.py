# Exercício Python #079 - Valores únicos em uma Lista
# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()

while True:
    try:
        valor = int(input('Digite um valor: '))
        if valor not in valores:
            print('Valor adicionado')
            valores.append(valor)
        else:
            print('Valor repetido. Não será considerado.')
        continuar = ''
        while continuar not in ('S', 'N'):
            continuar = input('Continuar? S/N').strip().upper()

        if continuar == 'S':
            continue
        if continuar == 'N':
            break

    except ValueError:
        print(f'Inválido!')
        continue

print(f'Os valores digitados foram: ', end='')
for a, i in enumerate(sorted(valores), 1):
    print(i, end=', ' if a != len(valores) else '.')