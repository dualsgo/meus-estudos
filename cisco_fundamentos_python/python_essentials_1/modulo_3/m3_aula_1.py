# 3.1.1 Perguntas e respostas
# Um programador cria um programa e o programa faz perguntas.
# Um computador executa o programa e fornece as respostas.
# O programa deve conseguir reagir conforme as respostas recebidas.

# Felizmente, os computadores sabem apenas dois tipos de respostas: 'Sim, isso é verdade' ou 'não, isso é falso'.

# Você nunca receberá uma resposta como "Deixe-me pensar", "Não sei" ou "provavelmente, sim, mas não tenho certeza".

# Para fazer perguntas, o Python usa um conjunto de operadores muito especiais. Vamos examiná-los um após o outro, ilustrando seus efeitos em alguns exemplos simples.

# 3.1.2 Comparação: operador de igualdade
# Pergunta: os dois valores são iguais?
# Para fazer essa pergunta, você usa o operador == (igual a).

# Não se esqueça dessa importante distinção:
# = é um operador de atribuição, por exemplo: "a = b" atribui a variável "a" com o valor de b;
# == A pergunta é: esses valores são iguais? então a == b compara a e b.

# É um operador binário com ligação do lado esquerdo. Ela precisa de dois argumentos e verifica se são iguais.

# Pregunta #1: Qual é o resultado da comparação a seguir? 2 == 2
# Resposta: True - claro, 2 é igual a 2. Python responderá True.
print(2 == 2)

# Pregunta #2: Qual é o resultado da comparação a seguir? 2 == 2.0
# Resposta: True - Python não se importa se você usa um ponto decimal ou não. O valor absoluto é o mesmo.
print(2 == 2.)

# Pergunta #3: Qual é o resultado da comparação a seguir? 2 == '2'
# Resposta: False - um valor inteiro não é igual a uma string.
print(2 == '2')

# Igualdade: o operador de igualdade (==)
# O operador == (igual a) compara os valores de dois operandos. Se forem iguais, o resultado da comparação é True. Se eles não forem iguais, o resultado da comparação é False.
valor_esquerdo = 2
valor_direito = 2
print(valor_esquerdo == valor_direito)   # True

# Desigualdade: o operador de desigualdade (!=)
# O operador "!=" (Não é igual a ou diferente de) também compara os valores de dois operandos.
# Aqui está a diferença: se eles são iguais, o resultado da comparação é False. Se eles não forem iguais, o resultado da comparação é True.
print(valor_esquerdo != valor_direito)   # False

# Operadores de comparação: maior que
# Você também pode fazer uma pergunta comparativa usando o > (maior que).
# Se quiser saber se há mais ovelhas negras do que brancas, escreva-as da seguinte forma:
black_sheep = 2   # Ovelhas negras
white_sheep = 2 * black_sheep   # Ovelhas brancas são duas vezes mais numerosas
var = black_sheep > white_sheep   # Mais ovelhas negras do que brancas? False

# Operadores de comparação: maior ou igual a
# O operador "maior que" tem outra variante especial, não estrita, mas é denotado de forma diferente em notação aritmética clássica: ≥ (maior que ou igual a). Há dois sinais subsequentes, não um.

# Comparação de operadores: menor que e menor ou igual que
# Como você provavelmente já adivinhou, os operadores usados neste caso são: o < (menor que) operador e seu irmão não rígido: ≤ (menor que ou igual a).
current_velocity_mph = 85   # Velocidade atual em milhas por hora
print(current_velocity_mph < 85)   # Menor que - False
print(current_velocity_mph <= 85)   # Menos que ou igual a - True

# Ambos os operadores (estrito e não-estrito), são operadores binários com ligação do lado esquerdo, e sua prioridade é maior do que a mostrada por "==" e "!=".

# 3.1.5 Utilização das respostas

# O que você pode fazer com a resposta (ou seja, o resultado de uma operação de comparação) que você obtém do computador?
# Há pelo menos duas possibilidades:
# primeiro, você pode memorizá-la (armazená-la em uma variável) e usá-la posteriormente. Como você faz isso? Bem, você usa uma variável arbitrária como esta:
number_of_lions = 3   # Número de leões
number_of_lionesses = 4   # Número de leoas
answer = number_of_lions >= number_of_lionesses   # O número de leões é maior ou igual ao número de leoas? Resposta: False
# answer armazena False
# O conteúdo da variável indicará a resposta para a pergunta.

# A segunda possibilidade é mais conveniente e muito mais comum: você pode usar a resposta para decidir sobre o futuro do programa.

# Agora precisamos atualizar nossa tabela de prioridades e colocar todos os novos operadores nela.
"""+, - (unários)
**, (exponenciação)
*, /, //, % (multiplicação, divisão, divisão inteira, resto)
+, - (binários)
<, <=, >, >= (comparação)
==, != (igualdade)"""

# 3.1.7 Condições e execução condicional
# Você já sabe fazer perguntas em Python, mas ainda não sabe como fazer uso racional das respostas. Você precisa ter um mecanismo que permita que você faça algo se uma condição for atendida, e não faça se não for.

# Para tomar essas decisões, o Python oferece uma instrução especial. Devido à sua natureza e aplicação, é chamada de instrução condicional (ou declaração condicional).

# if true_or_not:
#    do_this_if_true

# Essa declaração condicional consiste nos seguintes elementos, estritamente necessários, somente nesta e nesta ordem:

# a palavra-chave if;
# um espaço para separar a palavra-chave;
# uma expressão (uma pergunta ou uma resposta) cujo valor será interpretado apenas em termos de True (quando seu valor for diferente de zero) e False (quando for igual a zero);
# dois pontos seguidos por uma nova linha;
# uma instrução recuada ou um conjunto de instruções (pelo menos uma instrução é absolutamente necessária); o recuo pode ser obtido de duas maneiras: inserindo um número específico de espaços (a recomendação é usar quatro espaços de recuo) ou usando o caractere de tabulação;
# Nota: se houver mais de uma instrução na peça recuada, a indentação deve ser a mesma em todas as linhas; mesmo que você use as guias misturadas com os espaços, é importante tornar todos os recuos exatamente iguais - o Python 3 não permite a mistura de espaços e guias para o recuo.

# Como essa declaração funciona?
# Se a expressão true_or_not representar a verdade (ou seja, seu valor não for igual a zero), as instruções recuadas serão executadas;

# se a expressão true_or_not não representa a verdade (ou seja, seu valor é igual a zero), as instruções recuadas serão omitidas (ignoradas) e a próxima instrução executada será a seguinte ao nível de recuo original

"""
Na vida real, muitas vezes expressamos um desejo:
'Se o tempo estiver bom, vamos dar uma volta e então, vamos almoçar.'
Como você pode ver, almoçar não é uma atividade condicional e não depende do clima.
Sabendo quais condições influenciam nosso comportamento e assumindo que temos as funções sem parâmetros go_for_a_walk() e have_lunch(), podemos escrever o seguinte trecho:
"""
the_weather_is_good = True   # O tempo está bom
# Se alterarmos o valor da variável para False, o programa não executará a função.


def go_for_a_walk():   # Vamos dar uma volta
    print("Vamos dar uma volta")


def have_lunch():   # Vamos almoçar
    print("Vamos almoçar")


if the_weather_is_good:   # Se o tempo estiver bom
    go_for_a_walk()   # Vamos dar uma volta
have_lunch()   # Vamos almoçar, independentemente do tempo


# Execução condicional: o comando if

# O comando if é uma instrução condicional. Ele permite que você execute algumas instruções somente se uma determinada condição for atendida. Se a condição não for atendida, as instruções não serão executadas.
# As instruções que devem ser executadas se a condição for atendida são chamadas de bloco if. Elas devem ser indentations para identificar o bloco. Qualquer instrução não indentation após o bloco if será executada independentemente da condição.

# Execução condicional: o comando if-else
# O comando else é uma instrução condicional que executa algumas instruções caso a condição do comando if não seja atendida. Em outras palavras, nos fornece uma alternativa para o bloco if.

# A execução senão é a seguinte:
# se a condição for avaliada como True a instrução if é executada e a instrução condicional chega ao fim;
# se a condição for avaliada como False, a instrução else é executada e a instrução condicional chega ao fim.

# Tudo o que dissemos sobre a indentação funciona da mesma maneira dentro do ramo else:

# Comandos if-else aninhados
# Primeiro, considere o caso em que a instrução colocada após o if é outra if.

# Leia o que planejamos para este domingo:
# Se o tempo estiver bom, vamos dar uma volta.
# Se encontrarmos um bom restaurante, almoçaremos lá.
# Caso contrário, vamos comer um sanduíche.
# Se o tempo estiver ruim, vamos ao teatro.
# Se não houver ingressos, faremos compras no shopping mais próximo.

# Vamos escrever um programa que implemente esse plano. Aqui está:

the_weather_is_good = False   # O tempo está bom
we_have_tickets = True   # Temos ingressos
we_have_found_a_restaurant = True   # Encontramos um restaurante
we_have_found_a_shopping_mall = False   # Encontramos um shopping


def go_for_a_walk():   # Vamos dar uma volta
    print("Vamos dar uma volta!")


def have_lunch():   # Vamos almoçar
    print("Vamos almoçar")


def go_to_the_theatre():   # Vamos ao teatro
    print("Vamos ao teatro")


def go_shopping():   # Vamos fazer compras
    print("Vamos fazer compras")


if the_weather_is_good:   # Se o tempo estiver bom
    go_for_a_walk()   # Vamos dar uma volta
    if we_have_found_a_restaurant:   # Se encontrarmos um bom restaurante
        have_lunch()   # Vamos almoçar
    else:   # Senão
        print("Vamos comer um sanduíche")   # Vamos comer um sanduíche
else:   # Senão
    go_to_the_theatre()   # Vamos ao teatro
    if we_have_tickets:   # Se tivermos ingressos
        print('Temos tickets. Vamos assistir a peça.')
    else:   # Senão
        go_shopping()
        if we_have_found_a_shopping_mall:
            go_shopping()
        else:   # Senão
            print("Vamos assistir TV")   # Vamos assistir TV


# esse uso da instrução if é conhecido como aninhamento; lembre-se de que todo else se refere ao if que está no mesmo nível de indentação; você precisa saber disso para determinar como os ifs e else se combinam;
# considere como o recuo melhora a legibilidade e torna o código mais fácil de entender e rastrear.

# 3.1.8 Análise de amostras de código
# Todos os programas resolvem o mesmo problema: eles encontram o maior de vários números e o imprimem. Vamos começar com o caso mais simples:
# como identificar o maior de dois números:

# Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprimir o resultado
print("O maior número é:", larger_number)

# se qualquer uma das ramificações if-elif-else contiver apenas uma instrução, você poderá codificá-la de forma mais abrangente (não é necessário criar uma linha recuada após a palavra-chave, mas apenas continuar a linha após os dois pontos)
"""
if number1 > number2: larger_number = number1 else: larger_number = number2
"""
# Vamos encontrar o maior de três números. Será que vai ampliar o código?
# Supomos que o primeiro valor seja o maior. Em seguida, verificamos essa hipótese com os dois valores restantes.

# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

# Assumimos temporariamente que o primeiro número é o maior deles.
largest_number = number1

# Nós verificamos se o segundo número é maior que o maior_número atual e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2

# Nós verificamos se o terceiro número é maior que o maior_número atual e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3

# Imprimir o resultado
print("O maior número é:", largest_number)

# 3.1.9 Pseudocódigo e introdução aos loops
# Agora você deve conseguir escrever um programa que encontre o maior de quatro, cinco, seis ou até mesmo dez números. Você já conhece o esquema, então estender o tamanho do problema não será particularmente complexo.

# Mas o que acontece se pedirmos que você escreva um programa que encontre o maior de duzentos números? Você consegue imaginar o código? Você precisará de duzentas variáveis. Se duzentas variáveis não forem ruins o suficiente, tente imaginar a busca pelo maior de um milhão de números.

# Imagine um código que contenha 199 instruções condicionais e duzentas invocações da função input(). Felizmente, você não precisa lidar com isso. Há uma abordagem mais simples.

# Executar uma determinada parte do código mais de uma vez é chamado de loop. O significado desse termo é provavelmente óbvio para você.

# Informações adicionais
# O Python geralmente vem com muitas funções internas que farão o trabalho para você. Por exemplo, para encontrar o maior número de todos, você pode usar uma função interna do Python chamada max(). Você pode usá-lo com vários argumentos. Analise o código abaixo:

# Verifique qual dos números é o maior e passe-o para a variável de número_maior.
largest_number = max(number1, number2, number3)

# Imprimir o resultado.
print("O maior número é:", largest_number)

# Da mesma forma, você pode usar a função min() para retornar o número mais baixo.

# 3.1.13 RESUMO DA SEÇÃO

# 1. Os operadores de comparação (também conhecidos como relacionais) são
# usados para comparar valores. A tabela abaixo ilustra como os operadores de comparação funcionam, supondo que:
# x = 0
# y = 1
# z = 0

# == retorna True se os valores dos operandos forem iguais e False caso contrário
# x == y # False
# x == z  # True
# "!=" retorna True se os valores dos operandos não forem iguais e False caso contrário
# x "!=" y # True
# x "!=" z # False

# >	True se o valor do operando esquerdo for maior que o valor do operando direito e False caso contrário
# x > y  # False
# y > z  # True

# <	True se o valor do operando esquerdo for menor que o valor do operando direito e False caso contrário
# x < y  # True
# y < z  # False

# >= True se o valor do operando esquerdo for maior ou igual ao valor do operando da direita e False caso contrário
#  x >= y  # False
#  x >= z  # True
#  y >= z  # True

# <= True se o valor do operando esquerdo for menor ou igual ao valor do operando à direita e False caso contrário
#  x <= y  # True
#  x <= z  # True
#  y <= z   # False

# 2. Quando você deseja executar algum código apenas se uma determinada condição for atendida, você pode usar uma declaração condicional: uma única declaração if, por exemplo:

x = 10
if x == 10:   # condição
    print("x é igual a 10")   # Executado se a condição for True.

# uma série de declarações if, por exemplo:
# Cada declaração if é testada separadamente.

x = 10
if x > 5:  # condição um
    print("x é maior que 5")   # Executado se a condição um for True.
if x < 10:  # condição dois
    print("x é menor que 10")   # Executado se a condição dois for True.
if x == 10:  # condição três
    print("x é igual a 10")   # Executado se a condição três for True.


# uma declaração if-else, por exemplo:

x = 10
if x < 10:  # condição
    print("x é menor que 10")   # Executado se a condição for True.
else:
    print("x é maior ou igual a 10")   # Executado se a condição for False.


# uma série de instruções if seguidas de um else, por exemplo:
x = 10

if x > 5:  # condição um
    print("x é maior que 5")   # Executado se a condição um for True.
if x < 10:  # condição dois
    print("x é menor que 10")   # Executado se a condição dois for True.
if x == 10:  # condição três
    print("x é igual a 10")   # Executado se a condição três for True.

# Cada um if é testado separadamente. O corpo do else é executado se o último if for False.

# A declaração if-elif-else, por exemplo:
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("senão não será executado")

# Se a condição para if for False, o programa verifica as condições dos blocos elif subsequentes - o primeiro bloco elif que é True é executado. Se todas as condições forem False, o bloco else será executado.

# Instruções condicional aninhadas, por exemplo:

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("aninhado: x == 6")
    elif x == 10:  # True
        print("aninhado: x == 10")
    else:
        print("aninhado: else")
else:
    print("else")