# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


def valores(n, s, i):
    while True:
        name = input(n).strip().title()
        sex = input(s).upper()
        while 'M' != sex != 'F':
            print(f'Opção inválida. Digite novamente...')
            sex = input('Digite o sexo: M ou F ').upper()
        while True:
            try:
                age = int(input(i))
                break
            except ValueError:
                print('Valor inválido!')
        return name, sex, age


média_idade = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_menos_vinte = 0

for pessoa in range(1, 5):
    print(f'{"-" * 20}')
    print(f'{f"{pessoa}ª pessoa:":^20}')
    print(f'{"-"*20}')

    nome, sexo, idade = valores('Digite o nome: ', 'Digite o sexo: M ou F ', 'Digite a idade: ')

    média_idade += idade

    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1


print(f'A média de idade do grupo é {média_idade / 4} anos')

print(f'O homem mais velho se chama {nome_homem_velho} e tem {idade_homem_velho} anos' if nome_homem_velho else 'Não há homens no grupo')

print(f'Há {mulheres_menos_vinte}' if mulheres_menos_vinte else 'Não há', f'{'mulher' if mulheres_menos_vinte == 1 else 'mulheres'} com menos de 20 anos no grupo')