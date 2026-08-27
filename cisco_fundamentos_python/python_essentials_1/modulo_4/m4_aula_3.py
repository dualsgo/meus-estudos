# 4.3 Seção 3 - Retornando um resultado de uma função

# 4.3.1 Efeitos e resultados: a instrução return

# Todas as funções apresentadas anteriormente têm algum tipo de efeito - elas produzem algum texto e o enviam para o console.
# Obviamente, funções - como seus irmãos matemáticos - podem ter resultados.
# Para que as funções retornem um valor (mas não apenas para essa finalidade), use a instrução return.

# Essa palavra oferece uma visão completa de seus recursos. Nota: é uma palavra-chave Python.
# A instrução return tem duas variantes diferentes - vamos considerá-las separadamente.

# return sem uma expressão
def happy_new_year(wishes = True):
  
    print("Três...")
    print("Duas...")
    print("Uma...")
    
    # a condição a seguir verifica se o argumento é True
    if not wishes: # se wishes for False
        return # a função termina aqui

    print("Feliz Ano Novo!") # se wishes for True a função continua até aqui

# Quando invocado sem nenhum argumento:
happy_new_year()

# a função produz a seguinte saída:

# Três...
# Duas...
# Uma...
# Feliz Ano Novo!

# Fornecendo False como um argumento para testar a condição if:
happy_new_year(False)

# vai modificar o comportamento da função - ela não imprimirá o texto final - sua execução terminará imediatamente após a instrução return ser executada.

# Três...
# Duas...
# Uma...

# return com uma expressão
# A segunda variante de return é estendida com uma expressão:
"""
def function():
    return expression
"""
# Há duas consequências de usá-lo:
# causa o término imediato da execução da função (nada de novo se comparado à primeira variante)
# além disso, a função avaliará o valor da expressão e o retornará (daí o nome mais uma vez) como o resultado da função.

def boring_function():
    return 123 # a função retorna o valor 123 sempre que é chamada

x = boring_function() # x recebe o valor de retorno da função boring_function() que é 123

print("A aborrecimento_função retornou seu resultado. Isso é:", x) # imprime o valor de x

# O fragmento escreve o seguinte texto no console: A boring_function retornou seu resultado. Isso é: 123.

# A instrução de return, "transporta" o valor da expressão para o local onde a função foi chamada. O resultado pode ser usado livremente aqui, por exemplo, para ser atribuído a uma variável.

# Também pode ser completamente ignorado e perdido sem deixar vestígios.
# Observe que não estamos sendo muito educados aqui - a função retorna um valor e nós o ignoramos (não o usamos de forma alguma):
def boring_function():
    print("'Modo de tédio' ON.")
    return 123 # a função retorna o valor 123 sempre que é chamada

print("Esta lição é interessante!")
boring_function() # mas não usamos seu resultado! Ao chamar a função apenas o efeito é visível devido a instrução print() dentro da função.
print("Essa aula é chata...")

# O programa produz a seguinte saída:

# Esta lição é interessante!
# 'Modo de tédio' ON.
# Essa aula é chata...

# É punível? Não mesmo. A única desvantagem é que o resultado foi irremediavelmente perdido.

# Não se esqueça:
# você sempre pode ignorar o resultado da função e ficar satisfeito com o efeito da função (se a função tiver algum)
# se uma função se destina a retornar um resultado útil, ela deve conter a segunda variante da instrução de return.

# 4.3.2 Algumas palavras sobre None
# Vamos apresentar um valor muito curioso (para ser honesto, um valor nenhum) chamado None.
# Seus dados não representam nenhum valor razoável - na verdade, não é um valor; portanto, não deve participar de nenhuma expressão.

# Por exemplo, um trecho como este:
print(None + 2)

# causará um erro de tempo de execução, descrito pela seguinte mensagem de diagnóstico:
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# Existem apenas dois tipos de circunstâncias em que None pode ser usada com segurança:

# quando você a atribui a uma variável (ou a retorna como resultado de uma função)
value = None

# quando você a compara com uma variável para diagnosticar seu estado interno.
if value is None:
    print("Desculpe, você não carrega nenhum valor")

# Não se esqueça disso: se uma função não retorna um determinado valor usando a cláusula return, pressupõe-se que ele retorne implicitamente None. Isso significa que o resultado da função pode ser ignorado sem consequências, evita erros de tempo de execução.


def strange_function(n):
  if(n % 2 == 0):
    return True
# É óbvio que a função strange_function retorna True quando seu argumento é par. 
# Vamos verificar:
print(strange_function(2)) # True

# O que ele retorna no outro caso?
print(strange_function(1)) # None

# Nossa função não tem uma cláusula return para o caso ímpar, então ela retorna implicitamente None. Pense como um else: return None.

# Não fique surpreso na próxima vez que não vir o None como resultado de uma função - pode ser o sintoma de um erro sutil dentro da função.

# 4.3.3 Efeitos e resultados: listas e funções
# Há duas perguntas adicionais que devem ser respondidas aqui.

# A primeira é: uma lista pode ser enviada para uma função como argumento?
# Claro que sim! Qualquer entidade reconhecível pelo Python pode desempenhar o papel de um argumento de função, embora tenha que ter certeza de que a função é capaz de lidar com ele.

# Então, se você passar uma lista para uma função, a função tem que lidar com isso como uma lista.

# a tarefa dessa lista é somar todos os números da lista que for passada como argumento.
def list_sum(lst):
  
  s = 0 # a variavel contador começa com 0 e vai somando os elementos da lista a cada iteração do loop for
  
  for elem in lst: # para cada elemento da lista
    s += elem # adiciona o valor do elemento atual a s

  return s # retorna o resultado quando o loop for terminado

# Agora, você pode chamar a função contendo uma lista como argumento:
print(list_sum([5, 4, 3])) # Resultado: 12
# é absolutamente correto, já que 5 + 4 + 3 = 12.

# A segunda pergunta é: uma lista pode ser um resultado de função?
# Sim, claro! Qualquer entidade reconhecível pelo Python pode ser um resultado de função. Então podemos retornar uma lista de uma função.

# A tarefa dessa função é criar uma lista contendo todos os números de 0 a n-1, sendo 0 o primeiro número e n-1 o último número da lista (n é o argumento da função).
def strange_list_fun(n):
  strange_list = [] # começa com uma lista vazia que será preenchida com os valores do loop for em seguida sera retornada

  for i in range(0, n):
    # n, que é o valor final da lista será definido pelo usuário ao chamar a função usando o valor desejado como argumento. 
    # i será o valor inicial da lista, que é 0.
    
    strange_list.insert(0, i) # insere i no início da lista, formando uma lista reversa

  return strange_list # retorna a lista preenchida quando o loop for terminado

print(strange_list_fun(5)) # o argumento é 5, o que significa que a lista terá 5 elementos. Note que diferente do último exemplo, não estamos fornecendo uma lista e sim a quantidade de elementos. O resultado é [4, 3, 2, 1, 0].


# 4.3.9 RESUMO DA SEÇÃO

# 1. Você pode usar a palavra-chave return para informar uma função para retornar algum valor. A declaração de return sai da função, por exemplo:

def multiply(a, b):
    return a * b
# A tarefa da função acima é multiplicar dois argumentos e retornar o resultado. Você pode chamar a função da seguinte maneira:
print(multiply(3, 4)) # saídas: 12 

def multiply(a, b):
    return
# Se a instrução return for executada sem nenhum valor, ela retornará None, por exemplo:
print(multiply(3, 4)) # saídas: None

# 2. O resultado de uma função pode ser facilmente atribuído a uma variável, por exemplo:

def wishes():
    return "Feliz aniversário!"

w = wishes() # Atribuímos o resultado da função wishes() a variável w
print(w) # saídas: Feliz aniversário!

# Veja a diferença de saída nos dois exemplos a seguir:

# Exemplo 1 - A função contem a instrução return...
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
# ...mas não atribuímos o resultado da função a nenhuma variável - Apenas seu efeito será visível
wishes()
# saídas: Meus desejos

# Exemplo 2  - A função contem a instrução return...
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
# ... e utilizamos uma instrução print() para imprimir o resultado da função, com isso o resultado da função será visível
print(wishes())
# saídas: Meus desejos
# Feliz aniversário!

# 3. Você pode usar uma lista como argumento de função, por exemplo:
# A função recebe uma lista como argumento e iterasobre ela , imprimindo cada elemento
def hi_everybody(my_list):
    for name in my_list:
        print("Oi,", name)

hi_everybody(["Adão", "John", "Lucy"])

# 4. Uma lista também pode ser um resultado de função, por exemplo:
# A função recebe um valorinteiro como argumento e retorna uma lista com os valores de 0 até o valor do argumento
def create_list(n):
    my_list = [] # começa com uma lista vazia que será preenchida com os valores do loop for em seguida sera retornada
    for i in range(n): # O loop itera sobre a lista de 0 até o valor do argumento para preencher a lista
        my_list.append(i)
    return my_list

print(create_list(5))













