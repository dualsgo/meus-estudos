# Curso Python Aula 10 - Condições

"""RESUMO"""
# Introdução ao conceito de estruturas condicionais na programação em Python.

# Uso de uma analogia de um carro na estrada para explicar como comandos controlam o movimento do computador.

# Enfatização da importância da ordem sequencial dos comandos e do perigo de pular comandos.

# Explicação de como o programa segue uma sequência de cima para baixo, lendo na mesma direção da tela.

# Discussão sobre a criação de algoritmos como um tipo de estrutura condicional.

# Introdução à ideia de condicionais em que diferentes caminhos podem ser seguidos com base em decisões.

# Utilização de uma analogia de um carro fazendo uma escolha para ilustrar como a execução de código pode ser direcionada.

# Explicação de como condicionais permitem que um programa execute diferentes blocos de código com base em decisões.

# Introdução ao uso de cores para representar diferentes resultados em condicionais.

# Discussão sobre a sintaxe de condicionais em Python, com parênteses e dois pontos para indicar condição e ação.

# Ênfase na importância de compreender as condicionais e sua relevância na programação.

# Apresentação de exemplos de condicionais com diferentes cenários e explicações.

# Demonstração de condicionais mais complexas e sua aplicação em problemas de programação.

# Introdução a condicionais em uma única linha para simplificar a sintaxe.

# Encorajamento para os espectadores a praticarem condicionais como parte do aprendizado em programação.

"""CONTEÚDO"""

# Estruturas condicionais oferecem alternativas para os programas quando o fluxo não é linear

# Sintaxe:
# Nesse exemplo como atribuímos a variável o valor True, o primeiro bloco será executado.
algo = True

# A estrutura usa identação para identificar as instruções dentro das estruturas conducionais
if algo:  # if sempre é executado se a condição for verdadeira - podemos usar uma comparação
    print('\033[32mExecuta essa instrução caso a condição seja atendida\033[m')
else:  # else não precisa de condição pois será executado sempre que a condição não for atendida
    print('\033[31mExecuta essa instrução caso a condição não seja atendida\033[m')
# As instruções fora da identação são sempre executadas
print('Essa instrução não faz parte da estrutura condicional')

# Exemplo de programa:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')

# Condição simplificada - sintaxe:
print('CARRO NOVO'if tempo <= 3 else 'CARRO VELHO')

# Pratica
# Estrutura condicional simples possui apenas um bloco if, a estrutura condicional composta possui um ou mais blocos if. O bloco else é opicional, mas deve vir sempre no final, após os bloco if
nome = str(input('Qual é o seu nome? '))

# CONDIÇÃO - Consiste em uma comparação entre o valor digitado e o valor pré definido.
if nome == 'Gustavo':
    # BLOCO VERDADEIRO - Será executado somente se a CONDIÇÃO for atendida.
    print('Que nome lindo você tem!')
# Essa instrução será executada independete da condição pois a indentação indica que não faz parte do bloco condicional if
print(f'Bom dia, {nome}.')

# Exemplo 2
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'A sua média foi: {media}')
# A estrutura avalia se a média é boa ou ruim
if media >= 6:
    print('SUA MÉDIA FOI BOA.')
else:
    print('SUA MÉDIA FOI RUIM.')
# Estrutura simplificada
print('PARABÉNS' if media >= 6 else 'ESTUDE MAIS')
