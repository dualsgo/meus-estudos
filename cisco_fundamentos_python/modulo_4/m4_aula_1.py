# 4.1 Seção 1 - Funções

# 4.1.1 Por que precisamos de funções?
# Até agora, discutimos funções principalmente como ferramentas para simplificar tarefas. Agora, vamos abordar a criação e uso de suas próprias funções.

# Às vezes, trechos de código são repetidos ou clonados no programa, o que pode ser problemático se houver erros ou modificações necessárias. A primeira condição para escrever funções é quando um fragmento de código aparece em mais de um lugar; nesse caso, isole-o em uma função chamada nos pontos onde o código original estava.

# Se o código se tornar tão extenso que a leitura e a manutenção se tornarem desafiadoras, a segunda condição é aplicada: divida-o em partes menores e implemente cada uma como uma função separada. Esse processo, conhecido como decomposição, simplifica o trabalho, permitindo que cada parte seja codificada e testada independentemente.

# Em resumo, escrever suas próprias funções é uma prática eficaz para evitar repetição de código, melhorar a legibilidade e facilitar a manutenção do programa.

# 4.1.2 Decomposição
# Quando um problema de programação é tão extenso que requer a colaboração de uma equipe, é essencial dividir o trabalho entre os desenvolvedores para garantir eficiência. Isso não apenas facilita a cooperação, mas também distribui a responsabilidade entre os membros da equipe.

# Cada desenvolvedor é encarregado de escrever um conjunto específico de funções bem definidas. Essas funções, quando combinadas nos módulos (abordaremos isso mais tarde), formarão o produto final. Portanto, ao dividir o trabalho entre programadores, é crucial decompor o problema de maneira que o produto possa ser implementado como um conjunto de funções independentes, reunidas em diferentes módulos.

# 4.1.3 De onde vêm as funções?
# Em geral, as funções vêm de pelo menos três lugares:

# do próprio Python - várias funções (como print()) são parte integrante do Python, e estão sempre disponíveis sem nenhum esforço adicional em nome do programador; chamamos essas funções de funções internas;

# dos módulos pré-instalados do Python - muitas funções, muito úteis, mas usadas muito menos frequentemente do que as integradas, estão disponíveis em vários módulos instalados junto com o Python; o uso dessas funções requer algumas etapas adicionais do programador para torná-las totalmente acessíveis (falaremos sobre isso daqui a pouco);

# diretamente do seu código - você pode escrever suas próprias funções, colocá-las dentro do código e usá-las livremente;

# há uma outra possibilidade, mas ela está conectada às classes, então vamos omitir isso por enquanto.

# 4.1.4 Sua primeira função
# Vamos começar com uma função muito simples. Vamos escrever uma função que exibe uma mensagem na tela e nada mais. A mensagem será sempre a mesma, mas você poderá usá-la em qualquer lugar do seu código, quantas vezes quiser. É bem simples, mas queremos que seja apenas um exemplo de transformação de uma parte repetida de um código em uma função.

# Se quisermos solicitar um valor do usuário, podemos usar a função input().
print("Entre um valor: ")
a = int(input())

print("Entre um valor: ")
b = int(input())

print("Entre um valor: ")
c = int(input())

# Note que as mensagens enviadas para o console pela função print() são sempre as mesmas. Claro, não há nada de ruim nesse código, mas tente imaginar o que você teria que fazer se seu chefe pedisse para você mudar a mensagem para torná-la mais educada, por exemplo, para começar com a frase "Por favor".
# Com pouco código, não seria um problema, mas e se houvesse centenas de mensagens como essa?
# Parece que você precisaria gastar algum tempo alterando todas as ocorrências da mensagem (você usaria uma área de transferência, é claro, mas isso não tornaria sua vida muito mais fácil). É óbvio que você provavelmente cometeria alguns erros durante o processo de alteração, e você (e seu chefe) ficaria um pouco frustrado.

# É possível separar uma parte que pode ser repetida, nomeá-la e torná-la reutilizável? (Isso significaria que uma alteração feita uma vez em um só lugar seria propagada para todos os lugares onde é usada. Obviamente, um código como esse só deve funcionar quando for iniciado explicitamente).

# Sim, é possível. É para isso que servem as funções.

# Você precisa defini-lo. A palavra 'define' é significativa aqui.
# É assim que a definição mais simples de função se parece:
'''
def function_name():
    function_body
'''

# Começa sempre com a palavra-chave def (de define)
# Depois de def passa o nome da função (as regras para nomear funções são as mesmas que para nomear variáveis)
# depois do nome da função, há um lugar para um par de parênteses (eles não contêm nada aqui, mas isso vai mudar em breve)
# a linha deve ser terminada com dois pontos;
# a linha logo após def inicia o corpo da função - um par (pelo menos um) de instruções necessariamente aninhadas, que serão executadas sempre que a função for chamada; nota: a função termina onde o aninhamento termina, então você precisa ter cuidado.
# as regras de aninhamento são as mesmas que para as instruções if, for, while, etc. - você pode usar espaços ou tabulações, mas não misture os dois.

# Estamos prontos para definir nossa função de prompt. Vamos dar o nome de message - aqui está:

def message():
    print("Entre um valor: ") # o corpo da função - observe a indentação
# A função é extremamente simples, mas totalmente utilizável. Atribuímos o nome de message, mas você pode nomear de acordo com o seu gosto. Vamos usá-lo.
# print("Entre um valor: ") será o efeito colateral da função - não é o que a função retorna, mas o que ela faz. A função não retorna nada, mas faz algo. É por isso que a chamamos de efeito colateral.

# Nosso código contém a definição de função agora:

print("Começamos aqui.")
print("terminamos aqui.")
# Nota: não usamos a função - não há nenhuma chamada dentro da função.

# Ao executá-lo, você vê a seguinte saída:
'''
Começamos aqui.
terminamos aqui.
'''

# Isso significa que o Python lê as definições da função e as lembra, mas não inicia nenhuma sem a sua permissão. Ou seja, precisamos dizer ao Python para executar a função. Isso é chamado de invocação da função.
# Nós modificamos o código agora - inserimos a chamada da função entre as mensagens de início e fim:

print("Começamos aqui.")
message() # chamada da função
print("terminamos aqui.")
# A saída está diferente agora:
"""
Começamos aqui.
Entre um valor: # mensagem da função
terminamos aqui.
"""
# O bloco de código definido como o corpo da função foi executado. O Python lembra o local onde a função foi chamada e retorna a esse local quando a função termina.
# A função não retorna nada, mas faz algo. É por isso que a chamamos de efeito.

# 4.1.5 Como funções funcionam
# quando você invoca uma função, o Python se lembra do local onde aconteceu e salta para a função invocada;
# o corpo da função é então executado;
# alcançar o final da função força o Python a retornar ao local imediatamente após o ponto de chamada.

# Há duas coisas muito importantes. Aqui está a primeira:
# Você não deve invocar uma função que não é conhecida no momento da invocação. Lembre - se o Python lê seu código de cima para baixo. Ela não vai olhar para frente para encontrar uma função que você esqueceu de colocar no lugar certo ("certo" significa "antes da invocação".)

"""
# Inserimos um erro neste código - Vê a diferença?
Movemos a função para o final do código. O Python consegue encontrá-lo quando a execução atinge a invocação? Não, não é. A mensagem de erro será:

NameError: name 'message' is not defined

# Não tente forçar o Python a procurar funções que não foram disponibilizadas no momento certo.



print("Começamos aqui.")
message()
print("terminamos aqui.") 


def message():
    print("Entre um valor: ")
"""
# Segundo: Você não deve ter uma função e uma variável com o mesmo nome.
# Dependendo da ordem em que você os define o código até pode funcionar, mas não é uma boa prática de programação. Você pode se confundir e o Python também.
# É boa prática usar um certo padrão para nomear funções com verbos que tornam sua função mais descritiva assim como deixar claro o que uma variável guarda.

# Vamos retornar ao nosso exemplo principal e empregar a função para o trabalho certo, como aqui:

def message():
    print("Entre um valor: ")

message() # chamada da função
a = int(input())
message() # chamada da função
b = int(input())
message() # chamada da função
c = int(input())

# O código funciona como antes, mas agora é muito mais fácil de ler e entender. Você pode ver que a função é chamada três vezes, mas o código que ela executa é escrito apenas uma vez. Isso é muito bom. Poderíamos também adicionar argumentos à função para torná-la ainda mais flexível, definindo um texto diferente para cada chamada.
# Claro que essa tarefa é simples demais para exigi-la de uma função, mas é apenas um exemplo. Você pode imaginar como isso pode ser útil em um programa maior.

# # 4.1.6 RESUMO DA SEÇÃO
# 1. Uma função é um bloco de código que executa uma tarefa específica quando a função é chamada (chamada). Você pode usar funções para tornar seu código reutilizável, melhor organizado e mais legível. As funções podem ter parâmetros e valores de retorno.

# 2. Há pelo menos quatro tipos básicos de funções no Python:

# - incorporadas que são parte integrante do Python (como a função de print()). Você pode ver uma lista completa das funções integradas do Python em https://docs.python.org/3/library/functions.html.
# - os que vêm de módulos pré-instalados (você aprenderá sobre eles no curso Fundamentos do Python 2)
# - funções definidas pelo usuário que são escritas pelos usuários para os usuários - você pode escrever suas próprias funções e usá-las livremente no código,
# - as funções lambda (você aprenderá sobre elas no curso Fundamentos do Python 2.)

# 3. Você pode definir sua própria função usando a palavra-chave def e a seguinte sintaxe:

# def your_function(optional_parameters):
    # o corpo da função

# Você pode definir uma função que não aceita argumentos, por exemplo:

def message():  # definindo uma função
    print("Olá")  # o corpo da função

message()  # chamando a função

# Você pode definir uma função que aceita argumentos, assim como a função de um parâmetro abaixo:

def hello(name):  # definindo uma função
    print("Olá,", name)  # o corpo da função

name = input("Entre um valor: ")

hello(name)  # chamando a função

# Falaremos sobre funções parametrizadas na próxima seção. Não se preocupe.