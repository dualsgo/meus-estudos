# 3.4.6 LAB Básico de listas
# Cenário

# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

# Sua tarefa é:
# escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
# escreva uma linha de código que remova o último elemento da lista (Etapa 2)
# escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

hat_list = [1, 2, 3, 4, 5]  # Esta é uma lista atual de números ocultos no hat.

# Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário.
hat_list[2] = int(input('Digite um número: '))
# Etapa 2: escreva uma linha de código que remova o último elemento da lista.
hat_list.pop()
# Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual
print(len(hat_list))
print(hat_list)