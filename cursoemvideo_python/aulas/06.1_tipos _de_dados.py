# MIMO - Tipos de Dados

# STRING (str): São caracteres entre aspas. O texto pode conter letras, números e caracteres especiais.
tipo_1 = 'Letras, números (2) e caracteres especiais (@)'

# DADOS NUMÉRICOS: Representam valores numéricos e podem ser divididos em dois principais tipos.

# Inteiros/Integer (int): São números sem casas decimais.
numero_int = 10

# Ponto flutuante/Float (float): São números com casas decimais, representados usando um ponto como separador decimal.
numero_float = 10.0
zero_float = .1  # Podemos omitir o zero à esquerda do ponto.

# BOOLEANOS (bool): São valores especiais que representam verdadeiro ou falso.

# True (verdadeiro) representa um valor verdadeiro, geralmente equivalente a 1.
verdadeiro = True

# False (falso) representa um valor falso, geralmente equivalente a zero ou vazio.
falso = False

# Além disso, os booleanos podem ser usados para expressar condições, como em declarações condicionais (if, else) e loops.
condicao = numero_int > 5  # Exemplo de uso de um booleano em uma condição.

# Os booleanos são essenciais para controlar o fluxo do programa, permitindo a execução condicional de blocos de código.
if condicao:
    print("A condição é verdadeira.")
else:
    print("A condição é falsa.")
