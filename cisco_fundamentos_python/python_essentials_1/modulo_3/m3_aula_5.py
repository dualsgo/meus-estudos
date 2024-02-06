# 3.5 Seção 5 - Classificação de listas simples: o algoritmo de classificação bubblesort

# 3.5.1 A ordenção em bolhas

# Agora que você pode efetivamente manipular os elementos das listas, é hora de aprender a classificá-las. Muitos algoritmos de classificação foram inventados até agora, que diferem muito na velocidade e na complexidade. Vamos mostrar um algoritmo muito simples, fácil de entender, mas infelizmente não muito eficiente. É usado muito raramente, e certamente não para listas grandes e extensas.

# Digamos que uma lista pode ser classificada de duas maneiras:

# crescente (ou mais precisamente - não decrescente) - se, em cada par de elementos adjacentes, o primeiro elemento não for maior que o último;
# decrescente (ou mais precisamente - não crescente) - se, em cada par de elementos adjacentes, o primeiro elemento não for menor que o último.

# Nas seções a seguir, classificaremos a lista em ordem crescente, para que os números sejam ordenados do menor para o maior. Aqui está a lista:

#  8, 10, 6, 2, 4.
# Vamos tentar usar a seguinte abordagem: vamos pegar o primeiro e o segundo elementos e compará-los; se determinarmos que eles estão na ordem errada (ou seja, o primeiro é maior que o segundo), vamos trocá-los; se o pedido for válido, não faremos nada. Uma rápida olhada em nossa lista confirma a última; os elementos 01 e 02 estão na ordem correta, como em 8<10.
# 8, 10, 6, 2, 4. 
# Agora, observe o segundo e o terceiro elementos. Eles estão nas posições erradas. Temos que trocá-los:
# 8, 6, 10, 2, 4.
# Vamos mais além e olhamos para o terceiro e o quarto elementos. Novamente, isso não é o que deveria ser. Temos que trocá-los:
# 8, 6, 2, 10, 4.
# Agora vamos verificar o quarto e o quinto elementos. Sim, eles também estão nas posições erradas. Outra troca ocorre:
# 8, 6, 2, 4, 10.
# A primeira passagem pela lista já está concluída. Ainda estamos longe de terminar nosso trabalho, mas algo curioso aconteceu enquanto isso. O maior elemento, 10, já foi ao fim da lista. Observe que este é o local desejado. Todos os elementos restantes formam uma confusão pitoresca, mas este já está em vigor.

# Agora vamos começar com a segunda passagem pela lista. Analisamos o primeiro e o segundo elementos - uma troca é necessária:
# 6, 8, 2, 4, 10.
# Tempo para o segundo e terceiro elementos: temos que trocá-los também:
# 6, 2, 8, 4, 10.
# Agora, o terceiro e o quarto elementos e a segunda passagem estão concluídos, pois 8 já está em vigor:

# Começamos o próximo passe imediatamente. Observe o primeiro e o segundo elementos com cuidado; outra troca é necessária:
# 2, 6, 4, 8, 10.
# Agora 6 precisa ser implementado. Trocamos o segundo e o terceiro elementos:
# 2, 4, 6, 8, 10.

# A lista já está classificada. Não temos mais nada a fazer. Isso é exatamente o que queremos.

# Agora, vamos tentar resumir o que fizemos. Nós:

# percorremos a lista, comparando cada par de elementos adjacentes e trocando-os se necessário;
# repetimos o processo até que uma passagem completa pela lista não exija nenhuma troca.

# 3.5.2 Ordenando uma lista
# Quantos passos precisamos para classificar a lista inteira?

# Resolvemos esse problema da seguinte maneira: introduzimos outra variável ; sua tarefa é observar se alguma troca foi feita durante a passagem ou não; se não houver troca, a lista já está classificada e nada mais precisa ser feito. Criamos uma variável chamada swapped e atribuímos um valor de False a ela para indicar que não há swaps. Caso contrário, ele será atribuído como True.

my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True # A variável que monitora se houve trocas feitas na lista. Inicialmente, definido como True para entrar no loop while.

while swapped: # Enquanto uma troca for feita, continue o loop.
    swapped = False  # Não há trocas até agora. Se passarmos por todo o loop e não houver trocas, o valor permanecerá False e saberemos que a lista está classificada.
    
    for i in range(len(my_list) - 1): # Loop através da lista. len(my_list) - 1 é usado porque o último elemento não precisa ser verificado.
        if my_list[i] > my_list[i + 1]: # Se o elemento atual for maior que o próximo elemento, então:
            swapped = True # Continue o loop enquanto houver trocas.
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # Troque os dois elementos.

print(my_list)

# 3.5.3 A ordenação por bolhas - versão interativa

my_list = [] # Lista vazia
swapped = True # A variável que monitora se houve trocas feitas na lista. Inicialmente, definido como True para entrar no loop while.
num = int(input("Quantos elementos você deseja embaralhar? ")) # Usuário insere quantos elementos deseja embaralhar.

for i in range(num): # Loop através da lista. O número de iterações é igual ao número de elementos que o usuário deseja inserir.
    val = float(input("Entre com a lista de elementos:")) # Usuário insere os elementos da lista.
my_list.append(val) # Adiciona cada elemento à lista.

while swapped: # Enquanto uma troca for feita, continue o loop.
    swapped = False # Não há trocas até agora. Se passarmos por todo o loop e não houver trocas, o valor permanecerá False e saberemos que a lista está classificada.
    for i in range(len(my_list) - 1): # Loop através da lista. len(my_list) - 1 é usado porque o último elemento não precisa ser verificado.
        if my_list[i] > my_list[i + 1]: # Se o elemento atual for maior que o próximo elemento, então:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # Troque os dois elementos.

print("\nSorted:")
print(my_list)

# Esse método de classificação é chamado de ordenação por bolhas, porque os elementos "flutuam" para a superfície, como bolhas em um tanque de água. É um método muito simples, mas não muito eficiente. A complexidade do algoritmo é O(n2), o que significa que o número de operações necessárias cresce quadraticamente com o número de elementos na lista. Isso é muito ruim, especialmente quando você tem uma lista grande.

# Python, no entanto, tem seus próprios mecanismos de classificação. Ninguém precisa escrever seus próprios tipos, pois há um número suficiente de ferramentas prontas para o uso.

# Se você quiser que o Python classifique sua lista, é possível fazer o seguinte:
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# Como você pode ver, todas as listas têm um método chamado sort(), que as classifica o mais rápido possível. Você já aprendeu sobre alguns dos métodos de lista antes e em breve aprenderá mais sobre outros.

# NOTA: sort() é um método que não retorna nenhum valor. Ele apenas classifica a lista. Se você tentar atribuir o resultado a uma nova variável, a nova variável será None.

# Após usar sort() a lista original é alterada. Se você não quiser alterar a lista original, você pode usar a função sorted() que retorna uma lista classificada e não altera a original.

# Com sort() - a lista original é alterada.
lista = [8, 10, 6, 2, 4] # Lista original.
lista.sort() # A lista original é alterada.
print(lista) # [2, 4, 6, 8, 10]
lista2 = lista.sort() # sort() não retorna nenhum valor. Esse é um bom exemplo de sintaxe correta, mas semantica incorreta. Não será mostrado um erro, mas a variável lista2 será None, oque pode não ser o que você queria.
print(lista2) # None

# Com sorted() - uma nova lista é criada.
lista = [8, 10, 6, 2, 4] # Lista original.
lista2 = sorted(lista) # Uma nova lista é criada.
print(lista) # [8, 10, 6, 2, 4]
print(lista2) # [2, 4, 6, 8, 10]

# Podemos gerar uma lista na ordem decrescente usando o parâmetro reverse=True no método sort() ou na função sorted().

# Porém também existe um método chamado reverse() que inverte a ordem dos elementos da lista. Esse método não retorna nenhum valor, ele apenas inverte a lista, assim como o método sort().


# 3.5.4 RESUMO DA SEÇÃO

# 1. Você pode usar o método sort() para classificar elementos de uma lista, por exemplo:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]

# 2. Há também um método de lista chamado reverse(), que você pode usar para reverter a lista, por exemplo:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]



