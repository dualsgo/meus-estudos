# Um programa é uma sequência de instruções que especifica como executar uma operação de computação
'''
entrada: Receber dados do teclado, de um arquivo, da rede ou de algum outro dispositivo.
saída: Exibir dados na tela, salvá-los em um arquivo, enviá-los pela rede etc.
matemática: Executar operações matemáticas básicas como adição e multiplicação.
execução condicional: Verificar a existência de certas condições e executar o código adequado.
repetição: Executar várias vezes alguma ação, normalmente com algumas variações.

Acredite ou não, isto é basicamente tudo o que é preciso saber. Cada programa que você já usou, complicado ou não, é composto de instruções muito parecidas com essas. Podemos então chegar à conclusão de que programar é o processo de quebrar uma tarefa grande e complexa em subtarefas cada vez menores, até que estas sejam simples o suficiente para serem executadas por uma dessas instruções básicas.
'''
# Exercício 1.1

# Este exercício sugere a realização de experimentos para entender como o Python lida com erros.
# É uma prática útil para aprender como a linguagem funciona e como interpretar mensagens de erro.

# Primeiro, experimentaremos com a função 'print'.
# Tente omitir uma ou ambas as aspas e veja o que acontece.
print("Hello, World!")  # Correto
# print(Hello, World!)  # Isso resultará em um erro de sintaxe

# Em uma instrução 'print', o que acontece se você omitir um dos parênteses ou ambos?
# Experimente:
# print("Hello, World!"  # Isso resultará em um erro de sintaxe
# print "Hello, World!")  # Isso também resultará em um erro de sintaxe

# O que acontece se você usar um sinal de menos antes de um número?
# E se você escrever algo como '2++2'?
# Experimente:
# print(-2)  # Isso imprimirá -2
# print(2++2)  # Isso resultará em um erro de sintaxe

# Na notação matemática, zeros à esquerda são aceitáveis, como em '02'.
# O que acontece se você tentar usar isso em Python?
# Experimente:
# print(02)  # Isso resultará em um erro de sintaxe

# O que acontece se você tiver dois valores sem nenhum operador entre eles?
# Experimente:
# print(2 3)  # Isso resultará em um erro de sintaxe

# Exercício 1.2

# Neste exercício, você usará o interpretador do Python como uma calculadora.

# Quantos segundos há em 42 minutos e 42 segundos?
# Vamos calcular isso:
total_segundos = 42 * 60 + 42
print("Total de segundos:", total_segundos)

# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
# Vamos calcular isso:
quilometros = 10
milhas = quilometros / 1.61
print("Milhas equivalentes:", milhas)

# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)?
# Vamos calcular o passo médio em minutos e segundos:
tempo_total = 42 * 60 + 42  # Tempo total em segundos
passo_medio = tempo_total / milhas  # Tempo médio por milha em segundos
minutos = int(passo_medio / 60)  # Converte para minutos
segundos = passo_medio % 60  # Calcula os segundos restantes
print("Passo médio: {} minutos e {} segundos".format(minutos, segundos))

# Qual é a sua velocidade média em milhas por hora?
# Vamos calcular a velocidade média:
horas = (42 * 60 + 42) / 3600  # Converte o tempo total para horas
velocidade_media = milhas / horas
print("Velocidade média: {} milhas por hora".format(velocidade_media))
