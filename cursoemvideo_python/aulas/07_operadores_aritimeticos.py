# Curso Python Aula 07 - Operadores aritiméticos

"""RESUMO"""

# Discussão sobre operações aritméticas em Python, incluindo adição, subtração, multiplicação, divisão e módulo.

# Explicação dos operadores aritméticos em Python e sua utilização com números, strings e variáveis.

# Ênfase na importância de entender a precedência de operações e o uso de parênteses para controlar a ordem das operações.

# Demonstração do uso do operador de exponenciação para cálculo de potências e como combinar essa operação com multiplicação e adição.

# Exploração de operadores adicionais, como concatenação de strings, e funções embutidas, como raiz cúbica e formatação de strings.

# Exemplos de operadores relacionais e lógicos para comparação de valores e tomada de decisões em programas.

# Incentivo para praticar e digitar o código manualmente para melhor compreensão.

# Apresentação de exercícios de programação para praticar o uso de operadores aritméticos em Python.

# Discussão sobre colaboração e a importância de trabalhar em equipe para criar projetos incríveis.

# Agradecimento aos espectadores e convite para colaborar comentando seus nomes.

# Ênfase na importância da educação e agradecimento à audiência pelo apoio contínuo.

"""CONTEÚDO"""

# Operadores

# Operador de igualdade (==)
# Adição (+): 5 + 2 == 7
# Subtração (-): 5 - 2 == 3
# Multiplicação (*): 5 * 2 == 10
# Potência (**): 5 ** 2 == 25
# Divisão (/): 5 / 2 == 2.5
# Divisão inteira (//): 5 // 2 == 2
# Resto da divisão (%): 5 % 2 == 1

# Ordem de precedência

# Primeiro: Parênteses ()
# Segundo: Exponenciação/Potências **
# Terceiro: Multiplicação * e Divisões /, // e % (na ordem em que aparecem)
# Último: Adição + e subtração -


print(5 + 3 * 2)  # A multiplicação tem prioridade. O resultado é == 11
print(3 * 5 + 4 ** 2)  # A potência tem prioridade. O resultado é == 31
print(3 * (5 + 4) ** 2) # A soma entre os parênteses tem prioridade, seguido da potência. O resultado é == 243

# Função interna pow(base, expoente) - Potencia
print(pow(4,2)) # É o mesmo que 4 ** 2

# Calcular a raiz quadrada de um número é o mesmo que elevá-lo a meio (1/2) visto que 2 é o mesmo que 2/1, então fazemos a operação inversa
print(81**(1/2))  # Retornará 9.0 (Divisão retorna um valor float)

# Operadores em strings

# Concatenação (+) - Une os textos
# Multiplicação de texto (*) - Exibe o texto x vezes 'Oi'*5 Exibirá OiOiOiOiOi
# Limitando caracteres: Podemos definir a quantidade de espaços para caracteres nas strings formatadas.
nome = 'Maycon'  # Tem 6 caracteres
# Serão adicionados espaços adicionais até completarem 20
print(f'Olá {nome:20}!')
# Podemos usar os caracteres < e > para selecionar o alinhamento a esqueda ou direita:
print(f'Olá {nome:<20}!')  # Esquerda
print(f'Olá {nome:>20}!')  # Direita
# Ou circunflexo para alinha centralizado
print(f'Olá {nome:^20}!')
# Podemos definir um caracter que desejarmos substituindo os espaços
print(f'Olá {nome:=^20}!')

# Podemos formatar o numero de casas decimais
pi = 3.1415
print(f'{pi:.2f}')  # Irá exibir apenas 2 casas decimais >> Retorna 3.14

# Quebra de linha
# Irá exibir as instruções print na mesma linha
print('Uma linha', end=' apoio visual ')
print('Outra linha')
