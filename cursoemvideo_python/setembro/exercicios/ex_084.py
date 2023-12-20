"""Desafio 084 -  (Aula 01 a 18): Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves
"""
# Inicializa a lista principal
lista = []
# Inicializa as listas para armazenar as pessoas mais pesadas e mais leves
mais_pesados = []
mais_leves = []
# Loop para ler o nome e peso de várias pessoas. Será finalizado quando o usuário decidir não adicionar mais pessoas à lista.
while True:
    # Inicializa a lista para armazenar nome e peso da pessoa atual. Cada informação já será alocada em seu índice
    pessoa = [str(input('Digite o nome da pessoa: ')), float(input('Digite o peso dessa pessoa: '))]
    if len(lista) == 0:
        mais_leves = mais_pesados = pessoa[1]
    else:
        if pessoa[1] >= mais_pesados:
            mais_pesados.append(pessoa[1])
        if pessoa[1] <= mais_leves:
            mais_leves.append(pessoa[1])

    # Adiciona uma cópia da lista pessoa atual à lista principal
    lista.append(pessoa[:])

    # Pergunta se deseja continuar até obter uma resposta válida
    while True:
        pergunta = input('Deseja continuar? (S/N)').strip().upper()

        # Verifica a resposta para decidir se continua, encerra o programa ou mostra uma mensagem de comando inválido
        if pergunta == 'N':
            print('Finalizando o programa!')
            break  # Essa primeira instrução sai do loop de verificação
        elif pergunta == 'S':
            print('Continuando...')
            break
        else:
            print('Comando inválido! Digite S ou N.')

    # Encerra o loop principal se o usuário decidir não adicionar mais pessoas à lista
    if pergunta == 'N':
        break
print(lista)
# Quantas pessoas foram cadastradas. Essa informação é facilmente acessada exibindo o comprimento da lista principal
print(f'Foram cadastradas {len(lista)} pessoas!')

# Exibe as listas de pessoas mais pesadas e mais leves
print(f'As pessoas mais pesadas pesam {mais_pesados}Kg e são:')
if pessoa in mais_pesados:
    print(pessoa[0])
print(f'As pessoas mais leves pesam {mais_leves}Kg e são:')
if pessoa in mais_leves:
    print(pessoa[0])
