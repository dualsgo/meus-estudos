# Exercício Python #069 - Análise de dados do grupo - Aula 00 até 15 - Mundo 2
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoa_mais_18 = 0  # Contador para pessoas com mais de 18 anos
homens = 0         # Contador para homens
mulheres_menos_20 = 0  # Contador para mulheres com menos de 20 anos

contador = 0  # Contador total de pessoas

while True:
    # Conta a quantidade de pessoas
    contador += 1
    print(f'{contador}º pessoa')

    # Solicita a idade e o sexo da pessoa
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (F/M): ').strip().upper()

    # Garante que o sexo seja F ou M
    while sexo not in 'FfMm':
        sexo = input('Digite o sexo da pessoa (F/M): ').strip().upper()

# Verifica as condições e atualiza os contadores

    # Se for maior de 18 anos
    if idade >= 18:
        pessoa_mais_18 += 1

    # Se for um homem
    if sexo == 'M':
        homens += 1

    # Se for uma mulher com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    # Verifica se quer continuar
    continuar = input('Deseja continuar? (S/N): ').strip().upper()

    # Garante que a resposta seja S ou N
    while continuar not in 'SsNn':
        print('Comando inválido!')
        continuar = input('Somente S ou N. Deseja continuar? (S/N): ').strip().upper()

    # Se for não, encerra. Caso contrário, reinicia o loop
    if continuar == 'N':
        print('Encerrando...')
        break
    else:
        print('Continuando...')

# Exibe as estatísticas finais
print(f'{"Apenas uma pessoa foi cadastrada!" if contador == 1 else f'Foram cadastradas {contador} pessoas.'}')
print(f'Entre elas, {pessoa_mais_18} {"pessoa tem mais de 18 anos." if pessoa_mais_18 == 1 else "pessoas têm mais de 18 anos."}')
print(f'Ao todo, {homens} {"homem foi cadastrado." if homens == 1 else "homens foram cadastrados."}')
print(f'Temos {mulheres_menos_20} {"mulher com menos de 20 anos." if mulheres_menos_20 == 1 else "mulheres com menos de 20 anos."}')


