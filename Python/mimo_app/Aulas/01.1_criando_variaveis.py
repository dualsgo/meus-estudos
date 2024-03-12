# MIMO - 01 - Noções básicas de Python

# 01.1 - Criando variáveis

# Python é uma linguagem de programação fantástica para iniciantes e especialistas.
# É a linguagem de escolha para muitas empresas e uma escolha popular para projetos pessoais. Você pode usá-lo para automatizar tarefas, sair na frente no trabalho com análise de dados, aprendizado de máquina e muito mais!
# Não importa o quão complexo seja um programa, ele começa com uma única linha de código. Essa primeira linha geralmente é uma variável. Os programas usam variáveis para lembrar informações. Como caixas móveis, as variáveis têm conteúdo e nomes que nos dizem o que está dentro.

# Nomes das variáveis

# Para criar uma variável, começamos digitando seu nome. 
exemplo = "Valor da variável"

# Os nomes das variáveis devem ser palavras únicas sem espaços ou, se quisermos um nome de variável com várias palavras, podemos separar as palavras com sublinhados (_) ou maiúsculas.

# usamos sublinhado (_) para conectar as palavras adicionais (snake_case).
exemplo_snake_case = 'Parece um cobra' # minúsculas e sublinhado (snake_case)

# Ou usamos maiúsculas para cada palavra adicional (CamelCase).
exemploCamelCase = 'Lembra as corcovas de um camelo' # maiúsculas e minúsculas (CamelCase)

# Para nos ajudar a entender o que está numa variável, escolhemos nomes descritivos em vez de abreviações e etc
ano_atual = 2024 

# Após criar e nomear uma variável, usamos o operador de atribuição (=) para armazenar um valor dentro dela. Armazenar um valor em uma variável é como colocar coisas em uma caixa rotulada.
caixa = "Conteúdo"

# Valores das variáveis - Os valores das variáveis podem ser alterados a qualquer momento. Podemos alterar o valor de uma variável quantas vezes quisermos. O Python sempre usa o valor mais recente que armazenamos na variável.

# As variáveis podem conter todos os tipos de valores. Vamos dar uma olhada no armazenamento de valores de texto (string).

# Os valores de cadeia de caracteres são texto entre aspas duplas ou simples chamados strings.
equipe_de_futebol = "Vasco da Gama"

# A utilização do tipo de aspas depende do que queremos armazenar na variável. Por exemplo, se quisermos armazenar uma string que contenha aspas, usamos aspas simples para envolver a string e aspas duplas para envolver a citação dentro dea e vice versa. Caso isso não seja feito, o Python não saberá onde a string termina e gerará um erro.
citacao = "O técnico disse: 'Vamos vencer!'"

# Uma forma de contornar esse problema é usar uma barra invertida (\), que é um caractere de escape antes da aspas que queremos armazenar na string. Porém isso pode ser um pouco confuso.
citacao = 'O técnico disse: \'Vamos vencer!\''  # Dessa forma, o Python sabe que a aspas simples não é o fim da string.

# É importante manter o padrão de uso no programa. Escolhemos um tipo e o usamos em todo o programa.

# As strings podem conter todos os tipos de letras e símbolos, incluindo espaços
exemplo_string = 'Pode conter letras, números (1, 2, 3) e caracteres especiais (@, #, $)'

# Console - Exibindo valores

# Linhas de código são instruções para o computador seguir.
# Quando executamos código, dizemos ao computador para seguir as instruções que montamos.
# A ordem das instruções é importante porque o computador segue as instruções, linha por linha.
# Com a instrução especial print(), dizemos ao computador para exibir um valor em uma área chamada console, também conhecida como shell.

# Podemos usar a instrução quantas vezes quisermos. O computador exibe cada valor em uma nova linha no console.
# print() - Exibe o valor entre os parênteses no console
print('Essa instrução irá aparecer primeiro!') 
print('E essa em seguida, em ordem.')

# Podemos usar para exibir variáveis também - print(variavel) - Quando exibimos variáveis no console, seus valores aparecem em vez de seus nomes.
nome = 'Maycon'
print(nome)  # Estamos dizendo - Mostre o que há dentro da caixa nome
