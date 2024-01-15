# PE1: Módulo 1. Introdução à programação de computadores e Python

# 1.1.1 Como funciona um programa de computador?

# Podemos dizer que cada linguagem (máquina ou natural, não importa) consiste nos seguintes elementos:

# um alfabeto: um conjunto de símbolos que podem ser usados para construir palavras. O "alfabeto" é um conjunto padronizado de símbolos gráficos (letras) usado para representar os sons de uma língua. Cada língua pode ter seu próprio alfabeto, com um conjunto específico de letras e caracteres. O alfabeto é a base da escrita em muitas línguas e é essencial para a comunicação escrita.

# uma lexis: um conjunto de palavras que podem ser usadas para construir frases. "Lexis" refere-se ao vocabulário ou ao conjunto de palavras em uma língua ou em um contexto específico. Envolve todas as palavras, expressões e termos que fazem parte do léxico de uma língua ou de uma área de conhecimento. A análise do lexis inclui o estudo da semântica, colocações e usos específicos das palavras em diferentes contextos.

# uma sintaxe: um conjunto de regras que definem como as palavras podem ser combinadas para formar frases. A sintaxe refere-se à estrutura ou às regras gramaticais de uma linguagem. Na linguagem natural, isso se relaciona à organização das palavras e frases para formar sentenças gramaticalmente corretas. Em programação, a sintaxe está relacionada à estrutura e às regras de construção de código fonte em uma linguagem de programação específica. Violando a sintaxe de uma linguagem resultará em erros de compilação ou interpretação

# semântica: um conjunto de regras que definem o significado das frases. A semântica refere-se ao significado das palavras, frases ou instruções em uma linguagem. Na linguagem natural, a semântica lida com o significado das palavras e como elas se relacionam umas com as outras. Em programação, a semântica está relacionada ao significado das instruções e estruturas de controle no código fonte. Mesmo que o código tenha uma sintaxe correta, erros semânticos podem ocorrer se o significado das instruções não estiver de acordo com a lógica pretendida.


# Computadores possuem sua própria linguagem, chamada linguagem de máquina e um conjunto completo de comandos conhecidos como lista de instruçõesm ou IL. A linguagem de máquina é uma linguagem de baixo nível, que é composta por instruções binárias (0s e 1s) que podem ser executadas diretamente pelo processador. A lista de instruções é um conjunto de instruções que podem ser executadas diretamente pelo processador. Cada instrução é representada por um código binário específico. Por exemplo, o código binário 0000 0001 pode representar a instrução "carregar o valor 1 no registrador A". A lista de instruções é específica para cada arquitetura de processador e é definida pelo fabricante do processador.

# A linguagem de máquina é difícil de ser lida e compreendida por humanos. Por isso, os programadores usam linguagens de programação de alto nível, que são mais fáceis de serem lidas e compreendidas. Essas linguagens são chamadas de linguagens de programação de alto nível porque são mais próximas da linguagem natural. Elas são mais fáceis de serem lidas e compreendidas por humanos, mas não podem ser executadas diretamente pelo processador. Por isso, precisam ser traduzidas para a linguagem de máquina antes de serem executadas. Essa tradução é feita por um programa chamado compilador ou interpretador.

# A programação de computadores é o ato de compor os elementos da linguagem de programação selecionada na ordem que causará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, do conhecimento e da experiência do programador. 

# Obviamente, essa composição precisa ser correta em muitos sentidos:

# em ordem alfabética - um programa precisa ser escrito em um script reconhecível, ou seja, em uma linguagem de programação específica;

# lexicamente - cada linguagem de programação tem seu dicionário e você precisa dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer linguagem natural;

# sintaticamente - cada idioma tem suas regras e elas devem ser obedecidas;

# semanticamente - o programa tem que fazer sentido. 

# Há duas maneiras diferentes de transformar um programa de uma linguagem de programação de alto nível em linguagem de máquina:


# Na compilação, o código-fonte é traduzido integralmente para linguagem de máquina ou código intermediário por um programa chamado compilador. O compilador examina todo o código-fonte e produz um arquivo executável ou código objeto.
# Execução: O código compilado pode ser executado várias vezes sem a necessidade de recompilar, a menos que haja modificações no código-fonte. Durante a execução, o código compilado interage diretamente com o hardware do computador, resultando frequentemente em uma execução mais eficiente.

# Na interpretação, o código-fonte é executado linha por linha por um programa chamado interpretador. Não há um estágio de compilação antecipado, e o código-fonte é traduzido e executado sob demanda. 
# Execução: O código-fonte é traduzido e executado cada vez que o programa é executado. Isso significa que a execução pode ser mais lenta em comparação com a compilação, pois a tradução ocorre em tempo real. No entanto, a interpretação pode ser mais flexível e adaptável a mudanças no código-fonte.

# O interpretador é responsável por ler e processar o código-fonte de um programa, que geralmente está armazenado em um arquivo de texto. Ele verifica a correção das linhas do código, identificando eventuais erros. Se um erro é encontrado, o interpretador encerra imediatamente e fornece uma mensagem de erro indicando a localização e a natureza do problema. O processo de interpretação segue a leitura, verificação e execução de cada linha separadamente. O interpretador pode detectar erros apenas no momento em que tenta executar uma parte específica do código, o que pode resultar em mensagens de erro que não refletem necessariamente a verdadeira origem do problema. Comparando com o modelo de compilação, não há uma resposta clara sobre qual modelo é melhor, pois ambos têm vantagens e desvantagens. A interpretação é mais lenta, mas mais flexível e adaptável a mudanças no código-fonte. A compilação é mais rápida, mas menos flexível e adaptável a mudanças no código-fonte.