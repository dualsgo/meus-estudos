"""Desafio 56 - Analisador completo (Aula 01 a 13): Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""

# Primeiro coletar os dados - Defini as variáveis de controle para somar depois usá-las dentro do loop
soma_idades = 0
nome_mais_velho = ''
mais_velho = 0
mulheres_menos_20 = 0
# Fazendo a iteração
for i in range(1, 5):
    # print() para apoiar visualmente qual iteração estamos
    print(f'Pessoa {i}')
    # Coletar o nome, idade e sexo
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = int(input('1 - Masculino\n2- Feminino\n'))
    # A cada iteração somar o valor da idade a variável acumuladora
    soma_idades += idade
    # Controle para identificar o mais velho verificando se é homem e se a idade atual é maior que a anterior
    if sexo == 1 and idade > mais_velho:
        # Se a idade for maior que a anterior irá substituir o valor
        mais_velho = idade
        # E atribuir o valor do nome a variável
        nome_mais_velho = nome
    # Verifica se é mulher
    if sexo == 2 and idade < 20:
        # Se for acumula a ocorrência
        mulheres_menos_20 += 1
# Exibir a média de idade do grupo - Somar todas as idades e dividir pelo número de pessoas
print(f'A média de idade do grupo é \033[31m{soma_idades/4}\033[m')
# Exibir o nome a pessoa mais velha
print(f'O nome da pessoa mais velha é: \033[31m{nome_mais_velho}\033[m')
# Exibir a quantidade de mulheres com menos de 20 anos
if mulheres_menos_20 > 1:
    print(f'Ao todo temos \033[31m{mulheres_menos_20}\033[m mulheres com menos de 20 anos de idade!')
else:
    print(f'Ao todo temos apenas \033[31m{mulheres_menos_20}\033[m mulher com menos de 20 anos de idade!')

