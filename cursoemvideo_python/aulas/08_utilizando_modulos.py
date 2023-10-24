# Curso Python Aula 08 - Utilizando Módulos

"""RESUMO"""
# Explicação do conceito de módulos em Python e sua utilidade para estender a funcionalidade de programas.
# Demonstração de como importar módulos em Python usando o comando "import" e a possibilidade de importar funções específicas de um módulo usando "from".
# Exemplificação do uso do módulo "math" para realizar operações matemáticas, enfatizando a importância de compreender as funcionalidades dos módulos importados.
# Discussão sobre a necessidade de manter os módulos atualizados para garantir um desempenho ideal.
# Explicação adicional sobre a importação de módulos e o uso de funcionalidades específicas, bem como a possibilidade de importar módulos diretamente do diretório local.
# Demonstrações de como instalar e gerenciar módulos, incluindo adição e remoção de módulos de um projeto.
# Apresentação de desafios de programação, incentivando os espectadores a praticar e não depender da cópia de código da internet.
# Introdução de exercícios práticos, como criar um programa para selecionar a ordem de apresentações de estudantes e criar um programa para reproduzir arquivos MP3 usando módulos.
# Incentivo aos espectadores para tentar os exercícios por conta própria e não apenas assistir às soluções prontas.
# Lembrete para se inscrever no canal e ficar atualizado sobre novos vídeos e exercícios.

"""CONTEÚDO"""

# Comandos de Importação de Bibliotecas em Python

# Utilizando "import," importamos todos os comandos de uma biblioteca inteira.
# import exemplo

# Utilizando "from import," importamos um comando específico de uma biblioteca.
# from exemplo import algo

# Biblioteca math - Exemplos de Utilização:

# Função "ceil" - Arredonda um número para cima.
# Função "floor" - Arredonda um número para baixo.
# Função "trunc" - Elimina a parte decimal de um número.
# Função "pow" - Calcula a potência de um número.
# Função "sqrt" - Calcula a raiz quadrada de um número.
# Função "factorial" - Calcula o fatorial de um número.
# Para importar todas as funções da biblioteca math, utilize: import math
# Para importar funções específicas da biblioteca math, utilize: from math import pow, trunc

# Importando as bibliotecas necessárias

# Solicitando ao usuário um número
import math
import random
num = int(input('Digite um número: '))

# Utilizando a biblioteca math para calcular a raiz quadrada do número inserido
raiz = math.sqrt(num)

# Utilizando a função "ceil" para arredondar para cima e exibindo o resultado
print("Arredondando para cima:", math.ceil(raiz))

# Utilizando a função "floor" para arredondar para baixo e exibindo o resultado
print("Arredondando para baixo:", math.floor(raiz))

# Biblioteca random - Geração de Números Aleatórios

# A função "randint(a, b)" gera um número aleatório no intervalo definido por "a" e "b."
numero = random.randint(1, 10)
print("Número aleatório no intervalo de 1 a 10:", numero)
