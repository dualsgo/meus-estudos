# MIMO - 04 - Loops - Desafio 3
# Escrevemos uma instrução print() para nos informar que o programa entrou no loop. No entanto, o programa entrou no loop infinito, conserte-o antes que ele trave nosso computador!

# Tarefa 1: No loop while, altere o valor da variável loop para que "Entered the loop!" seja impresso apenas uma vez

loop = True
while loop:
    print("Entrando no loop")
    loop = False
print('Loop encerrado!')