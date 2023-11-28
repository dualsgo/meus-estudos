# MIMO - 03 - Declarações Condicionais - DESAFIO 3
# A entrada em determinados estabelecimentos como uma discoteca depende de ultrapassar o limite de idade e de ter reserva. Vamos escrever um programa Python para verificar se uma pessoa pode entrar.

idade = 21
tem_reserva = True
resultado = True

# Tarefa 1: Se idade for igual ou maior a 18 e tem_reserva for True, defina resultado como True
if idade >= 18 and tem_reserva == True:
    # Tarefa 2: Imprimir a saída:
    print(f'Entrada permitida: {resultado}')
