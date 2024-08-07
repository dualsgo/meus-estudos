# MIMO - 08 - Funções
# 08.1 - Reutilizando códigos com funções

# Programas precisam executar regularmente a mesma tarefa continuamente. Em vez de reescrever o mesmo código, podemos usar funções para agrupar código relacionados e executar a tarefa em um só lugar.

# Para começar a grupar o código relacionado, começamos a definir uma função com a palavra-chave def.
# def significa definir, ou seja, estamos definindo uma função.

# Em seguida vem o nome da função, em snake_case seguido de parênteses.
# E para finalizar a declaração que inicia o bloco de código, colocamos dois pontos.
# Para agrupar o bloco de código da função, usamos o recuo. O recuo é um espaço em branco no início de uma linha de código. O recuo é importante em Python, pois indica que o código recuado faz parte do bloco de código anterior.
def funcao():
    print('Código que será executado.')

# Para executar o código, precisamos chamar a função. Fazemos isso codificando seu nome seguido de parÊnteses
funcao()


# As funções podem executar qualquer código que quisermos. Podemos adicionar quantas linhas de código quisermos dentro da função.