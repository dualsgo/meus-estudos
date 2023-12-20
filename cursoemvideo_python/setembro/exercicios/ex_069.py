"""Desafio 069 - Análise de dados do grupo (Aula 01 a 15): Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada , o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.
"""

# Inicializa contadores
maior_18_anos = 0  # Contador de pessoas com mais de 18 anos
cadastros = 0  # Contador de total de cadastros
mulheres_menos_20 = 0  # Contador de mulheres com menos de 20 anos
homens = 0  # Contador de homens

# Inicia o loop principal
while True:
    print('CADASTRAR UMA PESSOA?')
    resposta = str(input('S/N')).upper().strip()

    # Verifica se a resposta é 'N', encerrando o programa se for verdadeira
    if resposta == 'N':
        print('Programa encerrado!')
        break

    # Se a resposta é 'S', realiza o cadastro
    elif resposta == 'S':
        # Recebe informações sobre a pessoa
        idade = int(input('Digite a idade: '))

        # Verifica e valida a entrada do sexo
        while True:
            sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
            if sexo in ['M', 'F']:
                break
            else:
                print('Opção inválida. Digite M para masculino ou F para feminino.')

        # Exibe mensagem de cadastro
        print(f'Você cadastrou uma pessoa de {idade} do sexo {sexo}')
        cadastros += 1  # Incrementa o contador de cadastros

        # Verifica e atualiza contadores
        if idade >= 18:
            maior_18_anos += 1  # Incrementa o contador de pessoas com mais de 18 anos

        if idade < 20 and sexo == 'F':
            mulheres_menos_20 += 1  # Incrementa o contador de mulheres com menos de 20 anos

        if sexo == 'M':
            homens += 1  # Incrementa o contador de homens

# Exibe resumo final apenas se condições são atendidas
if cadastros > 0:
    print(f'Foram cadastradas {cadastros} pessoas.')

if maior_18_anos > 0:
    print(f'{maior_18_anos} pessoas têm mais de 18 anos.')

if homens > 0:
    print(f'Foram cadastrados {homens} homens.')

if mulheres_menos_20 > 0:
    print(f'{mulheres_menos_20} mulheres têm menos de 20 anos.')


