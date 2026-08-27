# MIMO - 01 - Noções básicas de Python

# 01.2 - Usando variáveis

# As variáveis são chamadas de variáveis porque os valores que elas armazenam podem ser alterados. Podemos atualizar redeclarando a variável e dando-lhe um novo valor. Podemos atualizar as variáveis quantas vezes quisermos.
nome = 'José'
print(nome)
# O valor da variável nome é atualizado
nome = 'Antônio'
print(nome)
# O valor mais recente da variável será exibido e o anterior será esquecido

# Também podemos dar às variáveis os valores de outras variáveis
variavel_1 = '1 - Esse é o meu primeiro valor!'
print(variavel_1)

variavel_2 = '2 - Esse é o meu segundo valor!'
print(variavel_2)

variavel_3 = variavel_1  # Atribuímos ums variável como valor de outra
print(variavel_3)

# Quando atualizamos uma variável, ela esquece seu valor anterior. Aqui, podemos exibir a variável duas vezes e ver como seu valor é atualizado.

status = "Estudando"
status = "Descansando"
print(status)  # O valor da última instrução será exibido

# Expressões - valores combinados com operadores são outra maneira de atualizar variáveis. Podemos usar expressões para atualizar variáveis com base em seus valores anteriores.

# Podemos adicionar valores de strings com um sinal + (concatenação). Chamamos a adição de valores de cadeia de caracteres de expressão, pois a saída cria um único valor.
expressao = 'Essa parte do texto ' + 'se conecta a essa.'
print(expressao) # O resultado será uma string com os dois valores concatenados

# Quando as expressões contêm variáveis, elas usam os valores nas variáveis
texto_1 = 'Vamos unir essa parte '
print(texto_1)

texto_2 = 'com essa parte.'
print(texto_2)

print(texto_1 + texto_2)

# Como as expressões se tornam valores, podemos armazená-las em variáveis da mesma forma que os valores.
textao = texto_1 + texto_2
print(textao)

# Números

# Já vimos antes que as variáveis também podem armazenar números. Ao contrário das cadeias de caracteres, os valores numéricos não usam aspas.
numero = '1'  # valor string
numero = 1  # valor numérico

# Os números facilitam o controle de dados numéricos. Podemos criar expressões com números também.
calculo = '10' + '1'
print(calculo)  # O resultado será uma string, pois estamos utilizando dois valores desse tipo

calculo = 10 + 1
print(calculo)  # Nesse outro caso, o resultado será um número inteiro

# calulo = 10 + '1'  # O resultado será um erro, pois não podemos somar um número com uma string

# Alugns outros operadores aritméticos são:
# O sinal * para multiplicar números e o sinal / para dividir números. Também podemos usar variáveis com números para cálculos.

# Como as expressões se tornam valores, podemos armazenar resultados de cálculo em variáveis.

expressao = calculo + numero  # calculo vale 11 e numero vale 1
print(expressao)  # A expressao terá como valor a soma desses números