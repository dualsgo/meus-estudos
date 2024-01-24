# 3.4.1 Por que precisamos de listas?

# Pode ser que você precise ler, armazenar, processar e, finalmente, imprimir dezenas, talvez centenas, talvez até milhares de números. O que fazer então? Você precisa criar uma variável separada para cada valor? Você precisará passar longas horas escrevendo declarações como a abaixo?
"""
var1 = int(input())
var2 = int(input())
var3 = int(input())
var4 = int(input())
var5 = int(input())
var6 = int(input())
"""
# Pense em como seria conveniente declarar uma variável que pudesse armazenar mais de um valor. Por exemplo, uma centena ou mil ou até dez mil. Ainda seria a mesma variável, mas muito ampla e espaçosa. Soa atraente? Talvez, mas como ele lidaria com um contêiner tão cheio de valores diferentes? Como ela escolheria a que você precisa? E se você pudesse numerá-las? E então diga: dê-me o valor número 2; atribua o valor número 15; aumente o número do valor 10000.

# A resposta é: use listas.
# Vamos criar uma variável chamada numbers; ela é atribuída com não apenas um número, mas é preenchida com uma lista composta por cinco valores 

# Digamos o mesmo usando a terminologia adequada: numbers são uma lista que consiste em cinco valores, todos eles números. Também podemos dizer que essa declaração cria uma lista de comprimento igual a cinco (pois há cinco elementos dentro dela).

# Os elementos em uma lista podem ter tipos diferentes. Alguns deles podem ser números inteiros, outros carros alegóricos e outros ainda podem ser listas.

# Python adotou uma convenção afirmando que os elementos em uma lista são sempre numerados começando do zero. Isso significa que o item armazenado no início da lista terá o número zero. Como há cinco elementos em nossa lista, o último deles é atribuído o número quatro. Não se esqueça:
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# indice:   0,  1,  2, 3,  4,  5,  6,  7,  8
# nota: a lista começa com um colchete aberto e termina com um colchete fechado; o espaço entre os colchetes é preenchido com cinco números separados por vírgulas)

# 3.4.2 Indexando listas
# Como você altera o valor de um elemento escolhido na lista?

# Vamos atribuir um novo valor de 111 ao primeiro elemento na lista. Fazemos isso da seguinte forma:
numbers[0] = 111 # numbers é o nome da lista, e 0 é o índice do primeiro elemento da lista que atualmente é 12. O valor 111 substitui o valor 12.

# E agora queremos que o valor do quinto elemento seja copiado para o segundo elemento - você consegue adivinhar como fazer isso?
numbers[1] = numbers[4] # numbers[4] é o quinto elemento da lista. O valor 66 é copiado para o segundo elemento da lista que deixa de ser 10 e passa a ser 66.

# O valor entre parênteses que seleciona um elemento da lista é chamado de índice, enquanto a operação de seleção de um elemento da lista é conhecida como indexação.

# 3.4.3 Acesso ao conteúdo da lista
# Cada um dos elementos da lista pode ser acessado separadamente. Por exemplo, ele pode ser impresso:
print(numbers[0]) # Acessando o primeiro elemento da lista. 
# Resultado: 111

# Como você pode ver no editor, a lista também pode ser impressa como um todo, assim como aqui:
print(numbers) # Acessando a lista inteira.
# Resultado: [111, 10, 32, 3, 66, 17, 42, 99, 20]

# Como você provavelmente já deve ter notado antes, o Python adota uma saída especial para as listas - elas são impressas entre colchetes e separadas por vírgulas. Isso torna a lista muito fácil de reconhecer.

# A função len()
# O comprimento de uma lista pode variar durante a execução. Novos elementos podem ser adicionados à lista, enquanto outros podem ser removidos. Isso significa que a lista é uma entidade muito dinâmica.

# Se quiser verificar o comprimento atual da lista, você pode usar uma função chamada len() (o nome vem do comprimento).
# A função usa o nome da lista como argumento e retorna o número de elementos armazenados atualmente na lista (em outras palavras, o comprimento da lista).
print(len(numbers)) # Acessando o tamanho da lista. 
# Resultado: 9

# 3.4.4 Remover elementos de uma lista
# Qualquer um dos elementos da lista pode ser removido a qualquer momento - isso é feito com uma instrução chamada del (delete). Nota: é uma instrução, não uma função.
# Sintaxe: del list[index]

# Você precisa apontar para o elemento a ser removido - ele desaparecerá da lista e o comprimento da lista será reduzido em um.
numbers =  [111, 10, 32, 3, 66, 17, 42, 99, 20] # Criando uma lista com 9 elementos.
del numbers[1] # Removendo o segundo elemento da lista. 10
print(len(numbers)) # Acessando o tamanho da lista após a remoção. Resultado: 8
print(numbers) # Acessando a lista inteira. Resultado: [111, 32, 3, 66, 17, 42, 99, 20]

# Você não pode acessar um elemento que não existe - você não pode obter seu valor nem atribuir um valor a ele. Ambas as instruções causarão erros de tempo de execução agora:

# print(numbers[8]) # Acessando um elemento que não existe.
# # Resultado: IndexError: list index out of range

# 3.4.5 Os índices negativos são legais
# Pode parecer estranho, mas os índices negativos são legais e podem ser muito úteis.

# Um elemento com um índice igual a -1 é o último na lista.
print(numbers[-1]) # Acessando o último elemento da lista. 
# Resultado: 20

# Da mesma forma, o elemento com um índice igual a -2 é o penúltimo na lista, e assim por diante.

# Além de del, você pode usar o método pop() para remover um elemento da lista. O método pop() remove o último elemento da lista e o retorna.
# Se você não especificar o índice, o método pop() removerá e retornará o último elemento da lista, mas pop() aceita um argumento opcional que especifica o índice do elemento a ser removido.

# remove() é um método que remove o primeiro elemento com um valor especificado, ou seja, a primeira ocorrência de um valor especificado.
# O método remove() aceita um argumento que é o valor do elemento a ser removido. Se não houver nenhum elemento com o valor especificado, o Python gerará um erro.
# é boa prática verificar se o elemento existe na lista antes de removê-lo, utilizando o operador in. 

# del, pop e remove são métodos de lista que alteram a lista. Eles não retornam nenhum valor. Se você tentar atribuir o resultado a uma nova variável, a nova variável será None. 
# Cada um funciona melhor em situações diferentes. del remove um elemento com um índice especificado. pop remove o último elemento da lista. remove() remove o primeiro elemento com um valor especificado.

# Ao contrário de del e remove, o resultado de pop pode ser atribuído a uma nova variável. O valor atribuído será o elemento removido da lista.
# pop()
numbers =  [111, 10, 32, 3, 66, 17, 42, 99, 20]
print(numbers.pop()) # Removendo o último elemento da lista. Resultado: 20
print(numbers) # Acessando a lista inteira. Resultado: [111, 10, 32, 3, 66, 17, 42, 99]
print(numbers.pop(3)) # Removendo o elemento de índice 3 da lista. Resultado: 3
print(numbers) # Acessando a lista inteira. Resultado: [111, 10, 32, 66, 17, 42, 99]
valor_removido = numbers.pop(3) # Removendo o elemento de índice 3 da lista e atribuindo o valor removido à variável valor_removido.
print(valor_removido) # Acessando o valor removido. Resultado: 66

# 3.4.7 Funções x métodos

# Um método é um tipo específico de função - ele se comporta como uma função e se parece com uma função, mas difere na maneira em que atua e em seu estilo de invocação.

# Uma função não pertence a nenhum dado - ela obtém dados, pode criar novos dados e (geralmente) produz um resultado.

# Um método faz tudo isso, mas também é capaz de alterar o estado de uma entidade selecionada.

# Um método pertence aos dados para os quais trabalha, enquanto uma função pertence ao código inteiro.

# Isso também significa que a invocação de um método requer alguma especificação dos dados dos quais o método é invocado.

# Pode parecer confuso aqui, mas vamos lidar com isso em profundidade quando nos aprofundarmos na programação orientada a objeto.

# Em geral, uma chamada de função típica pode ser assim:
# result = function(arg)

# A função usa um argumento, faz alguma coisa e retorna um resultado.

# Uma invocação típica de método geralmente se parece com isso:
# result = data.method(arg)

# Nota: o nome do método é precedido pelo nome dos dados proprietários do método. Em seguida, adicione um ponto, seguido pelo nome do método, e um par de parênteses que encerra os argumentos.

# O método se comportará como uma função, mas pode fazer algo mais - ele pode alterar o estado interno dos dados dos quais foram chamados.

# Você pode perguntar: por que estamos falando sobre métodos, e não sobre listas? Esta é uma questão essencial neste momento, pois mostraremos como adicionar novos elementos a uma lista atual. Isso pode ser feito com métodos de propriedade de todas as listas, e não por funções.

# 3.4.8 Adicionando elementos a uma lista: append() e insert()
# Um novo elemento pode ser colado ao final da lista atual:
# list.append(value)

# Essa operação é realizada por um método chamado append(). Ele pega o valor do argumento e o coloca no final da lista que possui o método.

# O método insert() é um pouco mais inteligente - ele pode adicionar um novo elemento em qualquer lugar na lista, não apenas no final.
# list.insert(location, value)

# São necessários dois argumentos:

#  primeiro mostra a localização necessária do elemento a ser inserido; Nota: todos os elementos existentes que ocupam locais à direita do novo elemento (inclusive o na posição indicada) são deslocados para a direita, a fim de liberar espaço para o novo elemento;
# o segundo é o elemento a ser inserido.

# Veja como usamos os métodos append() e insert(). Preste atenção no que acontece depois de usar insert(): o primeiro primeiro elemento agora é o segundo, o segundo o terceiro e assim por diante.

# A lista original
numbers = [111, 7, 2, 1]
# Ela possui quatro elementos, numerados de 0 a 3
print(len(numbers))
# Os elementos são: 111, 7, 2, 1
print(numbers)
# Adicionando um elemento ao final da lista
numbers.append(4)
# Agora a lista possui cinco elementos, numerados de 0 a 4
print(len(numbers))
# Os elementos são: 111, 7, 2, 1, 4
print(numbers)

# Adicionando um elemento na posição 0 com o valor 222
numbers.insert (0, 222)
# Agora a lista possui seis elementos, numerados de 0 a 5
print(len(numbers))
# Os elementos são: 222, 111, 7, 2, 1, 4
print(numbers)
# Adicionando um elemento na posição 2 com o valor 333
numbers.insert(1, 333)
# Imprima o conteúdo da lista final na tela e veja o que acontece. O fragmento acima insere 333 na lista, tornando-o o segundo elemento. O antigo segundo elemento torna-se o terceiro, o terceiro o quarto e assim por diante.
print(numbers) # Resultado: [222, 333, 111, 7, 2, 1, 4]

# Você pode começar a vida de uma lista deixando-a vazia (isso é feito com um par de colchetes vazios) e, em seguida, adicionando novos elementos, conforme necessário.
my_list = [] # Criando uma lista vazia.

# Adicionando alguns elementos.
for i in range(5): # O loop for é executado cinco vezes.
    # Observe: usamos o método append() aqui.
    my_list.append (i + 1)
# Imprimindo a lista.
print (my_list)
# Resultado: [1, 2, 3, 4, 5]

# Modificamos um pouco o snippet:

my_list = []  # Criando uma lista vazia.

for i in range(5): # O loop for é executado cinco vezes.
    my_list.insert(0, i + 1) # Observe: usamos o método insert() aqui. A lista é preenchida de trás para frente pois cada valor será inserido na primeira posição.
# Imprimindo a lista.
print(my_list)

# 3.4.9 Utilização de listas
# O loop for tem uma variante especial que pode processar listas de forma muito eficaz - vamos dar uma olhada nisso.


# Vamos supor que você deseja calcular a soma de todos os valores armazenados na lista my_list.
# a uma lista é atribuída uma sequência de cinco valores inteiros;

my_list = [10, 1, 8, 3, 5]

# Você precisa de uma variável cuja soma seja armazenada e inicialmente atribuído um valor de 0 - seu nome será total (Nota: não vamos nomear sum pois o Python usa o mesmo nome para uma de suas funções internas: sum(). Usar o mesmo nome geralmente seria considerado uma má prática.) Em seguida, adicione todos os elementos da lista usando o loop for. Dê uma olhada no snippet no editor.
total = 0

# a variável i recebe os valores 0, 1, 2, 3 e 4, e depois indexa a lista, selecionando os elementos subsequentes: o primeiro, o segundo, o terceiro, o quarto e o quinto;
for i in range(len(my_list)):
  # cada um desses elementos é adicionado pelo operador += à variável total , fornecendo o resultado final no final do loop;
  total += my_list[i]

  # observe a maneira como a função len() foi empregada - ela torna o código independente de quaisquer alterações possíveis no conteúdo da lista.
print(total)

# O segundo aspecto do loop for
# Mas o loop for pode fazer muito mais. Ele pode ocultar todas as ações conectadas à indexação da lista e disponibilizar todos os elementos da lista de maneira prática. Este fragmento modificado mostra como funciona:

my_list = [10, 1, 8, 3, 5]
total = 0
# a instrução for especifica a variável usada para navegar pela lista (i aqui) seguida pela palavra-chave in e o nome da lista que está sendo processada (my_list aqui)

for i in my_list:
  # a variável i recebe os valores de todos os elementos da lista subsequente, e o processo ocorre quantas vezes houver elementos na lista; isso significa que você usa a variável i como uma cópia dos valores dos elementos e não precisa usar índices; a função len() também não é necessária.
    total += i

print(total)

# 3.4.10 Listas em ação
# Imagine que você precisa reorganizar os elementos de uma lista, ou seja, inverter a ordem dos elementos: o primeiro e o quinto, bem como o segundo e o quarto elementos serão trocados. O terceiro permanecerá intocado.

# Pergunta: como você pode trocar os valores de duas variáveis?

variable_1 = 1
variable_2 = 2
# Se você fizer algo assim, você perderia o valor armazenado anteriormente na variável_2. Alterar a ordem das tarefas não vai ajudar. Você precisa de uma terceira variável que serve como armazenamento auxiliar.
"""
variable_2 = variable_1 # Atribuindo o valor da variável_1 à variável_2, ou seja, 1.

variable_1 = variable_2 # Atribuindo o valor da variável_2 à variável_1, ou seja, 1.
"""
# É assim que você pode fazer:
"""
auxiliary = variable_1 # Atribuindo o valor da variável_1 à variável auxiliar, ou seja, 1.

variable_1 = variable_2 # Atribuindo o valor da variável_2 à variável_1, ou seja, 2.

variable_2 = auxiliary # Atribuindo o valor da variável auxiliar à variável_2, ou seja, 1.
"""
# O Python oferece uma maneira mais conveniente de fazer a troca - dê uma olhada:
variable_1, variable_2 = variable_2, variable_1

# A variável_1 recebe o valor da variável_2, ou seja, 2. A variável_2 recebe o valor da variável_1, ou seja, 1.

# O Python faz o trabalho para você - não há necessidade de uma variável auxiliar. A troca é feita em uma única linha e dessa forma o valor não é perdido.

# Agora você pode facilmente trocar os elementos da lista para reverter a ordem:
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Parece bom com cinco elementos.
# Ainda será aceitável com uma lista contendo 100 elementos? Não, não vai.
# Você pode usar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista? Sim, você pode.

# atribuímos a variável length com o comprimento da lista atual (isso torna nosso código um pouco mais claro e mais curto)
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

# lançamos o loop for para percorrer length//2 vezes (isso funciona bem para listas com comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o meio permanece intocado)

for i in range(length // 2):  # o operador // é usado para a divisão inteira
  
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
    # trocamos o i-ésimo elemento (do início da lista) pelo elemento com um índice igual a (length - i - 1) (do fim da lista); no nosso exemplo, para i igual a 0 o (length - i - 1) dá 4; para i igual a 1, dá 3 - isso é exatamente o que precisávamos.

    # Por exemplo, quando i for 1 (o segundo elemento da lista), o (length - i - 1) será 3 (o quarto elemento da lista). Quando i for 2 (o terceiro elemento da lista), o (length - i - 1) será 2 (o terceiro elemento da lista, novamente). E assim por diante.
    
print(my_list)

# O desempacotamento de listas é uma maneira conveniente de atribuir valores a várias variáveis em uma única linha. O número de variáveis à esquerda deve corresponder ao número de elementos da lista. Cada elemento da lista é atribuído a uma variável na ordem em que aparece na lista.

# 3.4.12 RESUMO DA SEÇÃO

# 1. A lista é um tipo de dados em Python usado para armazenar vários objetos. É uma coleção ordenada e mutável de itens separados por vírgula entre colchetes, por exemplo:

my_list = [1, None, True, "eu sou um barbante", 256, 0]

# 2. As listas podem ser indexadas e atualizadas, por exemplo:

my_list = [1, None, True, 'eu sou um barbante', 256, 0]
print(my_list[3])  # outputs: eu sou um barbante
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'eu sou um barbante', 256, 0]

my_list.insert(0, "primeiro")
my_list.append("último")
print(my_list)  # outputs: ['primeiro', 1, '?', True, 'eu sou um barbante', 256, 0, 'último']

# 3. As listas podem ser aninhadas, por exemplo:

my_list = [1, 'a', ["lista", 64, [0, 1], False]]

# Você aprenderá mais sobre o aninhamento no módulo {{_globals._moduleNumber}}.7 - Por enquanto, queremos que você esteja ciente de que algo como isso também é possível.

# 4. Os elementos e as listas podem ser excluídos, por exemplo:

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # exclui toda a lista

# Novamente, você aprenderá mais sobre isso no módulo {{_globals._moduleNumber}}.6 - não se preocupe. Por enquanto, apenas tente experimentar o código acima e verifique como a mudança isso afeta a saída.

# 5. As listas podem ser iteradas usando o loop for, por exemplo:

my_list = ["branco", "roxo", "azul", "amarelo", "verde"]

for color in my_list:
    print(color)

# 6. A função len() pode ser usada para verificar o comprimento da lista, por exemplo:

my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

# 7. Uma chamada de função típica tem a seguinte aparência: result = function(arg), enquanto uma chamada de método típico se parece com isso: result = data.method(arg).
