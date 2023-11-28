# Curso Python #04 - Primeiros comandos em Python3

# Os dados de texto são delimitados por aspas simples ou duplas. Podem conter letras, números e caracteres especiais.
# Todos os comandos são funções e devem ter parênteses.
# A função print() exibe no console o texto desejado
# A sintaxe é print('Seu texto')
print('Olá, mundo!')

# Se uma das aspas for omitida, o programa irá apresentar um erro de sintaxe. Caso as duas aspas sejam omitidas o programa irá exibir um erro diferente, pois irá interpretar cada palavra como uma variável além do erro de sintaxe.

# Também podemos exibir números. Números entre aspas são considerados textos!
# Os números são usados para cálculos matemáticos, por exemplo.
print(7 + 4) # Irá exibir a soma que é 11

# Se colocarmos os números entre as aspas e utilizarmos o operador de soma (+), o programa não irá apresentar um erro! Ele irá unir os dois textos. Essa ação é chamada de concatenação - O operador + une strings e soma valores numéricos.
print('7' + '4') # Exibe '74'

# Também é possível utilizar a vírgula para concatenar os valores. A diferença é que o operador de soma + só funciona com valores do mesmo tipo, por exemplo string + string ou número + número. A vírgula permite utilizar valores de tipos diferentes
print('7', 4) # Irá exibir '7' 4 - haverá um espaço, pois é o separador padrão ao utilizar vírgula na concatenação.
print('\n============ Parte prática ============\n')
# Variáveis são úteis para armazenar os valores. Recomenda-se utilizar letras minúsculas para nomeá-las. Toda variável é um objeto em Python.

# O símbolo de = é chamado de operador de atribuição. A sintaxe da atribuição é nome da variável - operador de atribuição - valor.
# Podemos ler o operador de atribuição como 'recebe'.
nome = 'Guanabara'
idade = 25
peso = 75.8

# Se utilizarmos as variáveis nas funções print() o seu valor será exibido. Concatenamos os valores com a vírgula, pois seus valores são de tipos diferentes.
print(nome, idade, peso)

# Se quisermos criar uma interatividade com o usuário utilizamos a função input(). Essa função recebe os dados pelo teclado, digitados pelo usuário.

# A sintaxe é input('Texto que será exibido')
# Vamos sobrescrever os valores das variáveis declaradas anteriormente usando input()

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
peso = input('Digite o peso: ')

# Exibindo os novos valores
print(nome, idade, peso)

# Podemos mudar o separador padrão da vírgula que é um espaço para outro caractere de preferência usando o atributo sep.
print(nome, idade, peso, sep=' - ')
