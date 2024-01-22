# 3.2 Seção 2 - Loops em Python
# Na segunda seção, você aprenderá sobre loops em Python e, especificamente, os loops while e for. Você aprenderá como criar (e evitar cair) infinitos loops, como sair de loops e pular iterações de loop específicas. Vamos lá?



# 3.2.1 Fazendo um loop no seu código com while

# Em geral, em Python, um loop pode ser representado da seguinte forma:

# enquanto há algo para fazer:
#    faça isso

# while:
#    instruction

# Observe que esse registro deixa inplicito que se nada precisa ser feito, nada será feito. Mesmo que hajam instruções dentro do loop, elas não serão executadas se não houver nada a fazer.

# Se você observar algumas semelhanças com a instrução if, tudo bem. Na verdade, a diferença sintática é apenas uma: você usa a palavra while em vez da palavra if. A diferença semática é mais importante: quando a condição é atendida, se executa suas instruções apenas uma vez; Enquanto um loop repete a execução, enquanto a condição avalia como True.
# Nota: todas as regras relacionadas à indentação também são aplicáveis aqui. Mostraremos isso em breve.

# Importante:
# se você quiser executar mais de uma instrução dentro de um loop while, você deve (como no if) recuar todas as instruções da mesma maneira;
# uma instrução ou um conjunto de instruções executadas dentro do loop while é chamado de corpo do loop;
# se a condição for False (igual a zero) quando for testada pela primeira vez, o corpo não será executado uma única vez (observe a analogia de não ter que fazer nada se não houver nada a fazer);
# o corpo deve ser capaz de alterar o valor da condição, porque se a condição for True no início, o corpo poderá ser executado continuamente até o infinito (observe que fazer algo geralmente diminui o número de coisas a fazer).

# 3.2.2 Um loop infinito
# Um loop infinito é uma sequência de instruções em um programa que se repete indefinidamente.

"""while True:
    print("Estou preso dentro de um loop.")"""
# Esse loop exibirá infinitamente "Estou preso dentro de um loop" pois não há nada que altere a condição do loop. Ela sempre será True.

#  Vamos mostrar como usar esse loop recém-aprendido para encontrar o maior número de um grande conjunto de dados inseridos.

# Armazene o maior número atual aqui.
largest_number = -999999999
# Uma maneira melhor de armazenar um número muito pequeno ou muito grande para esse contexto seria utilizar o valor float('-inf') ou float('inf'). Isso é mais legível e mais fácil de entender. Significa que o valor é infinitamente pequeno ou infinitamente grande.

# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))

# Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))

# Imprima o maior número.
print("O maior número é:", largest_number)

# 3.2.3 O loop while: mais exemplos
# Vejamos outro exemplo empregando o loop while. Siga os comentários para descobrir a ideia e a solução.

# Um programa que lê uma sequência de números e conta quantos números são pares e quantos são ímpares. O programa termina quando zero é digitado.

odd_numbers = 0
even_numbers = 0

# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))

# 0 termina a execução.
while number: # 0 é igual a False
    # Verifique se o número é ímpar.
    if number % 2: # 0 é igual a False
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))

# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)

"""Tente se lembrar de como o Python interpreta a verdade de uma condição e observe que essas duas formas são equivalentes:

while number != 0: e while number:.

A condição que verifica se um número é ímpar também pode ser codificada nessas formas equivalentes:

if number % 2 == 1: e if number % 2:."""

# Usando uma variável counter para sair do loop
# Este código destina-se a imprimir a cadeia de caracteres "dentro do loop". e o valor armazenado na variável do counter durante um determinado loop exatamente cinco vezes. Quando a condição não for atendida (a variável do counter atingiu 0), o loop é encerrado e a mensagem "Fora do loop" . assim como o valor armazenado no counter é impresso.

counter = 5 # contador
while counter != 0:  # enquanto contador for diferente de zero
    print("Dentro do laço.", counter) # imprime o contador
    counter -= 1 # diminui o contador
print("Fora do circuito.", counter) # imprime o contador quando for igual a zero

# 3.2.5 Fazendo um loop no seu código com for
# Outro tipo de loop disponível no Python vem da observação de que, às vezes, é mais importante contar as "voltas" do loop do que verificar as condições.

# Imagine que o corpo de um loop precisa ser executado exatamente uma centena de vezes. Se você quiser usar o loop while, pode ser assim:
i = 0 # contador
while i < 100: # enquanto contador for menor que 100
    i += 1 # aumenta o contador

# o for foi projetado para realizar tarefas mais complicadas - ele pode "navegar" em grandes coleções de itens de dados por item e até percorrer todos os caracteres de uma string.

for i in range(100): # para i no intervalo de 100
    pass # não faz nada. Usamos a palavra-chave pass para evitar um erro de sintaxe pois o Python exige que o corpo do loop não esteja vazio.

# Existem alguns elementos novos. Vamos falar sobre eles:

# a palavra-chave for abre o loop for; observação - não há nenhuma condição depois; você não precisa pensar nas condições, pois elas são verificadas internamente, sem qualquer intervenção;

# qualquer variável após a palavra -chave for é a variável de controle do loop; conta as voltas do loop e o faz automaticamente;

# a palavra-chave in introduz um elemento de sintaxe que descreve o intervalo de valores possíveis que estão sendo atribuídos à variável de controle;

# a função range() (essa é uma função muito especial) é responsável por gerar todos os valores desejados da variável de controle; em nosso exemplo, a função criará (podemos até dizer que alimentará o loop com) valores subsequentes do seguinte conjunto: 0, 1, 2 .. 97, 98, 99; note Nota: nesse caso, a função range() inicia seu trabalho de 0 e o conclui uma etapa (um número inteiro) antes do valor do argumento;

# observe a palavra-chave pass dentro do corpo do loop - ela não faz nada; é uma instrução vazia - nós a colocamos aqui porque a sintaxe do loop for exige pelo menos uma instrução dentro do corpo (a propósito - if, elif, else e while expressamos a mesma coisa)

for i in range(10):
    print("O valor de i é atualmente", i)
    # exibe os valores de 0 a 9

# o loop foi executado dez vezes (é o argumento da função range())
# o valor da última variável de controle é 9 (não 10, pois começa em 0, não em 1)

# A invocação da função range() pode ser equipada com dois argumentos, não apenas um:
for i in range(2, 8):
    print("O valor de i é atualmente", i)
# exibe os valores de 2 a 7

# Nesse caso, o primeiro argumento determina o (primeiro) valor inicial da variável de controle.
# O último argumento mostra o primeiro valor em que a variável de controle não será atribuída.

# Nota: a função range() aceita apenas números inteiros como argumentos e gera sequências de números inteiros. Isso significa que podemos usar variáveis como argumento, desde que contenham valores inteiros.

# 3.2.6 Mais sobre o loop for e a funçao range() com três argumentos
# A função range() também pode aceitar três argumentos - dê uma olhada no código no editor.

for i in range(2, 8, 3):
    print("O valor de i é atualmente", i)

# O terceiro argumento é um incremento - é um valor adicionado para controlar a variável a cada volta do loop (como você pode suspeitar, o valor padrão do incremento é 1).

# O prodgrama exibirá duas linhas:
# O valor de i é atualmente 2
# O valor de i é atualmente 5

# Você sabe por quê?
# O primeiro argumento passado para a função range() nos diz qual é o número inicial da sequência (portanto, 2 na saída). 
# O segundo argumento diz à função onde parar a sequência (a função gera números até o número indicado pelo segundo argumento, mas não o inclui). 
# Por fim, o terceiro argumento indica a etapa, que realmente significa a diferença entre cada número na sequência de números gerada pela função.

# 2 (número inicial) → 5 (incremento de 2 por 3 é igual a 5 - o número está dentro do intervalo de 2 a 8) → 8 (incremento de 5 por 3 é igual a 8 - o número não está dentro do intervalo de 2 a 8, porque o O parâmetro stop não é incluído na sequência de números gerada pela função.)

# Nota: se o conjunto gerado pela função range() estiver vazio, o loop não executará seu corpo.
for i in range(1, 1): # A cotagem não começa em 0, mas em 1. O valor inicial é 1 e o valor final é 1. Como o valor final não é incluído, o loop não é executado.
    print("O valor de i é atualmente", i)

# Porém, essa variante será executada uma vez:
for i in range(1):  # 0
    print("O valor de i é atualmente", i)

# Observação: o conjunto gerado pelo range() deve ser classificado em ordem crescente. Não há como forçar o range() a criar um conjunto de uma forma diferente quando a função range() aceitar exatamente dois argumentos. Isso significa que o segundo argumento do range() deve ser maior que o primeiro.

# Para resolver esse problema, você pode usar um incremento negativo. Dessa forma, o primeiro argumento será maior que o segundo.

power = 1 # potência
for expo in range(11): # expoente 0 a 10
    # A variável expo é usada como uma variável de controle para o loop e indica o valor atual do expoente.
    print("2 à potência de", expo, "é", power)
    power *= 2 # potência multiplicada por 2.power é atualizada, dobrando seu valor a cada volta do loop

# A exponenciação em si é substituída pela multiplicação por dois. Como 2 0 é igual a 1, 2 × 1 é igual a 2 1, 2 × 2 1 é igual a 2 2 e assim por diante. Qual é o maior expoente para o qual nosso programa ainda imprime o resultado? É 10, porque 2 10 é igual a 1024, mas 2 11 é igual a 2048, que é maior que 2000.

# 3.2.8 As instruções break e continue
# Até agora, tratamos o corpo do loop como uma sequência indivisível e inseparável de instruções que são executadas completamente a cada turno do loop. No entanto, como desenvolvedor, você pode se deparar com as seguintes opções:

# parece que é desnecessário continuar o loop como um todo; você deve se abster de executar o corpo do loop e ir além. Por exemplo:

# parece que você precisa iniciar a próxima curva do loop sem concluir a execução da curva atual. Por exemplo:


# O Python fornece duas instruções especiais para a implementação dessas duas tarefas. Digamos, por uma questão de precisão, que sua existência na linguagem não é necessária - um programador experiente é capaz de codificar qualquer algoritmo sem essas instruções. Essas adições, que não melhoram o poder expressivo da linguagem, mas simplificam o trabalho do desenvolvedor, às vezes são chamadas de açúcar sintático.

# Essas duas instruções são:

# break - sai do loop imediatamente e termina incondicionalmente a operação do loop; o programa começa a executar a instrução mais próxima após o corpo do loop;

# continue - se comporta como se o programa tivesse chegado ao fim do corpo; o próximo turno é iniciado e a expressão de condição é testada imediatamente.

# break - exemplo
for i in range(1, 6): # 1 a 5
    if i == 3: # se i for igual a 3
        break # sai do loop
    print("Dentro do laço.", i) # imprime o valor de i, mas não imprime o valor 3 pois o break sai do loop
print("Fora do loop.") # imprime fora do loop

# continue - exemplo

for i in range(1, 6): # 1 a 5
    if i == 3: # se i for igual a 3
        continue # pula o valor 3
    print("Dentro do laço.", i) # imprime o valor de i, mas não imprime o valor 3 pois o continue pula o valor 3. Porém, o loop continua
print("Fora do loop.") # imprime fora do loop

# 3.2.12 O loop while e o ramo else
# Ambos os loops, while e for, têm um recurso interessante (e raramente usado).
# Como você pode ter suspeitado, os loops também podem ter o ramo else, como os ifs.

""" O ramo else do loop sempre é executada uma vez, independentemente de o loop ter entrado em seu corpo ou não."""

i = 1 # contador
while i < 5: # enquanto contador for menor que 5
    print(i) # imprime o contador
    i += 1 # aumenta o contador
else:
    print("else:", i) # imprime o contador quando for igual a 5

# Obteríamos o mesmo efeito se utilizar o operador menor ou igual a (<=) em vez de menor que (<) na condição do loop. Ou até mesmo uniciando o contador com o valor 0 e incrementando antes de imprimir o valor do contador.

# 3.2.13 O loop for e o ramo else
# se os loops for se comportarem de forma um pouco diferente - dê uma olhada no snippet no editor e execute-o.
for i in range(5):  # Loop de 0 a 4
    print(i)  # Imprime o valor do contador durante cada iteração
else:  # Esta parte é executada quando o loop termina normalmente (quando i atinge 4)
    print("else:", i)  # Imprime o valor final de i quando o loop termina que é 4

# O loop for é projetado para iterar sobre uma sequência de valores, neste caso, a função range(5), que gera uma sequência de números de 0 a 4.
# Durante cada iteração do loop, o valor atual de i é impresso.
# Após a conclusão bem-sucedida do loop, a cláusula else é executada. Isso pode parecer um pouco contra intuitivo, pois geralmente associamos o "else" com condicionais (if-else), mas no caso dos loops for e while em Python, o bloco else é executado quando o loop é concluído normalmente, sem ser interrompido por uma instrução break.
# Neste exemplo, a cláusula else imprime o valor final de i quando o loop termina normalmente.
# Se o loop fosse interrompido por uma instrução break, o bloco else não seria executado. Portanto, a presença do bloco else aqui indica que o loop foi concluído sem ser interrompido por uma instrução break.

i = 111  # Atribuímos um valor à variável i antes do loop
for i in range(2, 1):  # O range(2, 1) não gera nenhum valor, pois o valor inicial é maior que o valor final
    print(i)  # O corpo do loop não será executado
else:
    print("else:", i)  # O bloco else será executado, imprimindo "else:" seguido do valor atual de i


# O corpo do loop não será executado aqui. Nota: atribuímos a variável i antes do loop.
# Quando o corpo do loop não é executado, a variável de controle retém o valor que tinha antes do loop.
# Nota: se a variável de controle não existir antes do início do loop, ela não existirá quando a execução atingir a filial do resto else.

# 3.2.16 RESUMO DA SEÇÃO

# 1. Existem dois tipos de loops no Python: while e for:

# o loop while executa uma declaração ou um conjunto de declarações desde que uma condição booleana especificada seja verdadeira, por exemplo:

# Exemplo 1
"""while True:
    print("Preso em um loop infinito.")"""

# Exemplo 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# o loop for executa um conjunto de instruções muitas vezes; é usado para iterar em uma sequência (por exemplo, uma lista, um dicionário, uma tupla ou um conjunto - você aprenderá sobre eles em breve) ou outros objetos iteráveis (por exemplo, sequências de caracteres). Você pode usar o loop for para fazer iterações em uma sequência de números usando a função range integrada. Veja os exemplos abaixo:

# Exemplo 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Exemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# 2. Você pode usar as instruções break e continue para alterar o fluxo de um loop:

# Você usa break para sair de um loop, por exemplo:

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# Você usa continue para ignorar a iteração atual e continuar com a próxima iteração, por exemplo:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# 3. Os loops while e for também podem ter uma cláusula else em Python. A cláusula else é executada depois que o loop termina sua execução, desde que não tenha sido finalizada por break, por exemplo:

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# 4. A função range() gera uma sequência de números. Ele aceita números inteiros e retorna objetos de intervalo. A sintaxe de range() tem a seguinte aparência: range(start, stop, step), em que:

# start é um parâmetro opcional que especifica o número inicial da sequência (0 por padrão)
# stop é um parâmetro opcional que especifica o fim da sequência gerada (não está incluída),
# e step é um parâmetro opcional que especifica a diferença entre os números na sequência (1 por padrão).
# Exemplo de código:

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2


# Qual a saída a seguir:
n = range(4) # 0, 1, 2, 3
for num in n:   # 0, 1, 2, 3
    print(num - 1) # -1, 0, 1, 2
else:
    print(num) # 3 (último valor de num)