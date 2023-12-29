# Exercício Python #084 - Lista composta e análise de dados - Aula 00 até 18 - Mundo 3
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_principal = []  # Inicializa a lista principal que irá conter todos os dados

pesado = 0  # Inicializa o mais pesado como zero
leve = 0  # Inicializa o mais leve como zero

while True:  # Inicializa o loop infinito
    pessoa = []  # Inicializa a lista de pessoas que será uma sub-lista dentro da principal
    pessoas_pesadas = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais pesadas
    pessoas_leves = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais leves

    nome = str(input('Nome: '))  # Recebe o nome da pessoa e armazena em uma variável
    pessoa.append(nome)  # Adiciona o valor a lista pessoa

    peso = float(input('Peso: Kg '))  # Recebe o nome da pessoa e armazena em uma variável
    pessoa.append(peso)  # Adiciona o valor a lista pessoa

    lista_principal.append(pessoa[:])  # Após cadastrar nome e peso na lista pessoa, adiciona uma cópia da lista a lista principal

    if len(lista_principal) == 1:  # Verifica se é a primeira pessoa cadastrada
        pesado = leve = peso  # Se for, o peso atribuído a ela será considerado o menor e o maior, já que é o único até o momento e servirá de comparação para os demais se houver

    else:  # Se não for a primeira pessoa, irá verificar se o peso atual é menor que o menor peso e irá atualizar caso seja verdade
        if peso < leve:
            leve = peso
        elif peso > pesado:  # Se a primeira comparação não for verdadeira, irá verificar se o peso atual é maior que o maior peso
            pesado = peso

    pessoa.clear()  # Após todas as verificações irá limpar a lista par adicionar novos dados separadamente

    continuar = str(input('Continuar? S/N')).strip().upper()  # Verificação se deseja continuar

    while continuar not in 'SN':  # Enquanto a resposta não estiver dentro dos parâmetros definidos a pergunta irá se repetir
        continuar = str(input('Continuar? S/N')).strip().upper()

    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

print(f'Foram cadastradas {len(lista_principal)} pessoas.')  # Exibe a quantidade de pessoas cadastradas

for indice, valor in enumerate(lista_principal):  # Itera sobre a lista principal para exibir cada pessoa e seu peso
    print(f'{indice + 1} - {valor[0]} pesando {valor[1]}Kg')
    if valor[1] >= pesado:  # Enquanto isso verifica se o valor do peso é maior ou igual ao valor considerado mais pesado para então adicionar o nome da pessoa em uma lista separada de pessoas mais pesadas
        pessoas_pesadas.append(valor[0])
    if valor[1] <= leve:  # O mesmo para as pessoas mais leves
        pessoas_leves.append(valor[0])
print()

print(f'O maior peso registrado foi {pesado}Kg - Peso de ', end='')
for pessoa in pessoas_pesadas:
    if len(pessoas_pesadas) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)
print()
print(f'O menor peso registrado foi {leve}Kg - Peso de ', end='')
for pessoa in pessoas_leves:
    if len(pessoas_leves) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)

