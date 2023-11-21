# Capítulo 1: A jornada do programa

## 1.1 - O que é um programa?
"""Um programa é uma sequência de instruções que especifica como executar uma operação de computação.

entrada: Receber dados do teclado, de um arquivo, da rede ou de algum outro dispositivo.

saída: Exibir dados na tela, salvá-los em um arquivo, enviá-los pela rede etc.

matemática: Executar operações matemáticas básicas

execução condicional: Verificar a existência de certas condições e executar o código adequado.

repetição: Executar várias vezes alguma ação, normalmente com algumas variações.

Programar é o processo de quebrar uma tarefa grande e complexa em sub-tarefas cada vez menores, até que estas sejam simples o suficiente para serem executadas por uma dessas instruções básicas."""

# Tipos de Dados
# Existem vários tipos de dados em Python, incluindo inteiros, números de ponto flutuante, strings e booleanos.

# Exemplo de inteiros
numero_inteiro = 10
print(numero_inteiro)  # Saída: 10
print(type(numero_inteiro))  # Saída: <class 'int'>

# Exemplo de números de ponto flutuante
numero_decimal = 3.14
print(numero_decimal)  # Saída: 3.14
print(type(numero_decimal))  # Saída: <class 'float'>

# Exemplo de strings
texto = "Olá, Python!"
print(texto)  # Saída: Olá, Python!
print(type(texto))  # Saída: <class 'str'>

# Exemplo de booleanos
verdadeiro = True
print(verdadeiro)  # Saída: True
print(type(verdadeiro))  # Saída: <class 'bool'>


# Operadores Aritméticos
# Python suporta operadores aritméticos básicos, como +, -, *, /, // (divisão inteira) e % (resto).

a = 5
b = 2

soma = a + b
print(soma)  # Saída: 7

subtracao = a - b
print(subtracao)  # Saída: 3

multiplicacao = a * b
print(multiplicacao)  # Saída: 10

divisao = a / b
print(divisao)  # Saída: 2.5

divisao_inteira = a // b
print(divisao_inteira)  # Saída: 2

resto = a % b
print(resto)  # Saída: 1


# Concatenação de Strings
# Para combinar strings, você pode usar o operador de adição (+).

nome = "João"
sobrenome = "Silva"

nome_completo = nome + " " + sobrenome
print(nome_completo)  # Saída: João Silva


# Comandos Básicos: print, input, type
# O comando print é usado para exibir informações na tela.

print("Olá, mundo!")

# O comando input é usado para receber entrada do usuário.
entrada_usuario = input("Digite algo: ")
print("Você digitou:", entrada_usuario)

# O comando type é usado para obter o tipo de uma variável.
tipo_variavel = type(10)
print(tipo_variavel)  # Saída: <class 'int'>

# 1.9 - Exercícios
## Exercício 1.1
# Sempre que estiver testando um novo recurso, você deve tentar fazer erros. Por exemplo, no programa “Hello, World!”, o que acontece se omitir uma das aspas?
"""
SyntaxError: incomplete input
"""
# E se omitir ambas?
"""
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"""
# E se você soletrar a instrução print de forma errada?
"""
Se houver apenas uma palávra apresenta o erro -
NameError: name 'hello' is not defined. Did you mean: 'help'? - pois interpreta que se trata de uma variável não definida.

Se houver duas ou mais palavras, apresenta o erro -
NameError: name 'prin' is not defined. Did you mean: 'print'? - pois interpreta que se tratam de duas ou mais variáveis não separadas por virgula.
"""
# Este tipo de experimento ajuda a lembrar o que foi lido; também ajuda quando você estiver programando, porque assim conhecerá o significado das mensagens de erro. É melhor fazer erros agora e de propósito que depois e acidentalmente. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
"""
Apresenta os erros - SyntaxError: incomplete input - ou - SyntaxError: unmatched ')'
"""
# Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
"""
Se omitir uma aspa apresenta o erro - SyntaxError: incomplete input - pois interpreta que é uma string de fato com a sintaxe incompleta e se omitir as duas apresenta o erro - NameError: name 'a' is not defined - pois não interpreta como string, e sim uma variável não declarada.
"""
# Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
"""
O programa interpreta que o segundo sinal de + significa que o número é positivo e faz a soma normalmente. Assim como em 2+-2 retorna 0, o ideal é colocar entre aspas para ficar mais auto explicativo
"""
# Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
"""
Exibe o erro - SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers - Significa que zeros a esquerda de números inteiros não são permitidos mas em float e octais sim
"""
# O que acontece se você tiver dois valores sem nenhum operador entre eles?
"""
Se estiverem juntos sem espaços, serão considerados como um só, se houver espaço entre eles exibe o erro - SyntaxError: incomplete input
"""
## Exercício 1.2
# Inicialize o interpretador do Python e use-o como uma calculadora. Quantos segundos há em 42 minutos e 42 segundos?
"""Sabendo que 1 minuto possui 60 segundos, atribuimos esse valor a variável minuto"""

segundos = 1
minutos = 60 * segundos
# Calculando a quantidade de segundos em 42 minutos e 42 segundos
tempo = (42 * minutos) + (42 * segundos)
print(f'A quantidade de segundos em 42 minutos e 42 segundos é de {tempo}.')

# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

quilometros_em_milhas = 1.61
dez_quilometros = 10 * quilometros_em_milhas
print(f'Em 10Km há {dez_quilometros} milhas.')

# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

# Dados fornecidos
distancia_total_km = 10
tempo_total_minutos = 42 + (42 / 60)  # Convertendo os segundos para minutos

# Convertendo a distância de quilômetros para milhas
quilometros_para_milhas = 1 / 1.61
distancia_total_milhas = distancia_total_km * quilometros_para_milhas

# Calculando o passo médio (tempo por milha em minutos)
passo_medio_minutos_por_milha = tempo_total_minutos / distancia_total_milhas

# Convertendo o passo médio para minutos e segundos
passo_medio_minutos = int(passo_medio_minutos_por_milha)
passo_medio_segundos = int((passo_medio_minutos_por_milha - passo_medio_minutos) * 60)

# Calculando a velocidade média (milhas por hora)
tempo_total_horas = tempo_total_minutos / 60
velocidade_media_milhas_por_hora = distancia_total_milhas / tempo_total_horas

# Exibindo os resultados
print(f'O passo médio é de {passo_medio_minutos} minutos e {passo_medio_segundos} segundos por milha.')
print(f'A velocidade média é de {velocidade_media_milhas_por_hora:.2f} milhas por hora.')




