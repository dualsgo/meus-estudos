"""Desafio 079 - Valores únicos em uma lista (Aula 01 a 17): Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
"""
# Inicializar a lista
lista = []

# Usuário digitar vários números
while True:
    elemento = int(input('Digite um valor: '))

    # Verificar se o número já está na lista
    if elemento not in lista:
        print('\033[1;32mNovo elemento adicionado!\033[m')
        lista.append(elemento)
    else:
        print('\033[1;31mElemento repetido!\033[m')

    # Perguntar se o usuário deseja adicionar mais elementos
    pergunta = input('Deseja adicionar mais elementos? (\033[1;32mS\033[m/\033[1;31mN\033[m)').strip().upper()

    # Encerrar o programa se a resposta for 'N'
    if pergunta == 'N':
        print('\033[1;31;40mPrograma encerrado!\033[m')
        break

# Exibir os valores em ordem crescente
print(f'Lista em ordem crescente: {sorted(lista)}')
