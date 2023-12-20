# MIMO - Loops While

# Um loop while repete seu bloco de código enquanto a sua condição for atendida (True).

# Se o loop não for parado, ele irá se repetir indefinidamente ou até que o programa apresente um erro de execução. Para parar um loop, começamos com uma variável fora dele.

variavel_de_controle = True

# Usamos a variável na condição para decidir se o loop deve ou não executar seu bloco de código.
while variavel_de_controle:  # Enquanto a variável de controle for True...
    print(variavel_de_controle)
    # Dentro do bloco de código, paramos o loop definindo a variável como False.
    variavel_de_controle = False
    # O loop executará todo o seu bloco de código uma vez, pois no início a variável é definida como True, mas seu valor é atualizado e na próxima execução o valor será False.

# Controlando Loops
# Podemos controlar o número de repetições de um loop while. Começamos com uma variável definida com um número e a chamamos de variável contador.

c = 1  # Aqui, a contagem começa com 1.

# Em seguida, usamos uma comparação na condição para comparar a variável contador com um número.

while c < 4:  # Enquanto a variável de contador for menor que 4...
    print(c)   # Mostre o valor da variável.
    c += 1     # E atualize o valor incrementando 1 a cada repetição.

# Isso exibirá a contagem de 1 até 3, atendendo à condição c < 4.
