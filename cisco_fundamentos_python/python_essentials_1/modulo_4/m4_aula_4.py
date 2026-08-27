# 4.4 Seção 4 - Escopos em Python
# Nesta parte do curso, você aprenderá sobre escopos em Python e a palavra-chave global. Ao final da seção, você será capaz de distinguir entre variáveis locais e globais e saberá como utilizar o mecanismo de namespaces em seus programas.

# 4.4.1 Funções e escopos
# Vamos começar com uma definição:
# O escopo de um nome (por exemplo, um nome de variável) é a parte de um código onde o nome é reconhecível corretamente.

# Por exemplo, o escopo do parâmetro de uma função é a própria função. O parâmetro está inacessível fora da função.

def scope_test():
	x = 123  # x é uma variável local para scope_test() - não pode ser usada fora da função
	print(x)  # Efeito


# Ao chamar a função o efeito fica visível
scope_test()  # saídas: 123


# Mas se tentarmos acessar a variável x fora da função, o Python retornará um erro
# print(x)  # NameError: name 'x' is not defined

# Mas ao contrário a história é diferente.
# Vamos começar verificando se uma variável criada fora de qualquer função é visível dentro das funções. Em outras palavras, o nome de uma variável se propaga no corpo de uma função?

def my_function():
	print("Eu conheço aquela variável?",
		  var)  # Repare que var ainda não foi definida, mas...


var = 1  # ao definir a variável fora da função, ela é visível dentro da função. Parece contra intuitivo, já que a variável foi utilizada antes de ser definida.

# Ao chamar a função o efeito fica visível - Isso é possível pois o Python não executa o corpo da função até que a função seja chamada. Então, quando a função é chamada, a variável já foi definida.

my_function()  # saídas: Eu conheço aquela variável? 1
print(var)  # saídas: 1


# Essa regra tem uma exceção muito importante. Vamos tentar encontrar.

def my_function():
	var = 2  # var foi definida dentro da função, isso a torna uma variável local
	print("Eu conheço aquela variável?", var)


var = 1  # de novo, definimos a variável com o mesmo nome fora da função e com um valor diferente

# Ao chamar a função o valor da variável local é o que é impresso, pois a variável local tem precedência sobre a variável global.
my_function()  # saídas: Eu conheço aquela variável? 2

# Se chamarmos a variável fora da função, o valor da variável global é impresso.
print(var)  # saídas: 1


# Podemos tornar a regra anterior mais precisa e adequada:

# Uma variável existente fora de uma função tem escopo dentro do corpo da função, excluindo aquelas que definem uma variável com o mesmo nome.
# Também significa que o escopo de uma variável existente fora de uma função é suportado apenas ao obter seu valor (leitura). A atribuição de um valor força a criação da própria variável da função.

# O ideal é nomear as variáveis de forma diferente para evitar confusão.

# Resumindo até aqui;
# Escopo Global:
# Se uma variável é definida fora de uma função, ela tem um escopo global. Isso significa que ela pode ser acessada de qualquer lugar no programa, incluindo dentro de funções.
# Se uma função tentar modificar o valor dessa variável usando a atribuição (=), a função criará uma variável local com o mesmo nome, não afetando a variável global fora da função.

# Escopo Local:
# Se você define uma variável dentro de uma função, ela tem um escopo local. Isso significa que ela só é acessível dentro dessa função.
# Se houver uma variável global com o mesmo nome, a função irá preferir a variável local. A função pode ler a variável global, mas se você atribuir um valor a ela, a função criará uma nova variável local.

# 4.4.2 Funções e escopos: a palavra-chave global
# Você deve ter chegado à seguinte pergunta: isso significa que uma função não é capaz de modificar uma variável definida fora dela? Isso criaria muito desconforto. Felizmente, a resposta é não.
# Há um método Python especial que pode estender o escopo de uma variável de uma forma que inclua o corpo da função (mesmo se você quiser não apenas ler os valores, mas também modificá-los).

# Tal efeito é causado por uma palavra-chave chamada global:

# Usar essa palavra-chave dentro de uma função com o nome (ou nomes separados por vírgulas) de uma variável (ou variáveis), força o Python a não criar uma nova variável dentro da função - a que pode ser acessada de fora será usada.

def my_function():
	global var  # com a palavra-chave global, definimos que a variável var é global
	var = 2  # modificando a variável global - ou seja, seu valor será modificado fora da função também
	print("Eu conheço aquela variável?", var)


# redefinimos o valor da variável, como sabemos, seu valor será o mais recente
var = 1  # portanto agora var vale 1
print(var)  # saídas: 1

# mas ao chamar a função, executamos o corpo da função, que contém uma instrução global que modifica o valor da variável
my_function()  # saídas: Eu conheço aquela variável? 2
print(var)  # saídas: 2


# Observe que a mudança de valor só ocorre após a chamada da função. Se você tentar imprimir o valor da variável antes de chamar a função, o valor será o original.

# 4.4.3 Como a função interage com seus argumentos
# Como você pode ver, a função altera o valor de seu parâmetro. A mudança afeta o argumento?

# Como sabemos, argumentos são variáveis locais, então a resposta é não. A alteração do valor do parâmetro não afeta o argumento.

def my_function(n):  # n é um parâmetro - uma nova variável local n é criada
	print("Eu obtive", n)
	n += 1  # modifica o valor de n
	print("Eu tenho", n)


var = 1  # var é um argumento
my_function(var)  # var é um argumento - seu valor é copiado para n
# saídas: Eu obtive 1
# saídas: Eu tenho 2

print(var)  # saídas: 1


# A conclusão é óbvia - alterar o valor do parâmetro não se propaga fora da função - o argumento permanece inalterado.
# Isso também significa que uma função recebe o valor do argumento, não o próprio argumento.

# Vale a pena verificar como ele funciona com listas (você se lembra das particularidades de atribuir fatias de lista versus atribuir listas como um todo?).

def my_function(my_list_1):  # my_list_1 é um parâmetro

	print("Print  #1:", my_list_1)  # saídas: Print  #1: [0, 1]
	print("Print  #2:", my_list_2)  # saídas: Print  #2: [2, 3]

	my_list_1 = [0,
				 1]  # my_list_1 é na verdade uma variável local, não uma fatia de my_list_2 portanto, não afeta my_list_2

	print("Print  #3:", my_list_1)  # saídas: Print  #3: [0, 1]
	print("Print  #4:", my_list_2)  # saídas: Print  #4: [2, 3]


my_list_2 = [2, 3]  # my_list_2 é um argumento

my_function(
	my_list_2)  # my_list_2 é um argumento - seu valor é copiado para my_list_1

print("Print  #5:", my_list_2)  # saídas: Print  #5: [2, 3]


# O que você pode ver é que a atribuição de uma lista a uma variável não cria uma nova lista. A lista é apenas referenciada por uma nova variável. Isso significa que a lista é compartilhada entre as variáveis.

def my_function(my_list_1):  # my_list_1 é um parâmetro

	print("Print  #1:", my_list_1)  # saídas: Print  #1: [2, 3]
	print("Print  #2:", my_list_2)  # saídas: Print  #2: [2, 3]
	del my_list_1[
		0]  # Exclui o primeiro elemento da lista - o efeito é visível fora da função
	print("Print  #3:", my_list_1)  # saídas: Print  #3: [3]
	print("Print  #4:", my_list_2)  # saídas: Print  #4: [3]


my_list_2 = [2, 3]  # my_list_2 é um argumento4

my_function(
	my_list_2)  # my_list_2 é um argumento - seu valor é copiado para my_list_1

print("Print  #5:", my_list_2)  # saídas: Print  #5: [3]

# se o argumento for uma lista, a alteração do valor do parâmetro correspondente não afeta a lista (lembre-se: as variáveis que contêm listas são armazenadas de forma diferente de escalares)
# mas se você alterar uma lista identificada pelo parâmetro (Nota: a lista, não o parâmetro!), a lista refletirá a alteração.

# 4.4.4 RESUMO DA SEÇÃO

# 1. Uma variável que existe fora de uma função tem escopo dentro do corpo da função (exemplo 1), a menos que a função defina uma variável com o mesmo nome (exemplo 2 e exemplo 3), por exemplo:

# Exemplo 1:
var = 2


def mult_by_var(x):
	return x * var


print(mult_by_var(7))  # saídas: 14


# Exemplo 2:
def mult(x):
	var = 5
	return x * var


print(mult(7))  # saídas: 35


# Exemplo 3:
def mult(x):
	var = 7
	return x * var


var = 3
print(mult(7))  # saídas: 49


# 2. Uma variável que existe dentro de uma função tem escopo dentro do corpo da função (exemplo 4), por exemplo:

# Exemplo 4:
def adding(x):
	var = 7
	return x + var


print(adding(4))  # saídas: 11
# print(var)  # NameError (var is not defined outside the function)

# 3. Você pode usar a palavra-chave global seguida por um nome de variável para tornar o escopo da variável global, por exemplo:

var = 2
print(var)  # saídas: 2


def return_var():
	global var
	var = 5
	return var


print(return_var())  # saídas: 5
print(var)  # saídas: 5