# Curso Python Aula 13 - Estruturas de repetição while

"""RESUMO"""

# O instrutor começa a seção discutindo a estrutura de repetição introduzida na lição anterior (Lição 13) e sua versatilidade, enfatizando que pode não ser 100% eficaz em todas as situações.

# Introdução ao conceito de um loop e explicação da importância de definir um limite ou condição de parada para o loop.

# Introdução ao uso de uma declaração condicional para controlar o loop.

# Ênfase na importância da prática e destaque de que aprender a usar loops efetivamente leva tempo.

# Introdução ao conceito de loop "while" em Python e sua implementação, incluindo a explicação de que o loop continua a ser executado enquanto a condição fornecida permanece verdadeira.

# Explicação de que o programa pode ser concluído com apenas três linhas.

# Ênfase na importância de entender a posição dos comandos no loop e destaque de como a definição de uma variável pode mudar o comportamento de um loop "while".

# Uso de um exemplo prático envolvendo uma pessoa alcançando uma manga para demonstrar como usar um loop "while".

# Discussão sobre os benefícios do uso de loops "while" em alguns casos, especialmente quando o limite do loop é conhecido e quando o programa requer tomada de decisão complexa e manipulação de variáveis.

# Instruções sobre como usar um loop "while" para realizar tarefas mais complexas e incentivo aos espectadores para praticar e entender melhor a mecânica do loop.

# Explicação de como usar um loop "while" em Python para repetir um bloco de código enquanto uma determinada condição permanece verdadeira.

# Ênfase na importância de definir a condição para o loop e qualquer opção ou condição necessária que deve ser atendida para que o loop continue sendo executado.

# Demonstração de como criar o loop usando a instrução "while" e fornecimento de um exemplo de como ele pode ser usado para executar uma função ou tarefa específica.

# Discussão sobre a criação de um arquivo HTML usando o editor de texto Notepad++, incluindo a definição da estrutura básica de uma página HTML e a adição de um cabeçalho e um título.

# Ênfase na importância de testar o código em vários navegadores para garantir a compatibilidade.

# Introdução ao uso de CSS (Folhas de Estilo em Cascata) para estilizar os elementos HTML e criar uma página visualmente atraente.

# Conclusão do tutorial com a importância do controle de versão usando Git e incentivo aos espectadores para praticar a escrita de código HTML.

# Explicação de como usar um loop "while" em Python para executar um programa repetidamente até que uma condição específica seja atendida.

# Fornecimento de exemplos de como usar loops "while" em diferentes cenários de programação, desde programas simples que repetem uma tarefa até que um valor do usuário seja inserido até programas mais complexos que envolvem análise e manipulação de dados.

# Ênfase na importância de entender o comportamento dos loops "while" e como usá-los corretamente para evitar bugs e criar código eficiente.

# Discussão sobre a criação de um programa que aceita entrada do usuário e avalia a correção da resposta, aceitando apenas 'masculino' ou 'feminino' como entradas válidas para 'sexo' e continuando a solicitar ao usuário até que uma resposta válida seja fornecida usando um loop "while" em Python.

# Lista de exercícios relacionados a este tópico juntamente com os valores esperados e as opções disponíveis, incluindo "desafio 57", que visa melhorar o jogo, e "desafio 28", que trata de um jogo aprimorado com o computador gerando um número aleatório em vez do jogador tentar adivinhar o número.

# Discussão sobre o uso do loop "while" em Python, explicando que ele permite que o programa execute um bloco de código repetidamente enquanto uma determinada condição permanece verdadeira.

# Explicação de que é importante determinar quando parar um loop e calcular a média de todos os valores inseridos pelo usuário.

# Mencionar a necessidade de determinar os maiores e menores valores em um determinado conjunto de dados.

# Ênfase na importância de não copiar o código de outra pessoa, pois é essencial entender a lógica subjacente antes de tentar aplicá-la em um novo contexto.

# Encorajamento aos espectadores para apoiar o criador de conteúdo, como curtir o vídeo, compartilhá-lo e se inscrever no canal.

"""CONTEÚDO"""

# Estrutura de repetição com teste lógico

# Laço while - Repete uma ou mais instruções enquanto uma condição for verdadeira

# Exemplo 1: Repetição usando um contador
contador = 1  # Inicializa o contador com 1
while contador <= 10:  # Enquanto o contador for menor ou igual a 10
    print(f'Contagem: {contador}')  # Imprime a contagem atual
    contador += 1  # Incrementa o contador em 1
print('Fim da contagem')  # Imprime "Fim da contagem" após a repetição

# Exemplo 2: Verificação de paridade usando um loop while
numero = 1  # Inicializa o número com 1
par = 0  # Inicializa a contagem de números pares
impar = 0  # Inicializa a contagem de números ímpares
while numero <= 10:  # Enquanto o número for menor ou igual a 10
    if numero % 2 == 0:  # Verifica se o número é par
        par += 1  # Incrementa a contagem de pares
    else:
        impar += 1  # Incrementa a contagem de ímpares
    numero += 1  # Incrementa o número em 1
print(f'Ao todo temos {par} pares e {impar} ímpares')  # Imprime o resultado

# Exemplo 3: Contagem regressiva
contagem_regressiva = 10  # Inicializa a contagem regressiva em 10
while contagem_regressiva >= 1:  # Enquanto a contagem regressiva for maior ou igual a 1
    print(contagem_regressiva)  # Imprime a contagem regressiva atual
    contagem_regressiva -= 1  # Decrementa a contagem regressiva em 1

# Exemplo 4: Entrada de valores e iteração personalizada
inicio = int(input('Início: '))  # Solicita ao usuário um valor de início
fim = int(input('Fim: '))  # Solicita ao usuário um valor de fim
iteracao = int(input('Iteração: '))  # Solicita ao usuário um valor de iteração
lista = []  # Inicializa uma lista vazia
soma = 0  # Inicializa a variável soma em 0
c = inicio  # Inicializa a variável 'c' com o valor de início
while c <= fim:  # Enquanto 'c' for menor ou igual ao valor de fim
    print(c, end=', ')  # Imprime 'c' separado por vírgula (end=', ')
    if c % 2 == 0:  # Verifica se 'c' é par
        lista.append(c)  # Adiciona 'c' à lista de números pares
    soma += c  # Incrementa 'c' na soma
    c += iteracao  # Incrementa 'c' com o valor de iteração
print(f'Soma: {soma}')  # Imprime a soma
print(f'Números pares na lista: {lista}')  # Imprime a lista de números pares
