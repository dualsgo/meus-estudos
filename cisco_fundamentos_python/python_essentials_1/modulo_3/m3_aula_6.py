# 3.6 Seção 6 - Operações em listas

# 3.6.1 A vida interior das listas

list_1 = [1]  # Cria a lista chamada list_1 com um elemento [1]
list_2 = list_1  # Atribui a lista_1 a lista_2 - [1]
list_1[0] = 2  # Altera o único elemento de list_1 para 2
print(list_2)  # Imprime a lista_2 - [2]
# A parte surpreendente é que o programa produzirá: [2], não [1], que parece ser a solução óbvia já que a lista_2 foi criada antes da alteração da lista_1.

# A explicação é a seguinte: As listas (e muitas outras entidades Python complexas) são armazenadas de maneiras diferentes das variáveis comuns (escalares).

# o nome de uma variável comum é o nome de seu conteúdo, ou seja, o valor armazenado na memória do computador.
# o nome de uma lista é o nome de um local de memória onde a lista é armazenada.

# Sendo assim, em vez de ocupar o espaço de memória com uma cópia da lista, o Python simplesmente copia o nome da lista, o que significa que ambas as variáveis (list_1 e list_2) apontam para o mesmo local de memória.

# A atribuição: list_2 = list_1 copia o nome da matriz, não seu conteúdo. Na verdade, os dois nomes (list_1 e list_2) identificam o mesmo local na memória do computador. Modificar um deles afeta o outro e vice-versa.

# 3.6.2 Os poderes do fatiamento
# Felizmente, a solução está ao seu alcance - é chamada de fatia.

# Uma fatia é um elemento da sintaxe do Python que permite fazer uma cópia totalmente nova de uma lista ou de partes de uma lista.
# Na verdade, ele copia o conteúdo da lista, não o nome da lista.

list_1 = [1] # Como antes, cria uma lista chamada list_1 com um elemento [1];
list_2 = list_1[:] # Agora com o fatiamento, cria uma cópia completa da lista_1 e atribui a lista_2 - [1];
list_1[0] = 2 # Sem alterar a lista_2, altera o único elemento de list_1 para 2;
print(list_2) # Ao imprimir a lista_2, o resultado é [1], já que a lista_2 não foi alterada.

# Esta parte discreta do código descrito como [:] é capaz de produzir uma nova lista.
# A sintaxe é a seguinte: my_list[start:end]
# start é o índice do primeiro elemento incluído na fatia;
# end é o índice do primeiro elemento não incluído na fatia.

# Se especificarmos o fim, mas não o início, a fatia começará no início da lista.
# Se especificarmos o início, mas não o fim, a fatia terminará no final da lista.
# Sendo assim, a fatia [:] cria uma cópia completa da lista. (Inicio ao fim)

# Lembrando que o fim é o índice do primeiro elemento não incluído na fatia. É como fim - 1; Se dizemos 1 até 10, o 10 não está incluído, então é 9 (Fica subentendido 10 - 1)

# 3.6.3 Fatias - índices negativos

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] # cria uma nova lista sem o primeiro e o último elemento da lista original. O primerio elemento é 10 e o último é 2.
# Se o start especificar um elemento além do descrito no end (do início da lista), a fatia estará vazia:
new_list = my_list[-1:1] # cria uma nova lista vazia já que o start é o último elemento da lista e o end é o segundo elemento da lista.

new_list = my_list[-1:1:-1] # cria uma nova lista com os elementos da lista original na ordem inversa. O start é o último elemento da lista, o end é o segundo elemento da lista e o step é -1.

# Mais sobre a instrução del
# A instrução del descrita anteriormente é capaz de excluir mais do que apenas os elementos de uma lista de uma só vez - ela também pode excluir fatias:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3] # Exclui 8 e 6 da lista.
print(my_list)  # outputs: [10, 4, 2]

# Também é possível excluir todos os elementos de uma só vez:
my_list = [10, 8, 6, 4, 2]
del my_list[:] # Exclui todos os elementos da lista. Restando uma lista vazia.
print(my_list) # outputs: []

# A remoção da fatia do código muda bastante de significado. A instrução del excluirá a lista em si, não seu conteúdo.
my_list = [10, 8, 6, 4, 2]
del my_list # Exclui a lista inteira. Não restará nada, então é como se a lista nunca tivesse sido criada.
# print(my_list) # Se tentarmos imprimir a lista recebemos oerro - NameError: name 'my_list' is not defined

# 3.6.4 Os operadores in e not in
# O Python oferece dois operadores muito eficientes, capazes de examinar a lista para verificar se um valor específico é armazenado ou não na lista.
"""
elemento in my_list # Retorna True se o elemento estiver na lista my_list
elemento not in my_list # Retorna True se o elemento não estiver na lista my_list
"""
my_list = [0, 3, 12, 8, 2]

print(5 in my_list) # False
print(5 not in my_list) # True
print(12 in my_list) # True

# 3.6.5 Listas - alguns programas simples
# Agora, queremos mostrar alguns programas simples que utilizam listas.

# O primeiro deles tenta encontrar o maior valor na lista. Veja o código no editor.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0] # Assume temporariamente que o primeiro elemento é o maior.

for i in range(1, len(my_list)): # Loop através da lista.
  # O primeiro argumento de range() é 1, porque o primeiro elemento já foi assumido como o maior. Então, não precisamos compará-lo com ele mesmo.Seguimos a partir do segundo até o último elemento, definido por len(my_list) que retorna o tamanho da lista. 
    if my_list[i] > largest: # Se o elemento atual for maior que o maior encontrado até agora:
        largest = my_list[i] # Atualiza o maior valor encontrado.
print(largest)

# Agora vamos encontrar a localização de um determinado elemento dentro de uma lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5 # O elemento que estamos procurando.
found = False # Define como False até que o elemento seja encontrado.

for i in range(len(my_list)):
    found = my_list[i] == to_find # Verifica cada elemento. Se for encontrado, found é True.
    if found: # Se found for True:
        break # Sai do loop.

if found: # Se found for True:
    print("Elemento encontrado no índice", i) # Imprime o índice onde o elemento foi encontrado.
else:
    print("ausente")

# o valor de destino é armazenado na variável to_find;
# o status atual da pesquisa é armazenado na variável found (True/False)
# quando found se torna True, o loop for é encerrado.
# O python oferece uma maneira mais simples de fazer isso: o operador in.
# Também existem métodos de lista que podem fazer isso.

# O método index() retorna o índice do primeiro elemento com um valor específico.
print(f'Encontrei no índice {my_list.index(to_find)}') # outputs: 4


# Vamos supor que você tenha escolhido os seguintes números na loteria: 3, 7, 11, 42, 34, 49.
# Os números que foram sorteados são: 5, 11, 9, 42, 3, 49.
# A pergunta é: quantos números você acertou?

acertos = 0 # Número de acertos.
drawn = [5, 11, 9, 42, 3, 49] # Números sorteados.
bets = [3, 7, 11, 42, 34, 49] # Números apostados.

for number in bets: # Loop através dos números apostados.
    if number in drawn: # Se o número apostado estiver entre os sorteados:
        acertos += 1 # Atualiza o número de acertos.

print(acertos)

# 3.6.7 RESUMO DA SEÇÃO

# 1. Se você tiver uma lista list_1, a seguinte atribuição: list_2 = list_1 não faz uma cópia da lista list_1, mas faz com que as variáveis list_1 e list_2 apontem para uma mesma lista na memória. Por exemplo:

vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one)  # outputs: ['carro', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0]  # exclui 'carro'
print(vehicles_two)  # outputs: ['bicicleta', 'motor']

# 2. Se quiser copiar uma lista ou parte da lista, você pode fazer isso dividindo:

colors = ['vermelho', 'verde', 'laranja']

copy_whole_colors = colors[:]  # copie a lista inteira
copy_part_colors = colors[0:2]  # copiar parte da lista

# 3. Você também pode usar índices negativos para executar fatias. Por exemplo:

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. Os start de end e fim são opcionais ao executar uma fatia: list[start:end], por exemplo:

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

# 5. Você pode excluir fatias usando a instrução del:

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

# 6. Você pode testar se alguns itens existem em uma lista ou não estão usando as palavras-chave in e not in, por exemplo:

my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

# EXERCICIO

list_1 = ["A", "B", "C"] # cria uma lista de três elementos
list_2 = list_1 # atribui a lista_1 a lista_2 - [A, B, C]
list_3 = list_2 # atribui a lista_2 a lista_3 - [A, B, C]

del list_1[0] # exclui o primeiro elemento da lista_1 - [B, C]
del list_2[:] # exclui todos os elementos da lista_2 - []
# Agora a lista_3 é uma lista vazia, já que ela aponta para a lista_2 que foi excluída.
print(list_3) # outputs: []