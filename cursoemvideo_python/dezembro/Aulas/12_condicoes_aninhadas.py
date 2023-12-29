# Curso Python #012 - Condições Aninhadas
# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if, elif e else em programas Python.

# Programas podem oferecer possibilidades extras caso haja mais de um caminho a ser seguido. Se uma determinada condição não é atendida, o programa deve conseguir oferecer essas outras opções

numero = 2

if numero == 1:
    print('Executa a primeira possibilidade')
elif numero == 2:
    print('Executa a segunda possibilidade')
elif numero == 3:
    print('Executa a terceira possibilidade')
else:
    print('Numero inválido!')

# OBSERVAÇÃO:
# elif pode ser usado quantas vezes for necessário, mas deve sempre ser usado após um if.
# else só pode ser usado como última opção mas também pode ser omitido.

# TESTANDO POSSIBILIDADES:
nome = str(input('Qual é o seu nome: '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil.')
elif nome in 'Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal.')

print(f'Tenha um bom dia, {nome}!')