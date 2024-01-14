# MIMO - 14 - Erros e exceções
# 14.1 - Erros e exceções

# Toda linguagem de programação possui:

# um alfabeto: conjunto de símbolos que podem ser usados para escrever programas
# um vocabulário: conjunto de palavras que podemos formar com os símbolos do alfabeto
# um lexicon: conjunto de palavras que têm um significado específico na linguagem de programação
# uma sintaxe: conjunto de regras que determinam como as palavras do vocabulário podem ser combinadas para formar programas válidos

# Às vezes, o Python não consegue entender o nosso código. Isso resulta em algo chamado SyntaxError. Isso geralmente acontece quando cometemos um erro de digitação ou esquecemos de fechar um parêntese, colchete ou aspas.

# Por exemplo:

# if > 10: # SyntaxError: invalid syntax
# O erro ocorre porque a palavra if existe no vocabulário do Python, mas não podemos usá-la sozinha. Precisamos combiná-la com outras palavras para formar uma instrução válida. O Python não sabe o que fazer com > 10 porque essa combinacão não faz sentido ferindo a sintaxe da linguagem.

# Erros de sintaxe geralmente ocorrem devido a erros de digitação, como palavras chave com erros ortográficos, como iff em vez de if.

# O recuo incorreto ou ausente resultará em um IndentationError, que é um tipo específico de SyntaxError.

# Colocar uma palavra chave no lugar errado também resultará em um SyntaxError.

# + 1 for item in [1, 2, 3]

# Esquecer símbolos , como dois pontos, colchetes ou parênteses, também resultará em um SyntaxError.

# Instruções incompletas também resultarão em um SyntaxError. Como por exemplo condicionais sem um bloco de código.

# O Python adiciona detalhes ao erro, como quando usamos uma string como nome de variável.
# "name" = "Ricky" # SyntaxError: can't assign to literal

# No console, o circunflexo (^) aponta para o local exato onde o erro ocorreu.

# As vezes o Python entende nosso código, mas não consegue executá-lo.

# O ZeroDivisionError ocorre quando tentamos dividir um número por zero.
# share = 100 / 0 # ZeroDivisionError: division by zero

# Um erro de exceção ocorre quando o Python entende o código, mas não consegue executá-lo. Isso geralmente ocorre quando tentamos executar uma operação inválida.

# O NameError ocorre quando tentamos usar uma variável que não existe.
# share = size / 6 # NameError: name 'size' is not defined

# O TypeError ocorre quando tentamos executar uma operação em um tipo de dados que não suporta essa operação.
# "3" + 1 # TypeError: can only concatenate str (not "int") to str

# FileNotFoundError ocorre quando tentamos abrir um arquivo que não existe ou erramos o caminho do arquivo.
# open("file.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'

# AttributeError ocorre quando tentamos acessar um atributo que não existe.
# "3".isalpha() # AttributeError: 'int' object has no attribute 'isalpha'

# O texto mostrado quando uma exceção é lançada é chamado de traceback. O traceback mostra o caminho que o programa percorreu até o ponto em que ocorreu o erro e isso nos ajuda a depurar o código.

# Alguns métodos não produzem erros e são capazes de resolver os problemas sozinhos. 
# count() retorna o número de ocorrências de um elemento em uma lista. Se o elemento não estiver na lista, ele retornará 0.

grades = ["A", "B", "C", "A", "B", "A"]
print(grades.count("D"))  # 0


# É melhor ler o traceback de baixo para cima. O traceback mostra o caminho que o programa percorreu até o ponto em que ocorreu o erro. O último item do traceback é o erro real.

# Se o Python não conseguir importar um módulo, ele lançará um ModuleNotFoundError.

# Se um índice estiver fora do intervalo, o Python lançará um IndexError.

# Erros de Syntax são retornados antes do programa ser executado. Erros de exceção são retornados durante a execução do programa.

# Erros lógicos são erros que ocorrem quando o programa não faz o que deveria fazer. O programa é executado sem erros, mas o resultado não é o esperado.

# Unspected EOF significa que o Python encontrou o final do arquivo quando não deveria. Isso geralmente ocorre quando esquecemos de fechar um parêntese, colchete ou aspas.