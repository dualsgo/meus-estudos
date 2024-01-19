# 2.3 Seção 3 - Operadores - ferramentas de manipulação de dados

# 2.3.2 Operadores básicos

# Um operador é um símbolo da linguagem de programação, capaz de operar com os valores. Por exemplo, assim como na aritmética, o sinal de + (mais) é o operador que consegue adicionar dois números, dando o resultado da adição.

# Vamos começar com os operadores que estão associados às operações aritméticas mais amplamente reconhecidas:

# + (mais) - adiciona dois valores
# - (menos) - subtrai um valor de outro
# * (asterisco) - multiplica dois valores
# ** (dois asteriscos) - eleva um valor ao poder de outr
# / (barra) - divide um valor por outro
# // (barra dupla) - divide um valor por outro (arredondando o resultado para baixo)
# % (porcentagem) - calcula o resto da divisão de um valor por outro

# Exponenciação
# Os exemplos mostram uma característica muito importante de praticamente todos os operadores numéricos do Python.

# quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
print(2 ** 3)  # 8

# Quando pelo menos um argumento ** é um float, o resultado também é um float.
print(2 ** 3.)  # 8.0
print(2. ** 3)  # 8.0
print(2. ** 3.)  # 8.0

# Multiplicação
# Um sinal de * (asterisco) é um operador de multiplicação.

print(2 * 3)  # 6
print(2 * 3.)  # 6.0
print(2. * 3)  # 6.0
print(2. * 3.)  # 6.0

# Divisão
# Um sinal / (barra) é um operador de divisão.
# O valor na frente da barra é um dividendo, o valor atrás da barra, um divisor.
print(6 / 3)  # 2.0
print(6 / 3.)  # 2.0
print(6. / 3)  # 2.0
print(6. / 3.)  # 2.0

# O resultado produzido pelo operador de divisão é sempre um float, independentemente de parecer ou não ser um flutuante à primeira vista: 1 / 2, ou se parece com um inteiro puro: 2 / 1.
# Isso é um problema? Sim, o limite continua igual. Às vezes acontece que você realmente precisa de uma divisão que forneça um valor inteiro, não um valor flutuante.

# Felizmente, o Python pode ajudá-lo com isso.

# Divisão de número inteiro (divisão arredondada)
# Um sinal // (barra dupla) é um operador de divisão inteira. Difere do padrão / operador em dois detalhes:

# Seu resultado não possui a parte fracionária ‒ está ausente (para inteiros), ou é sempre igual a zero (para flutuantes); isso significa que os resultados são sempre arredondados;
# Aplica-se a regra integer vs. float.

# Como você pode ver, a divisão de inteiro por inteiro dá um resultado inteiro.
print(6 // 3)  # 2
# Todos os outros casos produzem floats.
print(6 // 3.)  # 2.0
print(6. // 3)  # 2.0
print(6. // 3.)  # 2.0

# Observe o trecho a seguir:
print(6 // 4)  # 1
print(6. // 4)  # 1.0
# Obtemos dois uns - um inteiro e um flutuador.

# O resultado da divisão do número inteiro é sempre arredondado para o valor inteiro mais próximo que é menor que o resultado real (não arredondado).
# Isso é muito importante: o arredondamento sempre vai para o número inteiro menor.

# Imagine que usamos / em vez de // - você poderia prever os resultados?
print(6 / 4)  # 1.5
print(6. / 4)  # 1.5

# Observe o código abaixo e tente prever os resultados mais uma vez:
print(-6 // 4)  # -2
print(6. // -4)  # -2.0
# O resultado é dois pares negativos. O resultado real (não arredondado) é -1,5 em ambos os casos. No entanto, os resultados são sujeitos a arredondamento. O arredondamento vai em direção ao valor inteiro menor, e o valor inteiro menor é -2, portanto: -2 e -2.0.

# Note a diferença em relação à divisão tradicional
print(-6 / 4)  # -1.5
print(6 / -4)  # -1.5

# Restante (módulo)
# Sua representação gráfica em Python é o sinal de % (percentual), que pode parecer um pouco confuso. O resultado do operador é o restante após a divisão do número inteiro. Em outras palavras, é o valor que falta após dividir um valor por outro para produzir um quociente inteiro.

print(14 % 4)  # 2
# Como você pode ver, o resultado é dois. É por isso que:
# 14 // 4 dá 3 → este é o quociente inteiro;
# 3 * 4 dá 12 → como resultado da multiplicação de quociente e divisor;
# 14 - 12 dá 2 → este é o restante.

# Este exemplo é um pouco mais complicado:
print(12 % 4.5)  # Qual é o resultado?
# 3.0 – não 3, mas 3,0.
# A regra ainda funciona: 12 dividido por 4,5 dá 2,6666666666666665.
# O quociente é 2.
# O produto de 2 e 4,5 é 9.
# O restante é 12 - 9 = 3,0
# O resultado é um float porque um dos operandos é um float.

"""Como não dividir
Como você provavelmente sabe, a divisão por zero não funciona.
Não tente:
realizar uma divisão por zero;
realizar uma divisão inteira por zero;
encontre o resto de uma divisão por zero."""

# Adição
# O operador de adição é o sinal de + (mais), totalmente conforme os padrões matemáticos.

# O operador de subtração, os operadores unários e binários

# O operador de subtração é obviamente o sinal - (menos), embora você deva
# notar que esse operador também tem outro significado - ele pode alterar o sinal de um número.

# Esta é uma grande oportunidade para apresentar uma distinção muito importante entre operadores unários e binários.
# Ao subtrair aplicações, o operador menos espera dois argumentos: o esquerdo (um minuendo em termos aritméticos) e o direito (um subtraendo).
# Por esta razão, o operador de subtração é considerado um dos operadores binários, assim como os operadores de adição, multiplicação e divisão.

# Mas o operador menos pode ser usado de uma forma diferente (unária) ‒ dê uma olhada na última linha do trecho abaixo:
print(-4 - 4)   # -8 - operador binário: subtração
print(4. - 8)  # -4.0 - operador binário: subtração
print(-1.1)   # -1.1 - operador unário: altera o sinal do operando

# 2.3.3 Operadores e suas prioridades
# O fenômeno que faz com que alguns operadores ajam antes de outros é conhecido como a hierarquia de prioridades.

# O Python define com precisão as prioridades de todos os operadores e assume que os operadores de prioridade mais alta executam suas operações antes dos operadores de prioridade mais baixa.

# Operadores e suas ligações
# A ligação do operador determina a ordem das computações executadas por alguns operadores com igual prioridade, colocados lado a lado em uma expressão.
# A maioria dos operadores do Python tem ligação do lado esquerdo, o que significa que o cálculo da expressão é realizado da esquerda para a direita.
print(9 % 6 % 2)  # 1

# Há duas maneiras possíveis de avaliar essa expressão:

# da esquerda para a direita: primeiro 9 % 6 dá 3, e então 3 % 2 dá 1;
# da direita para a esquerda: primeiro 6 % 2 dá 0 e depois 9 % 0 causa um erro fatal.

# O resultado deve ser 1. Este operador tem ligação do lado esquerdo. Mas há uma exceção interessante.
print(2 ** 2 ** 3)  # 256

# Os dois resultados possíveis são:

# 2 ** 2 → 4; 4 ** 3 → 64
# 2 ** 3 → 8; 2 ** 8 → 256

# O resultado mostra claramente que o operador de exponenciação usa a associação do lado direito.

# Lista de prioridades
"""
Prioridade	Operador	
1           	**	
2	            +, - 	unário
3	            *, /, //, %	
4	            +, -	binário
"""
# observação: operadores unários localizados ao lado direito do operador de potência se vinculam mais fortemente
# Exemplo:
print(-3 ** 2)  # -9 - o operador unário - é aplicado depois do operador de potência.
# de forma explicita seria como: -(3 ** 2)

print((-3) ** 2) # 9 - o operador unário - é aplicado antes do operador de potência (o parêntese é usado para alterar a prioridade)
# de forma explicita seria como: (-3) ** 2
# -3 * -3 = 9 - sinais iguais na multiplicação resultam em um número positivo

# caso fosse (-3) ** 3 o resultado seria -27 pois teríamos (-3 * -3) * -3 = +9 * -3 = -27
# sinais diferentes na multiplicação resultam em um número negativo

# Operadores e parênteses
# Claro, você sempre pode usar parênteses, o que pode alterar a ordem natural de um cálculo.
# Conforme as regras aritméticas, sub-expressões entre parênteses são sempre calculadas primeiro.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # 10.0


"""
2.3.4 RESUMO DA SEÇÃO

Pontos principais
1. Uma expressão é uma combinação de valores (ou variáveis, operadores, chamadas para funções - você aprenderá sobre eles em breve) que resulta em um determinado valor, por exemplo, 1 + 2.

2. Operadores são símbolos especiais ou palavras-chave que são capazes de operar nos valores e realizar operações (matemáticas), por exemplo, o operador * multiplica dois valores: x * y.

3. Operadores aritméticos em Python: + (adição), - (subtração), * (multiplicação), / (divisão clássica ‒ sempre retorna um ponto flutuante), % (módulo ‒ divide o operando esquerdo pelo operando direito e retorna o restante da operação, por exemplo , 5 % 2 = 1), ** (exponenciação ‒ operando esquerdo elevado à potência do operando direito, por exemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (floor/divisão inteira ‒ retorna um número resultante da divisão, mas arredondado para o número inteiro mais próximo, por exemplo, 3 // 2.0 = 1.0)

4. Um operador unário é um operador com apenas um operando, por exemplo, -1 ou +3.

5. Um operador binário é um operador com dois operandos, por exemplo, 4 + 5 ou 12 % 5.

6. Alguns operadores agem antes de outros - a hierarquia de prioridades:

o operador ** (exponenciação) tem a prioridade mais alta;
então o unário + e - (Nota: um operador unário à direita do operador de exponenciação se liga mais fortemente, por exemplo, 4 ** -1 é igual a 0.25)
então: *, /, e %,
e, por fim, a prioridade mais baixa: binário + e -.
7. Sub-expressões entre parênteses são sempre calculadas primeiro, 
por exemplo, 15 - 1 * (5 * (1 + 2)) = 0.

8. O operador de exponenciação usa a associação do lado direito, por exemplo, 2 ** 2 ** 3 = 256.
"""