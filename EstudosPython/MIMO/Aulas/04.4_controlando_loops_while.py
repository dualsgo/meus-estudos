# MIMO - 04 - Loops

# 4.4 - Controlando loops while

# Vamos nos aprofundar no controle dos tempos em que um loop while repete seu código.
# Para controlar o tempo de repetição de um loop while, começamos com uma variável definida com um número. Chamamos essa variável de contador.
contador = 1

# Em seguida, usamos uma comparação na condição para comparar a variável de contador com um número.

# Dentro do bloco de código, fazemos a condição retornar False e paramos o loop incrementando a variável de contador.

# Neste caso usamos += e aumentamos o valor da variável em 1 cada vez que o loop é executado.

while contador < 4:
    print(f' {contador} - Agora temos um limite de repetições')
    contador += 1

# Alterar o valor da variável de contador muda quando o loop é iniciado.
# Alterar a condição informa ao loop quando parar.

# A ordem do código afeta o que o console exibe! Se colocar o incremento antes do print pro exemplo