# MIMO - Funções

# Funções são blocos de código que agrupam instruções relacionadas e permitem executar tarefas em um só lugar.

# Para definir uma função, usamos a palavra-chave 'def', seguida do nome da função e parênteses. O nome da função segue algumas regras:
# - Deve começar com uma letra.
# - Pode conter letras, números e underscores.
# - Deve ser seguido por dois pontos, que marcam o início de um bloco de código.
# - A indentação define o código pertencente à função.

def exemplo():
    print('Eu faço parte da função!')


print('Eu não faço parte da função.')

# Observe que a função é executada apenas quando chamada. Isso é feito digitando seu nome seguido por parênteses.
exemplo()

# Parâmetros

# Para passar valores para uma função, definimos parâmetros dentro dos parênteses. Esses parâmetros são variáveis que armazenam os valores que serão passados quando a função for chamada.


def saudacao(nome):
    print(f'Olá, {nome}!')


saudacao('Douglas')

# Podemos passar diferentes valores para a função chamando-a com argumentos diferentes.
saudacao('Maycon')

# Retornando Valores (return) - Funções são criadas para realizar tarefas e, às vezes, precisamos obter o resultado dessas tarefas.

# Para retornar um valor de uma função, usamos a palavra-chave 'return', seguida do valor a ser retornado. O valor retornado pode ser de qualquer tipo, e chamamos esse valor de "saída da função".


def soma(a, b):
    resultado = a + b
    return resultado


# Chamamos a função 'soma' com dois argumentos e recebemos o valor retornado.
total = soma(5, 3)
print(f'A soma é: {total}')

# O valor retornado pode ser usado de várias maneiras, como atribuir a uma variável ou imprimir diretamente.
