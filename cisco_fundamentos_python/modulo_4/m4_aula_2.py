# 4.2.1 Funções parametrizadas
# O poder total da função se revela quando pode ser equipado com uma interface capaz de aceitar dados fornecidos pelo invocador. Esses dados podem modificar o comportamento da função, tornando-a mais flexível e adaptável às condições variáveis.

# Um parâmetro é na verdade uma variável, mas há dois fatores importantes que tornam os parâmetros diferentes e especiais:

# parâmetros existem apenas dentro de funções nas quais eles foram definidos, e o único lugar onde o parâmetro pode ser definido é um espaço entre um par de parênteses na declaração def;
# a atribuição de um valor ao parâmetro é feita no momento da chamada da função, especificando o argumento correspondente.

# def function(parameter):
    ### corpo da função

# funciton(argument)

# Não se esqueça:
# parâmetros vivem em funções internas (este é o ambiente natural)
# argumentos existem fora das funções e são portadores de valores passados para os parâmetros correspondentes.

# Há uma fronteira clara e não ambígua entre esses dois mundos.

# Vamos agora melhorar o corpo da função:
# A definição especifica que nossa função opera em apenas um parâmetro chamado number. Você pode usá-lo como uma variável comum, mas apenas dentro da função - não é visível em nenhum outro lugar.

def message(number):
    print("Digite um número:", number)

# Um valor para o parâmetro chegará do ambiente da função. Lembre-se: especificar um ou mais parâmetros na definição de uma função também é um requisito, e você precisa preenchê-lo durante a chamada. Você deve fornecer quantos argumentos houver parâmetros definidos. Não fazer isso causará um erro.
"""
def message(number): # Função definida com um parâmetro
  print("Digite um número:", number)

message() # Função chamada sem argumento

# TypeError: message() missing 1 required positional argument: 'number'
"""
def message(number):
    print("Digite um número:", number)

message(1) # Digite um número: 1
message(598) # Digite um número: 598

# Você consegue ver como isso funciona? O valor do argumento usado durante a invocação (1) foi passado para a função, definindo o valor inicial do parâmetro chamado number.

# Temos que torná-lo sensível a uma circunstância importante. É legal e possível ter uma variável com o mesmo parâmetro de função.

# O trecho ilustra o fenômeno:
def message(number):
    print("Digite um número:", number)

number = 1234
message(1) # Digite um número: 1
print(number) # 1234

# Uma situação como essa ativa um mecanismo chamado shadowing:
# o parâmetro da função é obscurecido pela variável global com o mesmo nome.
# O parâmetro ainda existe, mas não é visível dentro da função.
# Evitamos esse fenômeno, dando nomes diferentes às variáveis e parâmetros.

# Uma função pode ter quantos parâmetros você quiser, mas quanto mais parâmetros tiver, mais difícil será memorizar suas funções e propósitos.

# Vamos modificar a função - ela tem dois parâmetros agora:
def message(what, number):
    print("Entrar", what, "número", number)

# Isso também significa que a invocação da função exigirá dois argumentos.
message("um", 1)

# Os tipos de parâmetros e argumentos não são verificados pelo Python. Você pode passar qualquer valor para qualquer parâmetro. O Python não se importa com isso. É sua responsabilidade garantir que os valores sejam adequados para o propósito da função.

# 4.2.2 Passagem de parâmetros posicionais
# Uma técnica que atribui o i-ésimo (primeiro, segundo e assim por diante) argumento para o i-ésimo (primeiro, segundo, etc.) parâmetro de função é chamada de passagem de parâmetro posicional, enquanto argumentos passados dessa maneira são chamados de argumento posicional.

# Você já usou, mas o Python pode oferecer muito mais. Vamos falar sobre isso agora.
def my_function(a, b, c): # a, b, c são parâmetros, exatamente nessa ordem
    print(a, b, c)
# Isso significa que os argumentos passados para a função devem ser colocados na mesma ordem.
my_function(1, 2, 3)

# Nota: a passagem de parâmetro posicional é usada intuitivamente por pessoas em várias ocasiões sociais. Por exemplo, pode-se aceitar que, quando nos apresentamos, mencionamos nossos nomes antes de nosso sobrenome, por exemplo, "Meu nome é John Doe".

# Vamos implementar esse costume social em Python. A função a seguir será responsável por apresentar alguém:
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction("Luke", "Skywalker") # Olá meu nome é Luke Skywalker
introduction("Jesse", "Quick") # Olá meu nome é Jesse Quick
introduction("Clark", "Kent") # Olá meu nome é Clark Kent

# A propósito, os húngaros fazem isso em ordem inversa.
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction("Skywalker", "Luke") # Olá meu nome é Skywalker Luke
introduction("Quick", "Jesse") # Olá meu nome é Quick Jesse
introduction("Kent", "Clark") # Olá meu nome é Kent Clark

# 4.2.3 Passagem de parametro por palavra-chave
# O Python oferece outra convenção para a passagem de argumentos, em que o significado do argumento é determinado por seu nome, e não por sua posição - é chamado de passagem de argumento de palavra-chave.
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction(first_name = "James", last_name = "Bond") # Olá meu nome é James Bond
introduction(last_name = "Skywalker", first_name = "Luke") # Olá meu nome é Luke Skywalker

# O conceito é claro - os valores passados para os parâmetros são precedidos pelos nomes dos parâmetros de destino, seguidos pelo sinal =.
# A posição não importa aqui - o valor de cada argumento sabe seu destino com base no nome usado.
# Obviamente, você não deve usar um nome de parâmetro inexistente. O Python não aceitará isso e gerará um erro. TypeError: introduction() got an unexpected keyword argument 'surname'

# 4.2.4 Mistura de argumentos posicionais e de palavras-chave
# Você pode combinar os dois estilos, se quiser - há apenas uma regra inquebrável:
# você precisa colocar argumentos posicionais antes dos argumentos das palavras-chave. Se você pensar por um momento, certamente entenderá o porquê.

# Seu objetivo é avaliar e apresentar a soma de todos os seus argumentos.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# A função, quando chamada da seguinte maneira:
adding(1, 2, 3) # 1 + 2 + 3 = 6
# Obviamente, você pode substituir essa chamada por uma variante de palavra-chave, como esta:
# adding(c = 1, a = 2, b = 3)

# Vamos tentar combinar os dois estilos agora.
# adding(3, c = 1, b = 2)
# Vamos analisar:
# o argumento (3) para o parâmetro a é passado usando a maneira posicional;
# os argumentos para c e b são especificados como palavras-chave.
# essa chamada é válida e produzirá a mesma saída que as duas chamadas anteriores.

# Porém, se você tentar fazer isso:
# adding(3, a = 1, b = 2)
# TypeError: adding() got multiple values for argument 'a'

# Você receberá um erro de tempo de execução. O Python não pode aceitar isso, pois não pode decidir qual valor deve ser atribuído ao parâmetro a - o valor posicional (3) ou o valor da palavra-chave (1).
# Tenha cuidado e cuidado com os erros. Se você tentar passar mais de um valor para um argumento, tudo que obterá será um erro de tempo de execução.

# 4.2.5 Funções parametrizadas – mais detalhes
# Às vezes, os valores de um determinado parâmetro são usados com mais frequência do que outros. Esses argumentos podem ter seus valores padrão (predefinidos) considerados quando seus argumentos correspondentes foram omitidos. Isso é chamado de parâmetro padrão. Também é usado para evitar erros de tempo de execução.

# Eles dizem que o sobrenome mais popular em inglês é Smith. Vamos tentar levar isso em conta.
def introduction(first_name, last_name="Smith"):
    print("Olá meu nome é", first_name, last_name)
# Você só precisa estender o nome do parâmetro com o sinal =, seguido pelo valor padrão.

introduction("James", "Doe") # Olá meu nome é James Doe
introduction("James") # Olá meu nome é James Smith - o valor padrão é usado aqui pois só foi passado um argumento
introduction(first_name="William") # Olá meu nome é William Smith

# Você pode usar argumentos posicionais e de palavras-chave em uma única chamada de função, mas você deve ter cuidado com a ordem dos argumentos posicionais. Eles devem vir primeiro.

# Você pode ir além se for útil. Ambos os parâmetros têm seus valores padrão agora, veja o código abaixo:
def introduction(first_name="John", last_name="Smith"):
    print("Olá meu nome é", first_name, last_name)

# Isso torna a seguinte chamada absolutamente válida:
introduction() # Olá meu nome é John Smith - nenhum argumento foi passado para a função e os valores padrão foram usados

# Os valores padrão são usados quando nenhum argumento é passado para o parâmetro correspondente. Diferente de caso você não defina valores padrão e não passe argumentos, você receberá um erro de tempo de execução.

# # 4.2.6 RESUMO DA SEÇÃO
# 1. Você pode passar informações para funções usando parâmetros. Suas funções podem ter quantos parâmetros forem necessários.

# Um exemplo de função de um parâmetro:
def hi(name):
    print("Oi,", name)

hi("Greg")

# Um exemplo de função de dois parâmetros:
def hi_all(name_1, name_2):
    print("Oi,", name_2)
    print("Oi,", name_1)

hi_all("Sebastian", "Konrad")

# Um exemplo de função de três parâmetros:
def address(street, city, postal_code):
    print("Seu endereço é:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Código postal: ")
c = input("Cidade: ")
address(s, c, p_c)

# 2. Você pode passar argumentos para uma função usando as seguintes técnicas:

# - passagem de argumento posicional em que a ordem dos argumentos passou importa (Ex. 1)
def subtra(a, b):
    print(a - b)

subtra(5, 2) # saídas: 3
subtra(2, 5) # saídas: -3

# - passagem de argumentos da palavra-chave (nomeada) na qual a ordem dos argumentos passados não importa (ex. 2)
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2) # saídas: 3
subtra(b=2, a=5) # saídas: 3
# - uma combinação de passagem de argumento de posição e de palavra-chave (por exemplo, 3.)
def subtra(a, b):
    print(a - b)

subtra(5, b=2) # saídas: 3
subtra(5, 2) # saídas: 3
# subtra(b=2, a) # SyntaxError: non-default argument follows default argument

# É importante lembrar que argumentos de posição não devem seguir argumentos de palavra-chave.
# É por isso que, se você tentar executar o seguinte trecho:

# Exemplo inválido
def subtra(a, b):
    print(a - b)

subtra(5, b=2) # saídas: 3
# Syntax Error
# subtra(a=5, 2) #  SyntaxError: positional argument follows keyword argument

# 3. Você pode usar a técnica de passagem de argumento da palavra-chave para predefinir um valor para um determinado argumento:
def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy") # saídas: Andy Smith
name("Betty", "Johnson") # saídas: Betty Johnson (the keyword argument replaced by "Johnson")


# Teste
"""
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
# SyntaxError: non-default argument follows default argument
"""
# O código apresenta um erro de sintaxe. Quando você define uma função em Python e fornece um valor padrão para um argumento, todos os argumentos subsequentes também devem ter valores padrão. No entanto, na função add_numbers, você deu um valor padrão apenas para o segundo argumento (b=2), deixando o terceiro argumento (c) sem valor padrão. A correção seria dar um valor padrão também para o argumento c ou reorganizar a ordem dos argumentos na definição da função. Aqui estão duas maneiras corretas de fazer isso:
"""
def add_numbers(a, b=2, c=0):
    print(a + b + c)

add_numbers(a=1, c=3)

"""