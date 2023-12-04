# MIMO - 01 - Noções básicas de Python

# 01.2 - Usando variáveis

# As variáveis são chamadas de variáveis porque os valores que elas armazenam podem ser alterados. Podemos atualizar redeclarando a variável e dando-lhe um novo valor. Podemos atualizar as variáveis quantas vezes quisermos.
nome = 'José'
print(nome)
nome = 'Antônio'
print(nome)

# Também podemos dar às variáveis os valores de outras variáveis
variavel_1 = 'Esse é o meu valor!'
print(variavel_1)
variavel_2 = 'Esse é o meu valor!'
print(variavel_2)
variavel_3 = variavel_1
print(variavel_3)

# Quando atualizamos uma variável, ela esquece seu valor anterior. Aqui, podemos exibir a variável duas vezes e ver como seu valor é atualizado.

status = "Estudando"
print(status)

status = "Descansando"
print(status)

# Expressões 

# Podemos adicionar valores de strings com um sinal + (concatenação). Chamamos a adição de valores de cadeia de caracteres de expressão, pois a saída cria um único valor.
expressao = 'Essa parte do texto ' + 'se conecta a essa.'
print(expressao)

# Quando as expressões contêm variáveis, elas usam os valores nas variáveis
texto_1 = 'Vamos unir essa parte '
texto_2 = 'com essa parte.'
print(texto_1 + texto_2)

# Como as expressões se tornam valores, podemos armazená-las em variáveis da mesma forma que os valores.
textao = texto_1 + texto_2
print(textao)

# Números

# Já vimos antes que as variáveis também podem armazenar números. Ao contrário das cadeias de caracteres, os valores numéricos não usam aspas.
numero = '1'
numero = 1

# Os números facilitam o controle de dados numéricos. Podemos criar expressões com números também.
calculo = '10' + '1'
print(calculo)
calculo = 10 + 1
print(calculo)

# Por exemplo, usamos o sinal * para multiplicar números e o sinal / para dividir números. Também podemos usar variáveis com números para cálculos. Como as expressões se tornam valores, podemos armazenar resultados de cálculo em variáveis.
expressao = calculo + numero
print(expressao)


