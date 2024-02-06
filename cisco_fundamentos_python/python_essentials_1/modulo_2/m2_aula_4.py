# 2.4.1 Variáveis - caixas em forma de dados

# Python irá ajudá-lo a armazenar resultados de expressões para utilizar posteriormente. Ele oferece "caixas" especiais (ou "contêineres", como podemos chamá-los) para essa finalidade, e essas caixas são chamadas de variáveis - o próprio nome sugere que o conteúdo desses contêineres pode ser variado (quase) de qualquer forma.

# O que todas as variáveis Python têm?
# um nome;
# um valor (o conteúdo do contêiner)

# Vamos começar com os problemas relacionados ao nome de uma variável.
# As variáveis não aparecem em um programa automaticamente. Como desenvolvedor, você deve decidir quantas variáveis e quais usar em seus programas.

# 2.4.2 Nomes de variáveis
# Se quiser dar um nome a uma variável, você deve seguir algumas regras estritas:

# O nome da variável deve ser composto de letras maiúsculas ou minúsculas, dígitos e o caractere _ (sublinhado)
# o nome da variável deve começar com uma letra;
# o caractere de sublinhado é uma letra;
# as letras maiúsculas e minúsculas são tratadas como diferentes (um pouco diferente do que no mundo real - Alice e ALICE são os mesmos nomes, mas em Python são dois nomes de variáveis diferentes e, consequentemente, duas variáveis diferentes);
# o nome da variável não deve ser nenhuma das palavras reservadas do Python (as palavras-chave).
# O Python não impõe restrições ao comprimento dos nomes de variáveis, mas isso não significa que um nome de variável longo seja melhor do que um nome curto.
# O Python permite que você use não apenas letras latinas, mas também caracteres específicos de idiomas que usam outros alfabetos.

# Observe que as mesmas restrições se aplicam a nomes de função.

# O PEP 8 - Guia de Estilo para Código Python recomenda a seguinte convenção de nomenclatura para variáveis e funções em Python:

# os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
# nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun, my_function)
# também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada

# Palavras-chave
# O Python reserva 33 palavras-chave: and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield, True, False, None.

# Eles são chamados de palavras-chave ou (mais precisamente) palavras-chave reservadas. Eles são reservados porque você não deve usá-los como nomes: nem para suas variáveis, nem funções, nem quaisquer outras entidades nomeadas que você deseja criar.

# 2.4.3 Como criar variáveis
# O valor de uma variável é o que você coloca nela. Pode variar com a frequência desejada. Pode ser um inteiro um momento, e um momento depois, e, se tornar uma string.
# Uma variável passa a existir como resultado da atribuição de um valor a ela. Ao contrário de outros idiomas, você não precisa declará-lo de nenhuma maneira especial.
# Se você atribuir qualquer valor a uma variável inexistente, a variável será criada automaticamente. Você não precisa fazer mais nada.

# A criação (ou seja, sua sintaxe) é extremamente simples: basta usar o nome da variável desejada, depois o sinal de igual (=) e o valor que deseja colocar na variável.

# Consiste em duas instruções simples:
# O primeiro deles cria uma variável chamada var e atribui um literal com um valor inteiro igual a 1.
var = 1
# O segundo imprime o valor da variável recém-criada no console.
print(var)

# 2.4.4 Como usar uma variável

# Você tem permissão para usar quantas declarações de variáveis forem necessárias para atingir seu objetivo.
# No entanto, você não pode usar uma variável que não existe (em outras palavras, uma variável que não recebeu um valor).

# Você pode usar a função print() e combinar texto e variáveis usando o operador + para gerar sequências e variáveis. Por exemplo:
var = "3.8.5"
print("Versão Python: " + var)

# O operador + é usado para concatenar (ou seja, juntar) duas sequências. Observe que o operador + não adiciona espaços entre as sequências, portanto, se você precisar deles, deverá adicioná-los explicitamente. Este operador só funciona se ambas as sequências forem do mesmo tipo (ou seja, ambas as sequências devem ser strings).

# Outra forma de concatenar strings é usando o operador de vírgula (,). Observe que o operador de vírgula adiciona um espaço entre as sequências. Este operador funciona com valores de qualquer tipo.
print("Versão Python:", var)

# Lembre-se: A função print() possui dois argumentos opcionais: sep e end. O valor padrão de sep é um único caractere de espaço, e o valor padrão de end é uma nova linha. Você pode alterar esses valores usando argumentos nomeados.

# 2.4.5 Como atribuir um novo valor a uma variável já existente

# Como você atribui um novo valor a uma variável que já existe? Da mesma forma. Você só precisa usar o sinal de igual.

# O sinal de igual é, na verdade, um operador de atribuição. Embora isso possa parecer estranho, o operador tem uma sintaxe simples e uma interpretação clara. Ela atribui o valor do argumento da direita para a esquerda, enquanto o argumento da direita pode ser uma expressão arbitrariamente complexa envolvendo literais, operadores e variáveis já definidas.

# A primeira linha do trecho cria uma nova variável chamada var e atribui 1 a ela. A instrução diz: atribua um valor de 1 a uma variável denominada var.
# Podemos dizer mais curto: "atribua 1 ao var", mas alguns preferem ler uma declaração como: var se torna 1.
var = 1
print(var)
# A terceira linha atribui a mesma variável com o novo valor retirado da própria variável, somada com 1. Vendo um registro como esse, um matemático provavelmente protestaria - nenhum valor pode ser igual a si mesmo mais um. Isso é uma contradição. Mas Python trata o sinal = não como igual a, mas como atribuir um valor a. Então, como você lê esse registro no programa?

# Pegue o valor atual da variável var, adicione 1 e armazene o resultado na variável var. Isso é uma autoatribuição. O Python permite que você faça isso. O resultado é que a variável var agora contém o valor 2.
# Com efeito, o valor da variável var tem sido incrementado por um, o que não tem nada a ver com a comparação da variável com qualquer valor.
var = var + 1  # var = 1 + 1
print(var)

# 2.4.6 Solução de problemas matemáticos simples
# Agora você deve conseguir construir um programa curto que resolva problemas matemáticos simples, como o teorema de Pitágoras:

# O quadrado da hipotenusa é igual à soma dos quadrados dos outros dois lados.

# O código a seguir avalia o comprimento da hipotenusa (ou seja, o lado mais longo de um triângulo retângular, o oposto do ângulo reto) usando o teorema de Pitágoras:


a = 3.0
b = 4.0
# Nota: precisamos usar o operador ** para avaliar a raiz quadrada como:
# √x = x(½) a raiz quadrada de x é igual a x elevado a meio.
c = (a ** 2 + b ** 2) ** 0.5
# c = √a2 + √b2
print("c =", c)

# 2.4.8 Operadores atalhos

# É hora do próximo conjunto de operadores que facilita a vida do desenvolvedor. Frequentemente, queremos usar uma e a mesma variável nos lados direito e esquerdo do operador =.
# Por exemplo, se precisamos calcular uma série de valores sucessivos de potências de 2, podemos usar uma parte como esta: x = x * 2

# O Python oferece uma maneira reduzida de escrever operações como essas, que podem ser codificadas da seguinte forma: x *= 2

# Vamos tentar apresentar uma descrição geral para essas operações. Se op for um operador de dois argumentos (esta é uma condição muito importante) e o operador for usado no seguinte contexto...:

# variável = variável operador expressão

# ... Então pode ser simplificado e exibido da seguinte forma:

# variável operador= expressão

"""
i = i + 2 * j
i += 2 * j

var = var / 2
var /= 2

rem = rem % 10
rem %= 10

j = j - (i + var + rem)
j -= (i + var + rem)

x = x ** 2
x **= 2
"""

# 2.4.11 RESUMO DA SEÇÃO
# Uma variável é um local nomeado reservado para armazenar valores na memória. Uma variável é criada ou inicializada automaticamente quando você atribui um valor a ela pela primeira vez.

# Cada variável deve ter um nome exclusivo ‒ um identificador. Um nome de identificador legal deve ser uma sequência não vazia de caracteres, deve começar com o sublinhado (_) ou uma letra e não pode ser uma palavra-chave do Python. O primeiro caractere pode ser seguido por sublinhados, letras e dígitos. Os identificadores em Python diferenciam maiúsculas de minúsculas.

# Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa declarar variáveis nela. Para atribuir valores a variáveis, você pode usar um operador de atribuição simples na forma do sinal de igual (=), ou seja, var = 1.

# Você também pode usar operadores de atribuição compostos (operadores de atalho) para modificar valores atribuídos a variáveis, por exemplo: var += 1 ou var /= 5 * 2.

# Você pode atribuir novos valores a variáveis já existentes usando o operador de atribuição ou um dos operadores compostos, por exemplo:

var = 2
print(var)
var = 3
print(var)
var += 1
print(var)

# Você pode combinar texto e variáveis usando o operador + e usar a função print() para gerar sequências e variáveis, por exemplo:

var = "007"
print("Agent " + var)

# a /= 2 * b
# a = a / (2 * b)