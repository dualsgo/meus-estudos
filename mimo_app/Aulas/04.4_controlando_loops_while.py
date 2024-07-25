# MIMO - 04 - Loops

# 4.4 - Controlando loops while

# Vamos nos aprofundar no controle dos tempos em que um loop while repete seu código.
# Para controlar o tempo de repetição de um loop while, começamos com uma variável definida com um número. Chamamos essa variável de contador.
contador = 1

# Em seguida, usamos uma comparação na condição para comparar a variável de contador com um número.

# Dentro do bloco de código, fazemos a condição retornar False e paramos o loop incrementando a variável de contador.

# Neste caso usamos += e aumentamos o valor da variável em 1 cada vez que o loop é executado.

# O loop while repete seu bloco de código enquanto a condição for True
while contador < 4:
    # Nesse caso, enquanto contador for menor que 4
    print(f'{contador} - Agora temos um limite de repetições')
    contador += 1 # Adicionamos 1 ao contador para atualizá-lo a cada repetição do loop
    

# Alterar o valor da variável de contador muda quando o loop é iniciado.
# Alterar a condição informa ao loop quando parar.

# A ordem do código afeta o que o console exibe! Se colocar o incremento antes do print pro exemplo


contador = 1  
# O loop while repete seu bloco de código enquanto a condição for True
while contador < 4:
    contador += 1  # Adicionamos 1 ao contador para atualizá-lo a cada repetição do loop. Nesse caso o contador é atualizado antes do print, então ele começa em 2 e vai até 4
    print(f'{contador} - Agora temos um limite de repetições') #  O contador irá até o 4 pois o incremento é feito antes do print, sendo assim o print() é executado pois a condição é verificada após o incremento
