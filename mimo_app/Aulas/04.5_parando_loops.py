# MIMO - 04 - Loops

# 4.4 - Parando loops for

# Usando loops for, podemos escrever programas com muito menos código e facilitar o entendimento de outros programadores.

# Para criar um loop for, adicionamos a palavra-chave for, uma variável como i ou qualquer outro nome, a palavra in e, finalmente range() - for i in range():

# Em um loop for, podemos especificar quantas vezes gostaríamos que nosso loop fosse executado com a instrução range() intervalo.

# Adicionar um número como 6, dentro de range() significa que ele fará uma iteração sobre o bloco de código 6 vezes (0 a 5) pois a contagem começa em 0 que é o primeiro número de índice.

# O loop for também repete seu bloco de código enquanto a condição for True
for i in range(6):  # O range() é o argumento de parada do loop for. Nesse caso, o loop for irá de 0 a 5
    print(i)

# A variável antes de in, nesse caso, i, é a variável de contador. Conta em que iteração o loop está.

# A mesma contagem utilizando while seria:

i = 0  # A variável de contador é definida antes do loop
while i < 6: # O loop while repete seu bloco de código enquanto a condição for True
    print(i)  