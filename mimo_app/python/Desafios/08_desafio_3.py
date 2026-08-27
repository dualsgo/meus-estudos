# MIMO - 08 - Funções - Desafio 3
# É seu aniversário e seus amigos decidiram presentear você com algum dinheiro. Eles colocaram o dinheiro em uma jarra e deram para você.

# Tarefa 1: Atualize a função calculate_total para iterar todas as quantias no jarro, somá-las e retornar a sum total.

def total(cofre):
    soma = 0

    for dinheiro in cofre:
        print(f'R$ {dinheiro:.2f}')
        soma += dinheiro
    print('Finalizado!')
    return soma


economias = [1, 2, 3, 4]
print(total(economias))
