# Exercício Python #069 - Análise de dados do grupo - Aula 00 até 15 - Mundo 2
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoa_mais_18 = 0
homens = 0
mulheres_menos_20 = 0

contador = 0

while True:
    contador += 1
    print(f'{contador}º pessoa')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: F/M')).strip().upper()
    while sexo not in 'FfMm':
        sexo = str(input('Digite o sexo da pessoa: F/M')).strip().upper()

    if idade > 18:
        pessoa_mais_18 += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20 += 1

    continuar = str(input('Deseja continuar? S/N')).strip().upper()

    if continuar not in 'SsNn':
        print('Comando inválido!')
        continuar = str(input('Somente S ou N')).strip().upper()

    if continuar in 'Ss':
        print('Continuando...')

    if continuar in 'Nn':
        print('Encerrando...')
        break

print(f'Foram cadastradas {contador} pessoas.')
print(f'Entre elas, {pessoa_mais_18} pessoas tem mais de 18 anos.')
print(f'Ao todo {homens} pessoas são homens.')
print(f'Temos {mulheres_menos_20} mulheres com menos de 20 anos.')
