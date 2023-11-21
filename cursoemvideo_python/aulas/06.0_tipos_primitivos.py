# Curso Python Aula 06 - Tipos primitivos

"""RESUMO"""

# O Professor Gustavo Guanabara agradece por alcançar o segundo objetivo do curso e anuncia uma playlist com mais de 100 exercícios resolvidos no YouTube.

# Introdução aos tipos primitivos na programação, destacando que Python trabalha com quatro tipos primitivos fundamentais. Menciona que mais tipos primitivos serão abordados conforme o curso avança.

"""# Introdução aos Tipos Primitivos em Python:

# 1. Inteiros (int): Representam números inteiros.
idade = 25

# 2. Números de Ponto Flutuante (float): Representam números decimais.
altura = 1.75

# 3. Strings (str): Representam texto, são delimitadas por aspas simples ou duplas.
nome = "João"

# 4. Booleanos (bool): Representam valores lógicos, True (verdadeiro) ou False (falso).
tem_carteira = True

# Mais tipos primitivos serão explorados à medida que o curso avança.
"""

# Demonstração do uso de funções de input para ler e armazenar entradas do usuário em variáveis. Exemplo de leitura de dois números e armazenamento em variáveis separadas, seguido pela adição dos números e armazenamento do resultado em outra variável.

# Discussão sobre o uso dos comandos input e print em Python. Input para ler dados do teclado e print para exibir saídas na tela. Exemplo de uso desses comandos para realizar adições e exibir o resultado.

# Explicação sobre diferentes tipos de dados primitivos em Python, incluindo inteiros, floats, booleanos e strings. Ênfase na importância de definir corretamente os tipos de dados para evitar erros.

# Demonstração de como usar a função print() para exibir saídas ao usuário, manipular dados e formatar saídas.

# Introdução de desafios para os espectadores, incluindo a criação de programas que calculam a soma de números fornecidos pelo usuário e determinam o tipo primitivo de dados inseridos pelo usuário.

# Incentivo para que os espectadores participem da comunidade do curso, compartilhem soluções e façam perguntas.

"""CONTEÚDO"""

# Tipos primitivos

# int - integer: São valores numéricos sem casas decimais após a vírgula (7, -4, 0, 9875)
# float - ponto flutuante: São valores que possuem casas decimais após a vírgula (4.5, 0.076, -15.223, 7.0)
# bool - boolean: São valores lógicos (True e False)
# str - string: São cadeias com nenhuma ou mais caracteres que podem ser números, letras ou símbolos ('Olá', '7.5', '', '@#$')

# Exemplo de tipos primitivos

inteiro = 42
flutuante = 3.14
booleano = True
string = "Olá, mundo"

# String formatada

# As strings formatadas são uma ferramenta poderosa para criar mensagens que combinam variáveis e texto de forma conveniente. Para utilizá-las, prefixamos a string com um "f" antes das aspas, e utilizamos chaves {} para incorporar os valores das variáveis no texto:
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
# Iniciamos a string com um f antes das aspas, seguimos com o texto e utilizamos chaves ns posições que desejamos exibir os valores.
print(f'A soma entre {n1} e {n2} vale {s}.')
# O valor será exibido no lugar das chaves {}

# Função type()

# A função type() é utilizada para determinar o tipo de dado armazenado em uma variável. Ela fornece informações sobre o tipo da variável, o que pode ser útil para depuração e controle de fluxo do programa.
print(type(s))

# Métodos de teste de tipo

# Python oferece métodos que permitem verificar o tipo de dado armazenado em variáveis, como o método isnumeric() para strings. Estes métodos auxiliam na validação e manipulação de dados

# Método isnumeric() para verificar se a string contém apenas dígitos numéricos
numero = "12345"
print(numero.isnumeric())  # Saída: True

# Método isalpha() para verificar se a string contém apenas letras
letras = "abcde"
print(letras.isalpha())  # Saída: True

# Método isalnum() para verificar se a string contém apenas letras e/ou números
alphanumeric = "abc123"
print(alphanumeric.isalnum())  # Saída: True

# Método isupper() para verificar se a string está em maiúsculas
maiusculas = "TODAS EM MAIÚSCULAS"
print(maiusculas.isupper())  # Saída: True

# Método islower() para verificar se a string está em minúsculas
minusculas = "todas em minúsculas"
print(minusculas.islower())  # Saída: True

# Método istitle() para verificar se a string segue o formato de título (cada palavra começa com maiúscula)
titulo = "Um Título Em Python"
print(titulo.istitle())  # Saída: True
