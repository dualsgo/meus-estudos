# 4.5 Seção 5 - Criação de funções de vários parâmetros
# Bem-vindo à seção 5, onde analisaremos os seguintes exemplos de funções multiparâmetros: calculadora de IMC, conversor de unidades, testador de triângulos, calculadora de áreas de triângulos, fatorial, Fibonacci e funções recursivas.

# 4.5.1 Funções de Exemplo: avaliando o IMC

# Vamos começar uma função para avaliar o índice de massa corporal (IMC).

# Como você pode ver, a fórmula obtém dois valores:

# peso (originalmente em quilogramas)
# altura (originalmente em metros)

# Parece que essa nova função terá dois parâmetros. O nome será bmi, mas se você preferir outro nome, use-o.

def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65)) # saídas: 19.283746556473833

# A função atende às nossas expectativas, mas é um pouco simples - ela pressupõe que os valores de ambos os parâmetros são sempre significativos. Definitivamente, vale a pena verificar se são confiáveis.
# Vamos verificar os dois e retornar None se algum parecer suspeito.

# Avaliação do IMC e conversão de unidades imperiais em unidades métricas

def bmi(weight, height):
  if height < 1.0 or height > 2.5 or \
  weight < 20 or weight > 200:
    return None

  return weight / height ** 2


print(bmi(352.5, 1.65)) # saídas: None

# Podemos escrever duas funções simples para converter unidades imperiais em unidades métricas. Vamos começar com libras. É um fato bem conhecido que 1 lb = 0.45359237 kg. Usaremos isso em nossa nova função.



def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(1)) # saídas: 0.45359237

# E agora é hora de pés e polegadas: 1 pé = 0.3048 m, e 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(1, 1)) # saídas: 0.3302


# Vamos converter seis pés em metros:
print(ft_and_inch_to_m(6, 0)) # saídas: 1.8288


# É bem possível que às vezes você queira usar apenas pés sem polegadas. O Python vai ajudar? Claro que sim.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
# Agora, o parâmetro inch tem seu valor padrão igual a 0.0.


print(ft_and_inch_to_m(6)) # saídas: 1.8288


# Por fim, o código é capaz de responder à pergunta: qual é o IMC de uma pessoa de 5'7" de altura e pesando 176 libras?

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) # saídas: 27.60406069007222
 


# 4.5.2 Funções de exemplo: triângulos
# Vamos jogar com triângulos agora. Vamos começar com uma função para verificar se três lados de determinados comprimentos podem construir um triângulo.

# Sabemos pela escola que a soma de dois lados arbitrários precisa ser maior que o terceiro lado.

# Não será um desafio difícil. A função terá três parâmetros - um para cada lado.
# Ele retornará True se os lados puderem construir um triângulo, e False caso contrário. Nesse caso, is_a_triangle é um bom nome para essa função.

def is_a_triangle(a, b, c):
  if a + b <= c:
    return False
  if b + c <= a:
    return False
  if c + a <= b:
    return False
  return True

# Esta é uma versão mais compacta:
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
 
# Podemos compactá-lo ainda mais?
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
 
# Negamos a condição (invertemos os operadores relacionais e substituímos or s com and s, recebendo uma expressão universal para testar triângulos). Vamos instalar a função em um programa maior. Ele solicitará ao usuário três valores e fará uso da função.

# Triângulos e o teorema de Pitágoras
def is_a_triangle(a, b, c):
 return a + b > c and b + c > a and c + a > b


a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Entre no segundo lado\'s comprimento: '))
c = float(input('Entre no terceiro lado\'s comprimento: '))

if is_a_triangle(a, b, c):
 print('Sim, pode ser um triângulo.')
else:
 print('Não, não pode ser um triângulo.')

# Na segunda etapa, tentaremos garantir que um determinado triângulo seja um triângulo de ângulo reto. Vamos precisar fazer uso do teorema de Pitágoras: a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa.
# c2 = a2 + b2

# Como podemos reconhecer qual dos três lados é a hipotenusa? A hipotenusa é o lado mais longo.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
 
# Veja como testamos a relação entre a hipotenusa e os lados restantes - escolhemos o lado mais longo e aplicamos o teorema de Pitágoras para verificar se está tudo certo. Isso exige três verificações no total.
# Também podemos avaliar a área de um triângulo. A fórmula da Heron será útil aqui:

# s = (a + b + c) / 2

# Vamos usar o operador de exponenciação para encontrar a raiz quadrada - pode parecer estranho, mas funciona:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))
 
# Tentamos fazer isso com um triângulo de ângulo reto como uma metade de um quadrado com um lado igual a 1. Isso significa que sua área deve ser igual a 0,5.
# É estranho - o código produz a seguinte saída:
# 0.49999999999999983

# É muito próximo de 0,5, mas não é exatamente 0,5. O que isso significa? É um erro?

# Não, não é. Essas são as especificidades dos cálculos de ponto flutuante. Logo vamos falar mais sobre isso.

# 4.5.3 Exemplos de funções: Fatoriais
# Outra função que vamos escrever são os fatoriais. Você se lembra como um fatorial é definido?
"""0! = 1 (sim! É verdade)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n"""

# Ela é marcada com um ponto de exclamação e é igual ao produto de todos os números naturais de um até seu argumento. Vamos escrever o nosso código. Vamos criar uma função e chamaremos ela de factorial_function. Aqui está o código:
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6):  # testando
    print(n, factorial_function(n))
 
# Observe como repetimos passo a passo a definição matemática e como usamos o loop for para encontrar o produto.

# 4.5.4 Números de Fibonacci
# Você está familiarizado com os números de Fibonacci?

# Eles são uma sequência de números inteiros criados usando uma regra muito simples:

# o primeiro elemento da sequência é igual a um (Fib1 = 1)
# o segundo também é igual a um (Fib 2 = 1)
# cada número subsequente é a the_sum dos dois números anteriores:( Fib i = Fib i-1 + Fib i-2)

# Vamos criar a função fib e testá-la. Aqui está:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10):  # testando
    print(n, "->", fib(n))
 
# Analise o corpo do loop for com cuidado e descubra como movemos as variáveis elem_1 e elem_2 pelos números subsequentes de Fibonacci.

# 4.5.5 Recursão
# Queremos mostrar mais uma coisa para tornar tudo completo: a recursão.

# Esse termo pode descrever muitos conceitos diferentes, mas um deles é especialmente interessante - o referente à programação de computadores.
# Nesse campo, a recursão é uma técnica em que uma função se chama.

# Esses dois casos parecem ser os melhores para ilustrar o fenômeno - fatoriais e números de Fibonacci. Especialmente o último.

# A definição dos números de Fibonacci é um exemplo claro de recursão. Já falamos a você que:

# A definição do i-ésimo número refere-se ao número i-1, e assim por diante, até que você atinja os dois primeiros. Isso pode ser usado no código? Sim, pode. Também pode tornar o código mais curto e claro.

# A segunda versão da nossa função fib() faz uso direto dessa definição:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
# Se você esquecer de considerar as condições que podem interromper a cadeia de invocações recursivas, o programa pode inserir um loop infinito.


# O fatorial tem um segundo lado recursivo também. Veja:
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
 

# # 4.5.6 RESUMO DA SEÇÃO

# 1. Uma função pode chamar outras funções, ou até mesmo ela mesma. 
# Quando uma função se chama, essa situação é conhecida como recursão, 
# e a função que se chama e contém uma condição de terminação específica 
# (ou seja, o caso base - uma condição que não diz à função para fazer 
# chamadas adicionais para essa função) é chamado de função recursiva.

# 2. Você pode usar funções recursivas no Python para escrever um código 
# limpo e elegante e dividi-lo em pedaços menores e organizados. Por outro 
# lado, você precisa ter muito cuidado, pois pode ser fácil cometer um erro 
# e criar uma função que nunca termina. Você também precisa se lembrar que 
# as chamadas recursivas consomem muita memória e, portanto, às vezes podem 
# ser ineficientes.

# Ao usar a recursão, você precisa levar em consideração todas as vantagens e desvantagens.

# A função fatorial é um exemplo clássico de como o conceito de recursão 
# pode ser colocado em prática:

# Implementação recursiva da função fatorial.
def factorial(n):
    if n == 1: # O caso base (condição de rescisão).
        return 1
    else:
        return n * factorial(n - 1)
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24














