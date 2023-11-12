# MIMO - Loops For vs. Loops While

# Loop For:
# Para criar um loop for, usamos a palavra-chave 'for', uma variável de contador como 'i', seguida da palavra 'in' e, por fim, a função 'range()' com seu parâmetro.

print("Loop For:")
for i in range(1):
    print(i)

# A função 'range()' especifica quantas vezes queremos que o nosso loop seja executado. Como começa no índice 0, ele terá duas execuções e irá exibir 0 e 1.

##################################### PARA EFEITO DE COMPARAÇÃO ########################################

# Loop While:
# Para criar um loop while, usamos a palavra-chave 'while' seguida de uma condição que deve ser True para que o loop continue.

print("\nLoop While:")
i = 0  # Inicializamos a variável de contador 'i' com 0
while i < 2:  # Enquanto 'i' for menor que 2...
    print(i)
    i += 1  # Incrementamos 'i' para controlar o loop.

# Ambos os loops produzem a mesma saída, exibindo 0 e 1.
