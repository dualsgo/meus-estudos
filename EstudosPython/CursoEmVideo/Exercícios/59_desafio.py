# Exercício Python #056 - Analisador completo - Aula 00 até 13 - Mundo 2
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Tarefa 1: Inicializar os contadores e acumuladores
membros_grupo = 0  # Inicializa o contador para o número total de membros no grupo
idades_grupo = 0  # Inicializa o acumulador para somar as idades dos membros

idade_homem_mais_velho = 0  # Inicializa a variável para armazenar a idade do homem mais velho
nome_homem_mais_velho = ''  # Inicializa a variável para armazenar o nome do homem mais velho

quantidade_mulheres = 0  # Inicializa o contador para o número de mulheres com menos de 20 anos

# Tarefa 2: Ler nome, idade e sexo
masculino = 'M'  # Atribui 'M' à variável masculino para facilitar comparações
feminino = 'F'  # Atribui 'F' à variável feminino para facilitar comparações

for pessoa in range(1, 5):  # Loop para iterar sobre 4 pessoas (de 1 a 4)
    print(f'{pessoa}º Pessoa')

    # Entrada de dados do usuário
    nome = str(input('Digite o nome da pessoa: ')).strip().title()  # Solicita e formata o nome
    idade = int(input('Digite a idade da pessoa: '))  # Solicita a idade como um número inteiro
    sexo = str(input('Digite o sexo da pessoa: F/M')).strip().upper()  # Solicita e formata o sexo
    membros_grupo += 1  # Incrementa o contador de membros no grupo

    # Verifica se é a primeira pessoa do sexo masculino ou se é mais velho que o homem mais velho atual
    if pessoa == 1 and sexo == masculino:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    else:
        # Verifica se a pessoa é do sexo masculino e se a idade é maior que a do homem mais velho atual
        if sexo == masculino and idade >= idade_homem_mais_velho:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade

    # Conta mulheres com menos de 20 anos
    if sexo == feminino and idade < 20:
        quantidade_mulheres += 1

    # Acumula as idades para calcular a média posteriormente
    idades_grupo += idade

    # Exibe os dados cadastrados para cada pessoa
    print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}')
    print('Cadastro realizado com sucesso!')

# Calcula a média de idade do grupo
media_idade_grupo = idades_grupo / membros_grupo

# Exibe os resultados finais
print(f'A média de idade do grupo é {media_idade_grupo} anos.')
print(f'A homem mais velho do grupo é o {nome_homem_mais_velho} com {idade_homem_mais_velho} anos de idade.')
print(f'Entre os quatro membros do grupo, {quantidade_mulheres} são mulheres com menos de 20 anos.')

