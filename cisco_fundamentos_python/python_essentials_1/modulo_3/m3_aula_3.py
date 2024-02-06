# 3.3.1 Lógica do computador

# Conjunção (AND)
# Se tivermos tempo livre, e se o tempo estiver bom, vamos dar uma volta.

# Usamos a conjunção and, o que significa que sair para passear depende do cumprimento simultâneo dessas duas condições.

# Disjunção (OR)
# Se você for ao supermercado ou ao açougue, compre carne.

# A aparência da palavra or significa que a compra depende de pelo menos uma dessas condições.

# É claro que o Python deve ter operadores para criar conjunções e disjunções. Sem eles, o poder expressivo da linguagem seria substancialmente enfraquecido. Eles são chamados de operadores lógicos.

# O operador and
# Um operador de conjunção lógica em Python é a palavra and. É um operador binário com uma prioridade menor do que a expressa pelos operadores de comparação. Ela nos permite codificar condições complexas sem o uso de parênteses como este:

# O resultado fornecido pelo operador and pode ser determinado com base na tabela verdade.
"""
False	and False	| False
False	and True	| False
True	and False	| False
True	and True	| True
"""

# O operador or
# Um operador de disjunção é a palavra or. É um operador binário com uma prioridade menor do que and (assim como + em comparação com *).
"""
False	or False	| False
False	or True	| True
True	or False	| True
True	or True	| True
"""

# O operador not
# Além disso, há outro operador que pode ser aplicado à construção de condições. É um operador unário que executa uma negação lógica. Sua operação é simples: transforma verdade em falsidade e falsidade em verdade.
# Esse operador é escrito como a palavra not, e sua prioridade é muito alta: o mesmo que os + e - unários. Sua tabela de verdade é simples:
"""
not False	| True
not True	| False
"""

# 3.3.2 Expressões lógicas
# Vamos criar uma variável chamada var e atribuir 1 a ela. As condições a seguir são equivalentes aos pares:
var = 1
# Exemplo 1:
print(var > 0)  # True
print(not (var <= 0)) # True - var é menor ou igual a 0? False
# Então, not False é True.

# Exemplo 2:
print(var != 0)  # True
print(not (var == 0))  # True - var é igual a 0? False



# Você pode estar familiarizado com as leis de De Morgan. Eles dizem que:

# A negação de uma conjunção é a disjunção das negações.
# not (A and B) = (not A) or (not B)

# A negação de uma disjunção é a conjunção das negações.
# not (A or B) = (not A) and (not B)

# 3.3.3 Valores lógicos vs. bits únicos
# Os operadores lógicos recebem seus argumentos como um todo, independentemente de quantos bits eles contenham. Os operadores estão cientes apenas do valor: zero (quando todos os bits são redefinidos) significa False; diferente de zero (quando pelo menos um bit for definido) significa True.
# O resultado de suas operações é um desses valores: False ou True. Isso significa que esse fragmento atribuirá o valor True à variável j se i não for zero; caso contrário, será False.

i = 1
j = not not i
print(j)  # True

# 3.3.4 Operadores bit a bit
# No entanto, existem quatro operadores que permitem manipular bits únicos de dados. Eles são chamados de operadores bit a bit.

# Eles abrangem todas as operações que mencionamos anteriormente no contexto lógico e um operador adicional. Este é o operador xor (as em exclusivo ou) e é indicado como ^ (circunflexo).

# Aqui estão todos eles:

# & (e comercial) - conjunção bit a bit;
# | (barra) - disjunção bit a bit;
# ~ (til) - negação bit a bit;
# ^ (circunflexo) ‒ bit a bit exclusivo ou (xor).

# Operações bit a bit (& , | , e ^ ) - conjunção bit a bit, disjunção bit a bit e bit a bit exclusivo ou (xor)

"""
A	B   	 	A & B   	 	 A | B   	 	A ^ B
0	0	    	  0   	   	  0          0
0	1	    	  0	   	   	  1	   	     1
1	0	    	  0	      	 	1	   	   	 1
1	1	    	  1	      	 	1	   	   	 0"""

# Operações bit a bit (~ ) - negação bit a bit
"""
A   ~  
0	  1
1	  0"""

# & requer exatamente dois 1 s para fornecer 1 como resultado;
# | requer pelo menos um 1 para fornecer 1 como resultado;
# ^ requer exatamente um 1 para fornecer 1 como resultado.

# Vamos acrescentar uma observação importante: os argumentos desses operadores devem ser números inteiros; não devemos usar carros alegóricos aqui.
# A diferença na operação dos operadores lógicos e de bit é importante: os operadores lógicos não penetram no nível de bit de seu argumento. Eles estão interessados apenas no valor inteiro final.

# Os operadores de bit a bit são mais rigorosos: eles lidam com cada bit separadamente. Se assumirmos que a variável inteira ocupa 64 bits (o que é comum em sistemas de computadores modernos), você pode imaginar a operação bit a bit como uma avaliação de 64 vezes do operador lógico para cada par de bits dos argumentos. Essa analogia é obviamente imperfeita, pois no mundo real todas essas 64 operações são realizadas ao mesmo tempo (simultaneamente).

# Operações lógicas x operações de bit
# Vamos agora mostrar um exemplo da diferença de operação entre as operações lógica e de bit. Vamos supor que as seguintes atribuições foram realizadas:

i = 15
j = 22

# Se assumirmos que os números inteiros são armazenados com 32 bits, a imagem bit a bit das duas variáveis será a seguinte:

# i = 00000000 00000000 00000000 00001111
# j = 00000000 00000000 00000000 00010110

# A tarefa é dada:
log = i and j # True

# Agora, a operação bit a bit - aqui está:
bit = i & j

# O operador & operará com cada par de bits correspondentes separadamente, produzindo os valores dos bits relevantes do resultado. Portanto, o resultado será o seguinte:

# i
# 00000000000000000000000000001111
# j
# 00000000000000000000000000010110
# bit = i & j
# 00000000000000000000000000000110
#
# 00000000000000000000000000000110
# & requer exatamente dois 1 s para fornecer 1 como resultado;

# Esses bits correspondem ao valor inteiro de seis.

# Vejamos os operadores de negação agora. Primeiro a lógica:
logneg = not i # A variável logneg será definida como False - nada mais precisa ser feito.

# A negação bit a bit é assim:
bitneg = ~i # A variável bitneg será definida como -16.
# Pode ser um pouco surpreendente: o valor da variável bitneg é -16. Isso pode parecer estranho, mas não é. O valor inteiro -16 é representado em binário como 11111111111111111111111111110000. A negação bit a bit de 00000000000000000000000000001111 é 11111111111111111111111111110000.

# Cada um desses operadores de dois argumentos pode ser usado de forma abreviada. Estes são os exemplos de notações equivalentes:


"""
x = x & y
x &= y

x = x | y	
x |= y

x = x ^ y	
x ^= y"""

# 3.3.5 Como lidamos com bits únicos?
# Vamos mostrar para que você pode usar operadores bit a bit. Imagine que você é um desenvolvedor obrigado a escrever uma parte importante de um sistema operacional. Você foi informado de que pode usar uma variável atribuída da seguinte maneira:

flag_register = 0x1234

# A variável armazena as informações sobre vários aspectos da operação do sistema. Cada bit da variável armazena um valor sim/não. Você também foi informado de que apenas um desses bits é seu - o terceiro (lembre-se de que os bits são numerados de zero, e o número de bits zero é o mais baixo, enquanto o mais alto é o número 31). Os bits restantes não têm permissão para alterar, porque pretendem armazenar outros dados. Aqui está o seu bit marcado com a letra x:

# flag_register = 0000000000000000000000000000x000

# Você pode se deparar com as seguintes tarefas:

# 1. Verifique o estado do seu bit - você quer descobrir o valor do seu bit; comparar a variável inteira com zero não fará nada, porque os bits restantes podem ter valores completamente imprevisíveis, mas você pode usar a seguinte propriedade de conjunção:
"""
x & 1 = x
x & 0 = 0"""

# Se você aplicar a operação & à variável flag_register junto com a seguinte imagem de bit: 00000000000000000000000000001000

# (observe o 1 na posição do bit), como resultado, você obtém uma das seguintes cadeias de bits:

# 00000000000000000000000000001000 se o bit foi definido como 1
# 00000000000000000000000000000000 se o bit foi redefinido para 0

# Essa sequência de zeros e uns, cuja tarefa é capturar o valor ou alterar os bits selecionados, é chamada de máscara de bit.

# Vamos construir uma máscara de bit para detectar o estado do bit. Deve apontar para o terceiro bit. Esse bit tem o peso de 23 = 8. Uma máscara adequada pode ser criada pela seguinte declaração:
the_mask = 8

# Você também pode fazer uma sequência de instruções, dependendo do estado do seu bit. Aqui está:


if flag_register & the_mask:
    print("Bit 3 está ligado")
else:
    print("Bit 3 está desligado")

# 2. Redefinir seu bit - você atribui um zero ao bit enquanto todos os outros bits devem permanecer inalterados; vamos usar a mesma propriedade da conjunção como antes, mas vamos usar uma máscara ligeiramente diferente, exatamente como abaixo:

# 11111111111111111111111111110111

# Observe que a máscara foi criada como resultado da negação de todos os bits da variável the_mask. Redefinir o bit é simples, e fica assim (escolha o que você mais gosta):

flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# 3. Defina seu bit - você atribui um 1 ao bit, enquanto todos os bits restantes devem permanecer inalterados; use a seguinte propriedade de disjunção:

"""
x | 1 = 1
x | 0 = x
"""
# Você está pronto para definir o seu bit com uma das seguintes instruções:

flag_register = flag_register | the_mask
flag_register |= the_mask

# 4. Negue sua parte - você substitui um 1 por um 0 e um 0 por um 1. Você pode usar uma propriedade interessante do operador xor:

"""x ^ 1 = ~x
x ^ 0 = x
"""
# e negue sua parte com as seguintes instruções:

flag_register = flag_register ^ the_mask
flag_register ^= the_mask

# 3.3.6 Deslocamento binário para a esquerda e deslocamento binário para a direita

# O Python oferece ainda outra operação relacionada a bits únicos: deslocamento. Isso é aplicado apenas a valores inteiros, e você não deve usar carros alegóricos como argumentos para ele.

# Você já aplica essa operação com muita frequência e inconsciência. Como você multiplica um número por dez? Dê uma olhada:

# 12345 * 10 = 123450

# Como você pode ver, multiplicar por dez é, na verdade, um deslocamento de todos os dígitos para a esquerda e preencher a lacuna resultante com zero.

# Divisão por dez? Dê uma olhada:
# 12340 / 10 = 1234

# Dividir por dez nada mais é do que mudar os dígitos para a direita.

# O mesmo tipo de operação é realizado pelo computador, mas com uma diferença: como dois é a base para números binários (não 10), deslocar um valor um bit para a esquerda corresponde à multiplicação por dois; respectivamente, mudar um bit para a direita é como dividir por dois (observe que o bit mais à direita está perdido).

# Os operadores de deslocamento em Python são um par de dígrafos: << e >>, sugerindo claramente em qual direção o deslocamento vai agir.

"""valor << bits
valor >> bits"""

# O argumento à esquerda desses operadores é um valor inteiro cujos bits são deslocados. O argumento certo determina o tamanho do turno. Ela mostra que essa operação certamente não é comutativa.

var = 17
# 00000000000000000000000000010001 - 17
var_right = var >> 1
# 00000000000000000000000000001000 - 8
var_left = var << 2
# 00000000000000000000000001000100 - 68
print(var, var_left, var_right)
# 17 68 8

# 17 >> 1 → 17 // 2 (17 piso dividido por 2 à potência de 1) → 8 (deslocar para a direita por um bit é igual a divisão inteira por dois)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 à potência de 2) → 68 (deslocar para a esquerda por dois bits é igual a multiplicação do número inteiro por quatro)

# 3.3.7 RESUMO DA SEÇÃO
# 1. O Python é compatível com os seguintes operadores lógicos:

# and → se ambos os operandos forem verdadeiros, a condição é verdadeira, por exemplo, (True and True) é True,
# or → se qualquer um dos operandos for verdadeiro, a condição é verdadeira, por exemplo, (True or False) é True,
# not → retorna falso se o resultado for verdadeiro e retorna verdadeiro se o resultado for falso, por exemplo, not True for False.
# 2. Você pode usar operadores bit a bit para manipular bits únicos de dados. Os seguintes dados de amostra:

# x = 15, que é 0000 1111 em binário,
# y = 16, que é 0001 0000 em binário.
# Será usado para ilustrar o significado dos operadores de bit a bit em Python. Analise os exemplos abaixo:

# & faz um bit a bit AND, por exemplo, x & y = 0 , que é 0000 0000 em binário,
# | faz um bit a bit OR, por exemplo, x | y = 31, que é 0001 1111 em binário,
# ˜ faz um bit a bit NOT, por exemplo, ˜ x = 240 *, que é 1111 0000 em binário,
# ^ faz um bit a bit xor, por exemplo, x ^ y = 31, que é 0001 1111 em binário,
# >> faz um deslocamento à direita bit a bit, por exemplo, y >> 1 = 8, que é 0000 1000 em binário,
# << faz um turno à esquerda bit a bit, por exemplo, y << 3 = 128, que é 1000 0000 em binário,
# * -16 (decimal do complemento de 2 assinado) - leia mais sobre a operação de complemento de Dois.


x = 581  # 1001000101
y = 644  # 1010000100

# Dado o código acima, qual será o valor de cada uma das variáveis a seguir?
a = x & y
# 1001000101 & 1010000100 = 1000000100 (581 & 644 = 516)
b = x | y
# 1001000101 | 1010000100 = 1011000101 (581 | 644 = 709)
c = ~x  # pegadinha!
# ~1001000101 = 0110111010 (-582)
d = x ^ 5
# 1001000101 ^ 0000000101 = 1001000000 (581 ^ 5 = 576)
e = x >> 2
# 1001000101 >> 2 = 0010010001 (581 >> 2 = 145)
f = x << 2
# 1001000101 << 2 = 0100010100 (581 << 2 = 2324)

print(a, b, c, d, e, f)
# 516 709 -582 576 145 2324

# A expressão c = ~x:

# Para entender como determinar o bit de sinal e interpretar o valor em complemento de dois, é necessário seguir alguns passos. Vamos analisar o exemplo com x = 581, representado em binário como 1001000101.

# Representação Binária de x:
x = 581  # 1001000101

# A representação binária de x consiste em 10 bits.

# Aplicação da Negação Bit a Bit (~x): Invertemos cada bit de x.
# ~x = 1110111010
# Agora, todos os 1s na representação binária original tornaram-se 0s, e todos os 0s tornaram-se 1s.

# Interpretação do Bit de Sinal:

# O bit mais à esquerda (o bit mais significativo) na representação binária de ~x indica o sinal do número.
# Se esse bit for 0, o número é positivo.
# Se esse bit for 1, o número é negativo.
# No exemplo, o bit mais à esquerda em ~x é 1, indicando que o número resultante é negativo.

# Cálculo do Valor Absoluto (Módulo):

# Ignorando o bit de sinal, a parte restante da representação binária (110111010) é tratada como o valor absoluto do número em binário.

#Interpretação do Valor em Complemento de Dois:

# O valor absoluto (110111010) é interpretado como um número em binário.
# Em seguida, é aplicada a regra de complemento de dois para converter o valor para decimal.
# No caso de um número negativo, o valor é o negativo do valor absoluto.
# Portanto, o resultado é interpretado como -110111010 em decimal.
# Então, a expressão c = ~x resultará em c sendo atribuído a -110111010. Certifique-se de ajustar o número para a base decimal para obter o valor correto. Se você precisar de mais detalhes sobre a interpretação de números em complemento de dois, posso fornecer mais informações.