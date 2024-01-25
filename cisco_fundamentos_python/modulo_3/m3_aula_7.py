# 3.7 Seção 7 - Listas em aplicativos avançados

# 3.7.1 Listas em listas
# As listas podem ser armazenadas em listas - isso é chamado de lista aninhada.

# Listas aninhadas, também conhecidas como listas dentro de listas, são estruturas de dados em que uma lista contém outras listas como elementos. Isso permite criar estruturas mais complexas, representando dados em várias dimensões. Vamos explorar esse conceito com uma explicação didática e um exemplo prático.

# Em Python, uma lista é uma coleção ordenada de elementos que pode conter diferentes tipos de dados. Por exemplo:
animais = ['cachorro', 'gato', 'pássaro']

# Agora, imagine que cada elemento da lista acima pode ter informações adicionais, como idade e cor. Em vez de criar duas listas separadas (uma para os tipos de animais e outra para as informações adicionais), podemos usar listas aninhadas:
animais_info = [['cachorro', 3, 'marrom'], ['gato', 2, 'preto'], ['pássaro', 1, 'verde']]

# Aqui, cada sublista contém o nome do animal, idade e cor. Esta é uma lista aninhada.

# Lista aninhada com informações sobre animais
animais_info = [['cachorro', 3, 'marrom'], ['gato', 2, 'preto'], ['pássaro', 1, 'verde']]

# Acessando informações específicas
primeiro_animal = animais_info[0] # Primeiro elemento da lista animais_info
nome_do_primeiro_animal = primeiro_animal[0] # Primeiro elemento da lista primeiro_animal
idade_do_primeiro_animal = primeiro_animal[1] # Segundo elemento da lista primeiro_animal
cor_do_primeiro_animal = primeiro_animal[2] # Terceiro elemento da lista primeiro_animal

# Exibindo informações
print(f"Nome: {nome_do_primeiro_animal}")
print(f"Idade: {idade_do_primeiro_animal} anos")
print(f"Cor: {cor_do_primeiro_animal}")

# Cada lista dentro da lista é um elemento, sendo assim recebe um índice que pode ser acessado. Além disso, cada elemento dentro da lista aninhada também pode ser acessado por meio de um índice. Por exemplo:

print(animais_info[0][2]) # Acessando o terceiro elemento da primeira lista da lista animais_info.

# Lista de compreensão - List Comprehension
# Uma compreensão de lista é, na verdade, uma lista, mas criada em andamento durante a execução do programa e não é descrita estaticamente.

# A sintaxe é a seguinte: [expr for element in iterable]

# A parte entre colchetes especifífca os dados que serão armazenados na lista e a cláusula for especifica os elementos que serão iterados.

squares = [x ** 2 for x in range(10)] # Cria uma lista com os quadrados dos números de 0 a 9.

# x ** 2 - especifica os dados que serão armazenados na lista. O valor de x será dado pela cláusula for, a cada iteração.
# for x in range(10) - especifica os elementos que serão iterados. O valor de x será dado pela cláusula for, a cada iteração no intervalo de 0 a 9.

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

twos = [2 ** i for i in range(8)] # Cria uma lista com as potências de 2 de 0 a 7.

# 2 ** i - especifica os dados que serão armazenados na lista. O valor de i será dado pela cláusula for, a cada iteração.
# for i in range(8) - especifica os elementos que serão iterados. O valor de i será dado pela cláusula for, a cada iteração no intervalo de 0 a 7.

print(twos) # [1, 2, 4, 8, 16, 32, 64, 128]

odds = [x for x in squares if x % 2 != 0] # Cria uma lista com os números ímpares da lista squares. Podemos usar uma lista existente para criar uma nova lista.

# x - especifica os dados que serão armazenados na lista. O valor de x será dado pela cláusula for, a cada iteração se atender a condição especificada na cláusula if. é como dizer "Adicione o valor x a lista odds se o valor z da lista squares atender a condição (ser ímpar)".

# 3.7.2 Matrizes bidimensionais
# Uma matriz bidimensional é uma lista de listas. Cada lista dentro da lista é uma linha da matriz.

tabuleiro = []

for i in range(8):
    linha = [0 for i in range(8)] # Cria uma lista de 8 elementos com o valor 0.
    tabuleiro.append(linha) # Adiciona a lista linha a lista tabuleiro.
    
    print(tabuleiro) # Serão exibidas 8 listas com 8 elementos cada.
    
# Como as compreensões da lista podem ser aninhadas, podemos reduzir a criação da placa da seguinte maneira:

tabuleiro = [[0 for i in range(8)] for j in range(8)] # Cria uma lista de 8 listas com 8 elementos cada.

# tabuleiro - é a lista que será criada.
# [0 for i in range(8)] - especifica os dados que serão armazenados na lista. O valor de 0 será armazenado na lista tabuleiro, a cada iteração.
# for j in range(8) - especifica os elementos que serão iterados. O valor de j será dado pela cláusula for, a cada iteração no intervalo de 0 a 7.

# Resumidamente a parte interna da compreensão da lista cria uma lista com 8 elementos com o valor 0 e a parte externa cria uma lista com 8 listas com 8 elementos cada.

# Cada campo contém um par de índices que devem ser dados para acessar o conteúdo do campo:

# Vamos colocar algumas peças de xadrez no tabuleiro. Primeiro, vamos adicionar todas as torres:
tabuleiro[0][0] = "Torre Preta"
tabuleiro[0][7] = "Torre Preta"
tabuleiro[7][0] = "Torre Branca"
tabuleiro[7][7] = "Torre Branca"
# Cavalheiros
tabuleiro[0][1] = "Cavalo Preto"
tabuleiro[0][6] = "Cavalo Preto"
tabuleiro[7][1] = "Cavalo Branco"
tabuleiro[7][6] = "Cavalo Branco"


# 3.7.3 Natureza multidimensional das listas: aplicações avançadas

# Vamos aprofundar a natureza multidimensional das listas. Para encontrar qualquer elemento de uma lista bidimensional, você precisa usar duas coordenadas:

# a vertical (número da linha)
# e horizontal (número da coluna).

# Imagine que você está desenvolvendo um software para uma estação meteorológica automática. O dispositivo registra a temperatura do ar a cada hora e faz isso durante todo o mês. Isso gera um total de 24 × 31 = 744 valores. Vamos tentar criar uma lista capaz de armazenar todos esses resultados.

# Primeiro, você precisa decidir que tipo de dados seria adequado para essa aplicação. Nesse caso, um float seria o melhor, já que este termômetro é capaz de medir a temperatura com uma precisão de 0,1 ° C.

# Em seguida, você toma uma decisão arbitrária de que as linhas gravarão as leituras de hora em hora (para que a linha tenha 24 elementos) e cada uma das linhas será atribuída a um dia do mês (vamos supor que cada mês tenha 31 dias, então você precisa de 31 linhas). Aqui está o par apropriado de compreensões (h é para hora, d para dia):


temperaturas = [[0.0 for h in range(24)] for d in range(31)]

# Toda a matriz está preenchida com zeros agora. Você pode supor que ela é atualizada automaticamente usando agentes de hardware especiais. O que você precisa fazer é esperar que a matriz seja preenchida com medidas.

# Agora é hora de determinar a temperatura média mensal ao meio-dia. Adicione todas as 31 leituras gravadas ao meio-dia e divida a soma por 31. Você pode supor que a temperatura da meia-noite é armazenada primeiro. Aqui está o código relevante:
temps = [[0.0 for h in range(24)] for d in range(31)] # Lista bidimensional com 31 linhas e 24 colunas.
total = 0.0 # Variável para armazenar a soma das temperaturas.

for day in temps: # Loop através da lista temps.
    total += day[11] # Adiciona o valor da temperatura ao meio-dia a variável total.

average = total / 31 # Calcula a temperatura média ao meio-dia.

print("Temperatura média ao meio-dia:", average)

# Observação: a variável day usada pelo loop for não é escalar; cada passagem pela matriz day itera por todas as linhas na temps a atribui às linhas subsequentes da matriz; portanto, é uma lista. Ele precisa ser indexado com 11 para acessar o valor de temperatura medido ao meio-dia. Em outras palavras, day[11] é um elemento de uma lista que é um elemento de outra lista.

# Agora, encontre a temperatura mais alta durante todo o mês - veja o código:
temps = [[0.0 for h in range(24)] for d in range(31)] # Lista bidimensional com 31 linhas e 24 colunas.

highest = -100.0 # Variável para armazenar a maior temperatura.

for day in temps: # Loop através da lista temps.
    for temp in day: # Loop através da lista day.
        if temp > highest: # Se o valor da temperatura for maior que o valor da variável highest:
            highest = temp # Atribui o valor da temperatura a variável highest.

print("A maior temperatura foi:", highest)

# a variável day itera por todas as 31 linhas na matriz temps. Cada dia (day) é uma lista de 24 elementos (horas). A variável temp itera por todos os 24 elementos da linha atual (day) que são valores de temperatura.

# O Python não limita a profundidade da inclusão na lista. Aqui você pode ver um exemplo de uma matriz tridimensional:

# Imagine um hotel. É um grande hotel composto de três edifícios, de 15 andares cada. Há 20 salas em cada andar. Para isso, você precisa de uma matriz que possa coletar e processar informações sobre as salas ocupadas/livres.
# Primeira etapa - o tipo dos elementos da matriz. Nesse caso, um valor booleano (True/False) seria adequado.
# Etapa dois - Análise calma da situação. Resuma as informações disponíveis: três edifícios, 15 andares, 20 salas.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# A lista rooms é uma lista tridimensional. A primeira dimensão (índice 0) representa o número do edifício (0, 1 ou 2). A segunda dimensão (índice 1) representa o número do andar (0 a 14). A terceira dimensão (índice 2) representa o número da sala (0 a 19).

# Agora você pode reservar um quarto para dois noivos: no segundo edifício, no décimo andar, quarto 14:

rooms[1][9][13] = True # Reserva o quarto 14 do décimo andar do segundo edifício.

# Verifique se há vagas no 15º andar do terceiro edifício:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# 3.7.4 RESUMO DA SEÇÃO

# 1. A compreensão da lista permite criar novas listas a partir das existentes de forma concisa e elegante. A sintaxe de uma compreensão de lista tem a seguinte aparência:

# [expressão para elemento na lista se condicional]
 
# que é equivalente ao seguinte código:

# for element in list:
#     if conditional:
#         expression
 
# Aqui está um exemplo de compreensão de lista - o código cria uma lista de cinco elementos preenchida com os cinco primeiros números naturais elevados à potência de 3:

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]


# 2. Você pode usar listas aninhadas em Python para criar matrizes (ou seja, listas bidimensionais). Por exemplo:

# Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)

table = [
        [":(", ":)", ":(", ":)"],
        [":)", ":(", ":)", ":)"],
        [":(", ":)", ":)", ":("],
        [":)", ":)", ":)", ":("]
        ]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'


# 3. Você pode aninhar quantas listas desejar, criando assim listas n-dimensionais, por exemplo, matrizes de três, quatro ou até mesmo sessenta e quatro dimensões. Por exemplo:

# Cubo - uma matriz tridimensional (3x3x3)

cube = [ # representa a primeira dimensão
        [ # representa a segunda dimensão - indice 0
        [':(', 'x', 'x'], # representa a terceira dimensão - indice 0
        [':)', 'x', 'x'], # representa a terceira dimensão - indice 1
        [':(', 'x', 'x']  # representa a terceira dimensão - indice 2
        ],

        [ # representa a segunda dimensão - indice 1
        [':)', 'x', 'x'], # representa a terceira dimensão - indice 0
        [':(', 'x', 'x'], # representa a terceira dimensão - indice 1
        [':)', 'x', 'x']  # representa a terceira dimensão - indice 2
        ],

        [ # representa a segunda dimensão - indice 2
        [':(', 'x', 'x'], # representa a terceira dimensão - indice 0
        [':)', 'x', 'x'], # representa a terceira dimensão - indice 1
        [':)', 'x', 'x']  # representa a terceira dimensão - indice 2
        ]
        ]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'



