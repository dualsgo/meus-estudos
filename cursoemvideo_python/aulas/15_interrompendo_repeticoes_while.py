# Curso Python #15 - Interrompendo repetições while

"""RESUMO"""
# O instrutor discute o conteúdo da lição, que aborda a interrupção de repetições "while" em Python, com foco na validação de números de CPF em um cenário do mundo real.

# O instrutor destaca que existem dois tipos de programadores: aqueles que verdadeiramente aprenderam a programar e aqueles que acreditam que sabem, mas não sabem. Ele aconselha os espectadores a aplicar os conceitos demonstrados no vídeo em vez de simplesmente copiar e colar soluções.

# Ênfase na importância da Educação Continuada e Desenvolvimento Profissional.

# Explicação dos conceitos de repetição e loops em Python.

# Demonstração do uso de um loop "enquanto" para repetir um bloco de código até que uma determinada condição seja atendida.

# Exemplo de repetição com um loop "enquanto", onde o bloco de código continua repetindo até que a condição "while isso é verdade" não seja mais verdadeira.

# Explicação do teste de condição, que é usado para determinar se um bloco de código deve ser executado ou não.

# Demonstração do uso de uma variável, onde eles atribuem e manipulam o valor da variável para realizar ações específicas.

# Explicação de como usar o comando "break" em Python para interromper um loop.

# Uso do exemplo de um loop "infinito" que é executado indefinidamente até encontrar uma condição específica.

# Destaque de que esse comando é útil para sair de um loop que está causando problemas ou levando muito tempo para ser executado.

# Demonstração de como usar o comando "break" em um exemplo simples, usando a função "input" para ler a entrada de um usuário e sair do loop antecipadamente se a entrada for um valor específico.

# Demonstração de como usar um loop "enquanto" em Python para repetidamente pedir um número até que ele seja diferente de um valor específico, neste caso, 999.

# Explicação da importância da interrupção de repetições durante a programação e demonstração de como fazer isso usando o comando "break" dentro do loop para parar o loop quando a condição desejada é atendida.

# Discussão do conceito de uma "bandeira" ou "ponto de interrupção" para interromper um loop, o que pode ser usado para evitar um loop infinito.

# Explicação de como usar o comando "break" em Python enquanto itera por uma lista e verifica se um determinado elemento é encontrado.

# Destaque de que esse comando permite sair do loop antes do término da execução quando um elemento específico é encontrado.

# Breve menção a uma atualização da linguagem Python em 2017, conhecida como Python 3.6.3, que adicionou um novo recurso chamado "f-strings." Esse recurso é útil para simplificar a escrita de determinados tipos de código, mas pode não ser suportado por todos os sistemas.

# Discussão sobre o uso do Python 2 e 3, com foco na versão 3.6. Recomendação geral para usar a versão 3.6 ou a versão mais recente do Python 3, em vez da versão 2.

# Demonstração de como usar interpolação em Python e f-strings para formatar e imprimir a saída com formatação precisa, incluindo a capacidade de alinhar o texto.

# Uso de um loop com um limite móvel e o comando "break" e ênfase na importância da aplicação prática.

# Discussão de um desafio de programação onde o programa deve ser encerrado quando um valor de entrada for negativo.

# O desafio envolve iniciar com um valor de 67, exibir uma tabela de quadrados de números e permitir que o usuário clique em valores específicos para exibir informações relacionadas.

# O programa deve ter várias opções para exibir a tabela.

# Discussão sobre a importância da prática na aprendizagem da programação e enfatiza que não é apenas o exame final que importa, mas também o esforço acumulado de trabalhar nos exercícios anteriores.

# Anúncio do próximo mundo do curso, que se concentrará em estruturas de dados e rotinas.

# Introdução do tópico do vídeo, que é um curso de Python de nível intermediário. O curso abrange uma variedade de tópicos, incluindo coleções como listas e dicionários, bem como tuplas.

# Ênfase na importância de entender as diferentes características e funções dessas coleções e incentivo aos espectadores para praticar e experimentar completando os exercícios do curso.

"""CONTEÚDO"""


# Laço while - Repete uma ou mais instruções enquanto uma condição for verdadeira

# Exemplo 1: Repetição usando um contador
contador = 1  # Inicializa o contador com 1
while contador <= 10:  # Enquanto o contador for menor ou igual a 10
    print(f'Contagem: {contador}')  # Imprime a contagem atual
    contador += 1  # Incrementa o contador em 1
    if contador == 5:  # Verifica se o contador chegou a 5
        print('Contador atingiu 5. Encerrando a contagem.')
        break  # O comando 'break' encerra o loop imediatamente
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
    if impar == 3:  # Verifica se já encontramos 3 números ímpares
        print('Encontramos 3 números ímpares. Encerrando a contagem.')
        break  # O comando 'break' encerra o loop imediatamente
print(f'Ao todo temos {par} pares e {impar} ímpares')  # Imprime o resultado

# Exemplo 3: Contagem regressiva
contagem_regressiva = 10  # Inicializa a contagem regressiva em 10
while contagem_regressiva >= 1:  # Enquanto a contagem regressiva for maior ou igual a 1
    print(contagem_regressiva)  # Imprime a contagem regressiva atual
    contagem_regressiva -= 1  # Decrementa a contagem regressiva em 1
    if contagem_regressiva == 5:  # Verifica se a contagem regressiva chegou a 5
        print('Contagem regressiva atingiu 5. Encerrando a contagem regressiva.')
        break  # O comando 'break' encerra o loop imediatamente

# Exemplo 4: Entrada de valores e iteração personalizada
inicio = int(input('Início: '))  # Solicita ao usuário um valor de início
fim = int(input('Fim: ')) # Solicita ao usuário um valor de fim
iteracao = int(input('Iteração: ')) # Solicita ao usuário um valor de iteração
lista = []  # Inicializa uma lista vazia
soma = 0  # Inicializa a variável soma em 0
c = inicio  # Inicializa a variável 'c' com o valor de início
while c <= fim:  # Enquanto 'c' for menor ou igual ao valor de fim
    print(c, end=', ')  # Imprime 'c' separado por vírgula (end=', ')
    if c % 2 == 0:  # Verifica se 'c' é par
        lista.append(c)  # Adiciona 'c' à lista de números pares
    soma += c  # Incrementa 'c' na soma
    c += iteracao  # Incrementa 'c' com o valor de iteração
    if c >= 20:  # Verifica se 'c' ultrapassou 20
        print('O valor de c ultrapassou 20. Encerrando o loop.')
        break  # O comando 'break' encerra o loop imediatamente
print(f'Soma: {soma}')  # Imprime a soma
print(f'Números pares na lista: {lista}')  # Imprime a lista de números pares
