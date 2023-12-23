# Exercício Python #004 - Dissecando uma Variável - Aula 00 até 06 - Mundo 1
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

'''# Tarefa 1: Ler algo pelo teclado.
algo = input('Digite algo: ')  # Nesse exercício nos limitamos a strings, pois é o valor padrão retornado pelo input()

# Tarefa 2: Mostrar na tela o seu tipo primitivo e outras informações.
print(f'O tipo primitivo desse valor é {type(algo)}.')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um numérico (contém somente números)? {algo.isnumeric()}')
print(f'É alfabético (contém somente letras)? {algo.isalpha()}')
print(f'É alfanumérico (contém letras ou números)? {algo.isalnum()}')
print(f'Está todo em MAIÚSCULAS? {algo.isupper()}')
print(f'Está todo em minúsculas? {algo.islower()}')
print(f'Está capitalizado (somente a primeira letra maiúscula)? {algo.istitle()}')

Todo objeto tem características e e realiza funcionalidades (atributos e métodos). Todos os métodos terminam com parênteses.'''

# Passo 1: Ler algo pelo teclado. Para isso utilizamos uma variável para armazenar os dados que serão inseridos através de uma função input()
def sim_ou_nao(condicao):
    return 'Sim' if condicao else 'Não'

algo = input('Digite algo: ')
# Passo 2: Exibir as informações. Para isso iremos criar um print() com uma string formatada e usaremos os métodos aplicáveis.
# Observação: Iniciar a impressão de uma string formatada com três aspas triplas permite que a string abranja várias linhas e contenha substituições de variáveis.

# Verifica se a string inserida é numérica.
if algo.isnumeric():
    # Se for numérica, converte para um número inteiro.
    valor_inteiro = int(algo)
    print(f'O valor digitado é do tipo int: {valor_inteiro}')
    if valor_inteiro > 0:
        print(f'É um número inteiro positivo.')
    elif valor_inteiro < 0:
        print(f'É um número inteiro negativo.')
    else:
        print('É um número inteiro igual a zero.')
elif algo.replace('.', '', 1).isdigit():
    # Se for numérica com um único ponto decimal, converte para float.
    valor_float = float(algo)
    print(f'O valor digitado é do tipo float: {valor_float}')
    if valor_float > 0:
        print(f'É um número de ponto flutuante positivo.')
    elif valor_float < 0:
        print(f'É um número de ponto flutuante negativo.')
    else:
        print('É um número de ponto flutuante igual a zero.')
else:
    # Se não for numérica, exibe como uma string.
    print(f'O valor digitado é do tipo {type(algo).__name__} e contém a seguinte informação: {algo}')
    # Verifica se só tem espaços em branco
    print(f'Só tem espaços? {sim_ou_nao(algo.isspace())}')
    # Verifica se é um numérico (contém somente números)
    print(f'É um numérico (contém somente números)? {sim_ou_nao(algo.isnumeric())}')
    # Verifica se é alfabético (contém somente letras)
    print(f'É alfabético (contém somente letras)? {sim_ou_nao(algo.isalpha())}')
    # Verifica se é alfanumérico (contém letras ou números)
    print(f'É alfanumérico (contém letras ou números)? {sim_ou_nao(algo.isalnum())}')
    # Verifica se está todo em MAIÚSCULAS
    print(f'Está todo em MAIÚSCULAS? {sim_ou_nao(algo.isupper())}')
    # Verifica se está todo em minúsculas
    print(f'Está todo em minúsculas? {sim_ou_nao(algo.islower())}')
    # Verifica se está capitalizado (somente a primeira letra maiúscula)
    print(f'Está capitalizado (somente a primeira letra maiúscula)? {sim_ou_nao(algo.istitle())}')


