# 2.6.1 A função input()

# A função input() é capaz de ler os dados inseridos pelo usuário e retornar os mesmos dados para o programa em execução.

# Dê uma olhada no nosso exemplo:

# O programa solicita que o usuário insira alguns dados do console (provavelmente usando um teclado, embora também seja possível inserir dados usando voz ou imagem);
print("Conta-me qualquer coisa...")

# a função input() é invocada sem argumentos (essa é a maneira mais simples de usar a função); a função mudará o console para o modo de entrada; você verá um cursor piscando e poderá inserir algumas teclas, finalizando pressionando a tecla Enter; todos os dados inseridos serão enviados ao seu programa através do resultado da função; nota: você precisa atribuir o resultado a uma variável; isso é crucial - perder esta etapa fará com que os dados inseridos sejam perdidos;
anything = input()

# em seguida, usamos a função print() para exibir os dados que obtemos, com algumas observações adicionais.
print("Hum...", anything, "... Realmente?")

# 2.6.2 A função input() com um argumento

# a função input() é invocada com um argumento ‒ é uma string contendo uma mensagem; a mensagem será exibida no console antes que o usuário tenha a oportunidade de digitar qualquer coisa;
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

# 2.6.3 O resultado da função input()
# Já dissemos isso, mas deve ser afirmado de forma inequívoca mais uma vez: o resultado da função input() é uma string. Uma string contendo todos os caracteres que o usuário insere no teclado. Não é um inteiro ou um float.

# Isso significa que você não deve usá-lo como argumento de nenhuma operação aritmética, por exemplo, você não pode usar esses dados para elevá-los ao quadrado, dividi-los por qualquer coisa ou dividir qualquer coisa por eles.

anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

# A última linha da frase explica tudo - você tentou aplicar o operador ** a 'str' (string) acompanhado de 'float'. Isso é proibido.
# Isso deve ser óbvio - você pode prever o valor de "ser ou não ser" elevado à potência de 2?

# 2.6.5 Conversão de tipo (tipo de conversões)
# O Python oferece duas funções simples para especificar um tipo de dados e resolver esse problema: aqui estão eles: int() e float().

# a função int() usa um argumento (por exemplo, uma string: int(string)) e tenta convertê-lo em um número inteiro; se falhar, o programa inteiro também falhará (há uma solução para essa situação, mas mostraremos isso um pouco mais tarde);
# a função float() usa um argumento (por exemplo, uma string: float(string)) e tenta convertê-la em um flutuante (o resto é o mesmo).

# Isso é muito simples e muito eficaz. Além disso, você pode chamar qualquer uma das funções passando os resultados de input() diretamente para elas. Não há necessidade de usar nenhuma variável como armazenamento intermediário.

# Dê uma olhada no exemplo: o programa solicita que o usuário insira um número inteiro e, em seguida, calcula o seu quadrado.

something = int(input("Digite um número: "))
something = something ** 2
print(something)

# 2.6.7 Operadores de string

# O sinal de + (mais), quando aplicado a duas cadeias de caracteres, torna-se um operador de concatenação:

# Ela simplesmente concatena (cola) duas sequências de caracteres em uma. Obviamente, como seu irmão aritmético, ele pode ser usado mais de uma vez em uma expressão e, nesse contexto, se comporta de acordo com a ligação do lado esquerdo.

# Em contraste com seu irmão aritmético, o operador de concatenação não é comutativo, ou seja, "ab" + "ba" não é o mesmo que "ba" + "ab".

# Não se esqueça - se você quiser que o sinal de + seja um concatenador, não um somador, certifique-se de que ambos os argumentos sejam cadeias.

# O sinal * (asterisco), quando aplicado a uma string e um número (ou um número e uma string, pois permanece comutativo nessa posição) se torna um operador de replicação:

# string * number
# number * string

# Por exemplo:

# "James" * 3 gera "JamesJamesJames"
# 3 * "an" gera "ananan"
# 5 * "2" (or "2" * 5) gera "22222" (não10!)

# 2.6.8 Conversões de tipo mais uma vez concluídas

# str() - str(number)

# Esse tipo de conversão não é uma via de mão única. Você também pode converter um número em uma string, o que é muito mais fácil e seguro - esse tipo de operação é sempre possível.


# 2.6.12 RESUMO DA SEÇÃO
# 1. A função print() envia dados para o console, enquanto a função input() obtém dados do console.
# 2. A função input() vem com um parâmetro opcional: a string de prompt. Ele permite que você escreva uma mensagem antes da entrada do usuário, por exemplo:

name = input("Digite seu nome: ")
print("Olá, " + name + ". Prazer em conhecê-lo!")

# 3. Quando a função input() é chamada, o fluxo do programa é interrompido, o símbolo de prompt fica piscando (ele solicita que o usuário tome medidas quando o console for alternado para o modo de entrada) até que o usuário tenha inserido uma entrada e/ou pressionado o Enter chave.

#   Observação
# Você pode testar a funcionalidade da função input() em seu escopo completo localmente em sua máquina. Por motivos de otimização de recursos, limitamos o tempo máximo de execução do programa no Edube a alguns segundos. Vá para Sandbox, copie e cole o snippet acima, execute o programa e não faça nada. Apenas espere alguns segundos para ver o que acontece. Seu programa deve ser interrompido automaticamente após um instante. Agora abra o IDLE e execute o mesmo programa. Você consegue distinguir?

# Dica: o recurso mencionado acima da função input() pode ser usado para solicitar que o usuário encerre um programa. Observe o código abaixo:


name = input("Digite seu nome: ")
print("Olá, " + name + ". Prazer em conhecê-lo!")

# print("\nPressione Enter para finalizar o programa.")
# input()
# print("O FIM.")

# 4. O resultado da função input() é uma string. Você pode adicionar strings umas às outras usando o operador de concatenação (+). Confira este código:

# num_1 = input("Digite o primeiro número: ") # Digite 12
# num_2 = input("Digite o segundo número: ") # Digite 21

# print(num_1 + num_2) # o programa retorna 1221

# 5. Você também pode multiplicar cadeias (* - replicação), por exemplo:

# my_input = input("Enter something: ") # Exemplo de entrada: Olá
# print(my_input * 3) # Saída esperada: OláOláOlá


# TESTE DO MÓDULO 2

# O dígrafo \n força a função print() a:
# quebrar a linha de saída

# O significado do parâmetro de palavra-chave é determinado por:
# o nome do argumento especificado junto com seu valor

# O valor vinte ponto doze vezes dez elevado à potência de oito deve ser escrito como:
# 20.12E8

# O prefixo 0o significa que o número após ele é indicado como:
# octal

# O operador **:
# eleva o número à potência especificada - Exponenciação

# O resultado da seguinte divisão: 1 / 1
# 1.0 - float (ponto flutuante) é o tipo de dados do resultado de uma divisão

# Qual das seguintes afirmações são verdadeiras? (Selecione duas respostas)
# O argumento correto do operador % não pode ser zero.
# O operador ** usa ligação do lado direito.

# A associação do lado esquerdo determina que o resultado da seguinte expressão:
# 1 // 2 * 3 = 0

# Quais dos seguintes nomes de variáveis são ilegais? (Selecione duas respostas)
# True e and

# A função print() pode gerar valores de:
# qualquer número de argumentos (incluindo zero)


# Qual é a saída do seguinte snippet?
x = 1
y = 2
z = x
x = y
y = z
print(x, y) # 2 1

# Qual é a saída do seguinte trecho se o usuário digitar duas linhas contendo 2 e 4 respectivamente?
x = input()
y = input()
print(x + y) # 24

# Qual é a saída do seguinte trecho se o usuário digitar duas linhas contendo 2 e 4 respectivamente?
x = 2
y = 4
x = x // y # 0
y = y // x # ZeroDivisionError: integer division or modulo by zero
print(y) # 2

# Qual é a saída do seguinte trecho se o usuário digitar duas linhas contendo 2 e 4 respectivamente?
x = 2
y = 4
x = x / y # 0.5
y = y / x # 8.0
print(y) # 8.0

# Qual é a saída do seguinte snippet se o usuário digitar duas linhas contendo 11 e 4 respectivamente?
x = 11 
y = 4
x = x % y # 3
x = x % y # 3
y = y % x # 1
print(y) # 1

# Qual é a saída do seguinte snippet se o usuário digitar duas linhas contendo 3 e 6 respectivamente?

x = '3'
y = 6
print(x * y) # 333333

# Qual é a saída do seguinte snippet?
z = y = x = 1
print(x, y, z, sep='*') # 1*1*1

# Qual é a saída do seguinte snippet?
y = 2 + 3 * 5.
# print(Y) # NameError: name 'Y' is not defined

# Qual é a saída do seguinte snippet?
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x) # 17.5

# Qual é a saída do seguinte trecho se o usuário digitar duas linhas contendo 2 e 4 respectivamente?
x = 2
y = 4
print(x + y) # 6
