# Curso Python Aula 13 - Estruturas de repetição for

"""RESUMO"""

# O professor começa uma nova parte do curso de Python, que se concentra em estruturas de repetição (loops).

# Introdução ao conceito de loops e repetição versus controle e interação na terceira parte do curso de Python.

# Explicação do conceito de loop "for" em Python, que é usado para repetir um conjunto de comandos um número específico de vezes, determinado pelo valor de uma variável.

# Descrição da sintaxe de um loop "for", que envolve o uso de uma variável para armazenar o valor do item a ser repetido e uma estrutura de controle de loop para especificar quantas vezes o loop deve ser executado.

# Exemplo do uso de um loop "for" para contar de 1 a 10, demonstrando o loop externo e o loop interno que realiza a operação desejada em cada item.

# Ênfase na importância de decompor um problema em etapas pequenas e gerenciáveis e usar loops para automatizar tarefas repetitivas.

# Introdução ao conceito de estruturas condicionais em Python e sua utilidade além do Python.

# Explicação de que as estruturas condicionais são um bloco de construção para muitos outros conceitos de programação e que é importante para iniciantes entender como elas funcionam, mesmo que ainda não saibam usá-las efetivamente.

# Exemplo do uso de estruturas condicionais para criar uma relação entre a sintaxe do Python e a sintaxe de programação usada na Geração de Algoritmos.

# Solicitação ao espectador para adicionar uma etapa ao seu próprio guia de prática para consolidar a compreensão do tópico.

# Discussão sobre a implementação de um loop em Python para contar de zero até um número dado.

# Explicação da sintaxe do loop "for" em Python, incluindo "for i in range(início, fim, passo): bloco de código", onde "início" é o valor de início, "fim" é o valor de parada (exclusivo) e "passo" é o valor para incremento ou decremento em cada iteração.

# Explicação de que se "fim" não for especificado, ele será padrão para o "fim do intervalo", e o último valor no intervalo será ignorado.

# Exemplos de como usar o loop "for" para contar de zero a sete e de zero a dez.

# Visão geral dos conceitos abordados na seção anterior, enfatizando a importância do uso da repetição na programação.

# Anúncio do primeiro exercício da série: criar um programa que exibe uma contagem regressiva a partir de um número dado. O exercício envolve o uso de um loop "for" e a implementação de uma pausa entre cada elemento na sequência.

# Ênfase na necessidade de praticar e criar soluções por conta própria, evitando copiar recursos da internet. Sugestão de verificar os resultados e entender a lógica por trás do código.

# Discussão sobre conceitos de programação relacionados a loops e repetição em Python, abrangendo tópicos como loops "for" e "while", bem como a importância de considerar a indexação e a iteração.

# Menção a vários desafios e exercícios de programação relacionados à repetição e iteração, como encontrar o termo de ordem "n" de uma sequência e identificar números primos e palíndromos.

# Discussão sobre a experiência recente do produtor de conteúdo de produzir conteúdo para alguém em uma base semanal ou diária, destacando a duração de 8 semanas e a espera por mais instruções.

# Lembrete de que, apesar das dificuldades de trabalhar em algo novo, é importante continuar estudando, praticando e buscando melhorias.

# Ênfase na importância contínua de estudar e praticar, com destaque para essa prática como parte crucial do negócio.

"""CONTEÚDO"""

# Laço for - Repete uma ou mais instruções um número determinado de vezes

# Exemplo 1: Iterando de 1 a 9
for passo in range(1, 10):
    print(f'Andei {passo}')
    passo += 1  # Incrementa o contador
print('Parei')

# Exemplo 2: Iterando de 0 a 9, verificando se é par ou ímpar
c = 0
for c in range(0, 10):
    if c % 2 == 0:
        print(f'{c} é par.')
    else:
        print(f'{c} é ímpar.')
    c += 1
print('FIM')

# Exemplo 3: Contagem regressiva com iteração personalizada
for c in range(10, 0, -1):
    print(c)  # Contagem regressiva de 10 a 1

# Exemplo 4: Entrada de valores e iteração personalizada
inicio = int(input('Início: '))
fim = int(input('Fim: '))
iteracao = int(input('Iteração: '))
lista = []
soma = 0
for c in range(inicio, fim + 1, iteracao):
    print(c)
    if c % 2 == 0:
        lista.append(c)
    soma += c
print(f'Soma: {soma}')
print(f'Números pares na lista: {lista}')
