# Exercício Python #094 - Unindo dicionários e listas - Aula 00 até 19 - Mundo 3
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
mulheres = []
idade_maior_media = []
total_idade = 0

while True:
    pessoa = dict()
    pessoa["nome"] = str(input('Nome: ')).strip().upper()
    pessoa["sexo"] = str(input('Sexo: F/M ')).strip().upper()
    while pessoa["sexo"] not in 'FM':
        pessoa["sexo"] = str(input('ERRO! Sexo deve ser F ou M ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))

    total_idade += pessoa["idade"]
    pessoas.append(pessoa)

    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

pessoas_cadastradas = len(pessoas)
media_idade = total_idade / pessoas_cadastradas
print(f'A) Foram cadastradas {pessoas_cadastradas} pessoas.')
print(f'B) A média de idade do grupo é {media_idade:.2f}')

for i, v in enumerate(pessoas):
    if v['idade'] > media_idade:
        idade_maior_media.append(v.copy())
    if v['sexo'] == 'F':
        mulheres.append(v.copy())

if len(idade_maior_media) > 0:
    print(f'{"-=" * 20}')
    print(f'{"C) ACIMA DA IDADE MÉDIA DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(idade_maior_media):
        print(f"{i+1:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")
if len(mulheres) > 0:
    print(f'{"-=" * 20}')
    print(f'{"D) MULHERES DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(mulheres, 1):
        print(f"{i:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")