# MIMO - 08 - Funções - Desafio 2
# Você vai dar um mergulho rápido na piscina, mas não suporta água fria. Vamos ter certeza de que a temperatura da água é adequada para nadar!

# Tarefa 1: Dentro da função, escreva uma instrução if else para verificar a temperatura da água. Se a temperatura estiver acima de 30, retorne True. Caso contrário, retorne False.

def can_swim(temperature):
    if temperature > 30:
        return True
    else:
        return False

print(can_swim(40))
