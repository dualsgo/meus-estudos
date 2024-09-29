# Criar um programa que receba uma quantidade que representará a quantidade de caracteres de uma senha. Mínimo 8 e máximo 16. O programa deverá gerar uma senha aleatória com a quantidade de caracteres informada.

# Para isso, serão sorteados 8 números aleatórios entre 33 e 126, que representam os caracteres da tabela ASCII.
# Os caracteres são: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# Os 8 números sorteados serão gerados a partir de um número binário de 8 bits. Para chegar a este número, sortearemos 8 números aleatórios entre 0 e 1.

# Converteremos esse número binário para decimal e, em seguida, para um caractere da tabela ASCII que será exibido na tela.
from random import randint

def quantidade_caracteres(mensagem):
    # Solicita ao usuário a quantidade de caracteres para a senha aleatória
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            pass


# Inicializa uma lista vazia para armazenar os caracteres gerados
lista_caracteres = list()

# Loop para gerar a quantidade desejada de caracteres
for caractere in range(quantidade_caracteres('Digite a quantidade de caracteres para sua senha aleatória: Min. 8 Max. 16 ')):

    # Inicializa uma lista vazia para armazenar os dígitos binários
    lista_bin = list()

    # Loop para gerar 8 dígitos binários
    while len(lista_bin) < 8:
        # Gera dígitos binários aleatórios (0 ou 1)
        num_bin_sorteado = randint(0, 1)
        lista_bin.append(str(num_bin_sorteado))

    # Converte a lista de dígitos binários para uma string
    lista_editada = ''.join(lista_bin)

    # Converte a string binária para um número inteiro
    numero_valido = int(lista_editada, 2)

    # Verifica se o número está na faixa desejada (48 a 57, 65 a 90, 97 a 122)
    while not ((48 <= numero_valido <= 57) or (65 <= numero_valido <= 90) or (97 <= numero_valido <= 122)):
        # Se o número não estiver na faixa desejada, reinicia o loop
        lista_bin = []
        while len(lista_bin) < 8:
            num_bin_sorteado = randint(0, 1)
            lista_bin.append(str(num_bin_sorteado))

        lista_editada = ''.join(lista_bin)
        numero_valido = int(lista_editada, 2)

    # Converte o número para o caractere correspondente e adiciona à lista
    lista_caracteres.append(chr(numero_valido))

# Imprime a senha gerada na tela
for i in lista_caracteres:
    print(i, end='')


'''

Aqui está a lista completa dos tópicos organizados em ordem:

1. **Comentários em Python**
   - Comentários de linha única com `#`.
   - Strings multilinhas com `"""` usadas como documentação.

2. **Tipos de Dados Primitivos e Operadores**
   - **Números e Operações Matemáticas**: Operadores básicos (+, -, *, /), divisão inteira (//), módulo (%), exponenciação (**).
   - **Valores Booleanos**: `True`, `False`, operadores lógicos (`and`, `or`, `not`), comparação (`==`, `!=`, <, >).
   - **Verificação de Tipos e Valores**: Uso de `is` versus `==`, função `bool()`.

3. **Strings**
   - Criação com `"` ou `'`.
   - Concatenação e formatação (`+`, `f-strings`).
   - Acesso por índice, funções como `len()`.

4. **Variáveis e Coleções**
   - **Variáveis**: Atribuição simples, convenção `snake_case`.
   - **Listas**: Métodos como `append()`, `pop()`, slicing, concatenação, inserção (`insert`), remoção (`remove`).
   - **Tuplas**: Imutáveis, operações básicas, desempacotamento.
   - **Dicionários**: Estrutura chave-valor, métodos (`get`, `setdefault`, `update`), verificação de existência (`in`).
   - **Sets**: Conjuntos, operações de união, interseção, diferença.

5. **Fluxo de Controle e Iteráveis**
   - **Condicionais**: Estruturas `if`, `elif`, `else`, operadores ternários.
   - **Laços**: `for` e `while`, uso de `range()`, `enumerate()`.
   - **Tratamento de Exceções**: Blocos `try`, `except`, `else`, `finally`, uso de `with`.

6. **Leitura e Escrita de Arquivos**
   - Leitura e escrita de strings e JSON em arquivos usando `open()`, `json`.

7. **Iteráveis e Iteradores**
   - Conceito de iteráveis e iteradores.
   - Uso de `iter()`, `next()`, conversão para lista.

8. **Funções**
   - **Definindo Funções**: Uso de `def` para criar funções.
   - **Chamada de Funções**: Argumentos posicionais e nomeados.
   - **Funções com Argumentos Variáveis**: `*args` e `**kwargs`.
   - **Expansão de Argumentos**: Uso de `*` e `**` para desempacotar argumentos ao chamar funções.
   - **Retorno Múltiplo**: Retornando múltiplos valores como tupla.
   - **Escopo**: Variáveis globais e locais, palavra-chave `global`.
   - **Funções de Primeira Classe e Closures**: Funções como objetos, criação de closures, uso de `nonlocal`.
   - **Funções Anônimas (Lambdas)**.
   - **Funções de Alta Ordem**: `map`, `filter`.
   - **Compreensão de Listas, Sets e Dicionários**.

9. **Módulos**
   - **Importação de Módulos**: Uso de `import`, `from ... import`, e alias com `as`.
   - **Exploração de Módulos**: Uso de `dir()` para listar atributos e métodos.
   - **Módulos Personalizados**: Criando e importando seus próprios módulos.

10. **Classes**
    - **Definindo Classes**: Uso de `class`, atributos e métodos de instância.
    - **Métodos Especiais (Dunder Methods)**: `__init__`, `__str__`, `__repr__`.
    - **Métodos de Classe e Métodos Estáticos**: Uso de `@classmethod` e `@staticmethod`.
    - **Propriedades e Encapsulamento**: Uso de `@property`, `setter`, `deleter`.
    - **Verificação de Tipos e Instâncias**: Uso de `isinstance()`, `type()`.

11. **Herança**
    - **Herança Simples**: Classes filhas herdando atributos e métodos da classe pai.
    - **Método `super()`**: Acessando métodos e atributos da classe pai.
    - **Sobrescrita de Métodos**: Modificando métodos herdados.
    - **Checagem de MRO (Method Resolution Order)**: Uso de `__mro__` para ver a ordem de herança.

12. **Herança Múltipla**
    - **Herança de Múltiplas Classes**: Exemplo de uma classe que herda de várias classes.
    - **Conflitos de Métodos e MRO**: Resolução de métodos em herança múltipla.

13. **Tópicos Avançados**
    - **Geradores**: Criação de geradores com `yield`, compreensão de geradores.
    - **Decoradores**: Funções decoradoras para modificar o comportamento de outras funções.
    - **Uso de `functools.wraps`**: Preservando metadados da função original ao usar decoradores.

'''

# iter() e next() são usados para criar e acessar iteradores

# iter() retorna um iterador a partir de um objeto iterável
iterador = iter([1, 2, 3, 4, 5])

# next() retorna o próximo item do iterador
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
print(next(iterador))  # 4
print(next(iterador))  # 5

# next() gera uma exceção StopIteration se não houver mais itens

# são usados em laços for e compreensões de listas:

for i in [1, 2, 3, 4, 5]:
    print(i)

# é equivalente a:

iterador = iter([1, 2, 3, 4, 5])

help(iter)