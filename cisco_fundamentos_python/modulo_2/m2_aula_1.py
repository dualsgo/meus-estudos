# PE1: Módulo 1. Introdução à programação de computadores e Python


print('Olá mundo!')
# Como você pode ver, este primeiro programa consiste nas seguintes partes:

# a palavra print
# um parênteses de abertura e fechamento
# uma linha de texto: Olá, Mundo!; entre os parênteses
# um par de aspas envolvendo o texto.

# Cada uma das opções acima desempenha um papel muito importante no código.

# A palavra chave print é um comando que instrui o interpretador a exibir um texto na tela. O interpretador Python sabe que print é um comando porque é uma palavra reservada da linguagem Python.

# Os parênteses de abertura e fechamento são usados para executar uma função. Uma função é um conjunto de instruções que executa uma tarefa específica. A função print() exibe um texto na tela.

# O texto que você deseja exibir na tela é chamado de argumento da função. O argumento é o valor que a função usa para executar sua tarefa. No caso da função print(), o argumento é o texto que você deseja exibir na tela. O argumento é colocado entre os parênteses de abertura e fechamento.

# Utilizamos os parênteses para envolver o texto que queremos exibir na tela. Isso é necessário porque o interpretador Python precisa saber onde o texto começa e onde termina. O interpretador Python sabe que o texto começa e termina onde os parênteses de abertura e fechamento estão localizados. O texto é chamado de string. Uma string é um conjunto de caracteres que podem ser letras, números, símbolos ou espaços. Uma string é sempre colocada entre aspas simples ou duplas, dependendo do contexto

# Uma função nesse contexto é uma parte separada do código capaz de:

# Causar algum efeito (por exemplo, exibir um texto na tela)
# Avaliar um valor (por exemplo, calcular uma soma)
# Retornar um valor (por exemplo, retornar o resultado de uma soma)

# As funções podem vir:
# Do prórprio Python (como a função print()) que é chamada de função interna pois já vem com o Python e não é necessário instalar nada para usá-la.
# De bibliotecas externas (como a função sqrt() da biblioteca math) que é chamada de função externa pois é necessário instalar a biblioteca para usá-la.
# Do seu próprio código (como a função soma()) que é chamada de função definida pelo usuário pois você mesmo a criou definindo o que ela deve fazer com a palavra chave def e sua sintaxe.

# Ao escrever suas próprias funções, devemos dar a elas nomes significativos que deixam claro o que elas fazem. Por exemplo, se você escrever uma função que exibe um texto na tela, você pode chamá-la de exibe_texto().

# 2.1.3 Argumentos de função
# Como dissemos antes, uma função pode ter:
# um efeito;
# um resultado.

# Há também um terceiro compontente que pode ser usado para modificar o comportamento de uma função: o argumento.
# As funções matemáticas geralmente levam um argumento. Por exemplo, sin(x) leva um x, que é a medida de um ângulo.

# As funções Python, por outro lado, são mais versáteis. Dependendo das necessidades individuais, eles podem aceitar qualquer número de argumentos ‒ quantos forem necessários para realizar suas tarefas. Nota: quando dizemos qualquer número, que inclui zero ‒ algumas funções do Python não necessitam de argumento.

# Apesar do número de argumentos necessários/fornecidos, as funções do Python exigem fortemente a presença de um par de parênteses ‒ abrindo e fechando, respectivamente. Se desejamos passar mais de um argumento para uma função, devemos separá-los com uma vírgula.


# Cadeia de caracteres como o argumento da função print()
# O único argumento entregue à função print() neste exemplo é uma string:
print("Olá Mundo!")

# Como você pode ver, a string é delimitada por aspas - na verdade, as aspas formam a string - elas cortam uma parte do código e atribuem um significado diferente a ele. Você pode imaginar que as citações dizem algo como: o texto entre nós não é código. Não se destina a ser executado e você deve tomá-lo como está. Quase tudo o que você coloca dentro das aspas será levado literalmente, não como código, mas como dados. 

# 2.1.4 Chamada de função
# O nome da função (print neste caso), juntamente com os parênteses e os argumento(s), formam a invocação da função.

# O que acontece quando o Python encontra uma invocação como esta abaixo?
# function_name(argument)

# Primeiro, o Python verifica se o nome especificado é legal (ele navega em seus dados internos para encontrar uma função atual do nome; se essa pesquisa falhar, o Python anula o código)
# segundo, o Python verifica se os requisitos da função para o número de argumentos permitem que você chame a função dessa maneira (por exemplo, se uma função específica exigir exatamente dois argumentos, qualquer invocação que forneça apenas um argumento será considerada errônea e abortará os execução) a menos que o argumento seja opcional;
# terceiro, o Python deixa seu código por um momento e salta para a função que você deseja chamar; é claro, ele também usa seus argumentos e os passa para a função;
# quarto, a função executa seu código, causa o efeito desejado (se houver), avalia o (s) resultado (s) desejado (s) (se houver) e termina sua tarefa;
# por fim, o Python retorna ao seu código (para o local imediatamente após a invocação) e retoma a execução.


# 2.1.7 Instruções

# o programa chama a função print() duas vezes, e você pode ver duas linhas separadas no console ‒ isso significa que print() começa sua saída a partir de uma nova linha cada vez que inicia sua execução; você pode mudar esse comportamento, mas também pode usá-lo a seu favor;

# cada invocação print() contém uma string diferente, como seu argumento, e o conteúdo do console a reflete ‒ isso significa que as instruções no código são executadas na mesma ordem em que foram colocadas no arquivo fonte; nenhuma instrução subseqüente é executada até que a anterior seja concluída (existem algumas exceções a esta regra, mas você pode ignorá-las por enquanto.)

# A sintaxe do Python é bastante específica nessa área. Ao contrário da maioria das linguagens de programação, o Python exige que não haja mais de uma instrução em uma linha apesar de ser possível utilizando vírgulas ou ponto e vírgulas.
# Uma linha pode estar vazia (ou seja, pode não conter nenhuma instrução), mas não deve conter duas, três ou mais instruções.

# Por exemplo, o código abaixo é válido, mas não é recomendado:

print("A pequenina aranha escalou a tromba d'água."), print("Caiu a chuva e lavou a aranha.")

# Como dito, funções podem receber qualquer número de argumentos. O código abaixo é válido, mas também não é recomendado:
print("A pequenina aranha escalou a tromba d'água.")
print()  # Essa instrução imprime uma linha em branco pois esse efeito é causado pelo argumento padrão da função print() chamado end que por padrão é \n (caractere de nova linha)
print("Caiu a chuva e lavou a aranha.")

# 2.1.8 Escape do Python e caracteres de novas linhas

print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")

# Curiosamente, enquanto você pode ver dois caracteres, o Python vê um.
# A barra invertida (\) tem um significado muito especial quando usada dentro de strings – isso é chamadode caractere de escape. A letra n colocada após a barra invertida vem da palavra newline (nova linha).

# Esta convenção tem duas consequências importantes:

# 1. Se você quiser colocar apenas uma barra invertida dentro de uma string, não se esqueça de sua natureza de escape - você precisa dobrá-la. Por exemplo, uma invocação como esta causará um erro:
# print("\")

print("\\") # enquanto este não vai

# 2. Nem todos os pares de escape (a barra invertida juntamente com outro caractere) significam algo.


# 2.1.9 Usando vários argumentos
# Há uma chamada de função print(), mas ela contém três argumentos. Todos eles são cadeias de caracteres.

print("A aranha pequenininha" , "subiu" , "a tromba d'água.")

# Os argumentos são separados por vírgulas. Nós os cercamos de espaços para torná-los mais visíveis, mas não é realmente necessário, e não faremos mais isso.

# Nesse caso, as vírgulas que separam os argumentos desempenham uma função completamente diferente da vírgula dentro da sequência. O primeiro faz parte da sintaxe do Python, enquanto o último deve ser exibido no console.

# Duas conclusões emergem desse exemplo:
# uma função print() chamada com mais de um argumento gera todos eles em uma linha;
# a função print() coloca um espaço entre os argumentos gerados por sua própria iniciativa.

# 2.1.11 Argumentos de palavra-chave

# A função print() tem dois argumentos de palavra-chave que você pode usar para seus propósitos. O primeiro é chamado de end.

# Para usá-lo, é necessário conhecer algumas regras:
# um argumento de palavra-chave consiste em três elementos: uma palavra-chave que identifica o argumento (end aqui); um sinal de igual (=); e um valor atribuído a esse argumento;
# qualquer argumento de palavra-chave deve ser colocado após o último argumento posicional (isso é muito importante)

# O comportamento padrão reflete a situação em que o argumento de palavra-chave end é usado implicitamente da seguinte maneira: end="\n".

# Se o argumento end for definido como nada, a função print() também não gera nada, uma vez que seus argumentos posicionais se esgotam. Nenhum caracter de nova linha será enviado para a saída.

# Dissemos anteriormente que a função print() separa seus argumentos em saída com espaços. Esse comportamento também pode ser alterado.

# O segundo argumento de palavra-chave é chamado de sep. Ele define o caractere usado para separar os argumentos. O valor padrão é um único espaço, mas você pode alterá-lo para qualquer caractere ou sequência de caracteres válidos.

print("Meu", "nome", "é", "Monty", "Python.", sep="-") # O resultado é: Meu-nome-é-Monty-Python.7

# A função print() agora usa um traço, em vez de um espaço, para separar os argumentos de saída.

"""2.1.14 RESUMO DA SEÇÃO
1. A função print() é uma função interna. Ele imprime/envia uma mensagem especificada para a tela/janela do console.

2. As funções incorporadas, ao contrário das funções definidas pelo usuário, estão sempre disponíveis e não precisam ser importadas. O Python 3.8 vem com 69 funções integradas. Você pode encontrar a lista completa fornecida em ordem alfabética na Python Standard Library.

3. Para chamar uma função (este processo é conhecido como chamada de função ou invocação de função), você precisa usar o nome da função seguido de parênteses. Você pode passar argumentos para uma função colocando-os dentro dos parênteses. Você deve separar os argumentos com uma vírgula, por exemplo, print("Olá,", "world!"). Um print() vazio imprime uma linha vazia na tela.

4. Strings no Python são delimitadas por aspas, por exemplo, "eu sou um barbante" (aspas duplas), ou 'eu sou um barbante, demasiado' (aspas simples).

5. Programas de computador são uma coleção de instruções. Uma instrução é um comando para executar uma tarefa específica quando executado, por exemplo, para imprimir uma determinada mensagem na tela.

Vamos ver o que você aprendeu hoje.
6. Em Strings do Python a barra invertida (\) é um caracter especial que anuncia que o próximo caracter terá um significado diferente, por exemplo, \n (o caracter de nova linha) inicia uma nova linha de saída.

7. Argumentos posicionais são aqueles cujo significado é ditado por sua posição, por exemplo, o segundo argumento é gerado após o primeiro, o terceiro é gerado após o segundo, etc.

8. Argumentos de palavras-chave são aqueles cujo significado não é ditado por sua localização, mas por uma palavra especial (palavra-chave) usada para identificá-los.

9. Os parâmetros end e sep podem ser utilizadas para formatar a saída do print(). O parâmetro sep especifica o separador entre os argumentos de saída, por exemplo, print("H", "E", "L", "L", "O", sep="-"), enquanto o parâmetro end especifica o que imprimir no final da impressão.
"""