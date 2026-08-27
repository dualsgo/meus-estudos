# MIMO - 03 - Declarações Condicionais - DESAFIO 1
# Imprimiremos o número de notificações lidas ou não lidas que um usuário recebeu.

lidas = 5
nao_lidas = 4

# Tarefa 1: Se unread não for 0, imprima "Você tem {nao_lidas} mensagens não lidas". Use f-string para exibir o valor de unread dentro de string

if nao_lidas != 0:
    print(f'Você tem {nao_lidas} mensagens não lidas.')

# Tarefa 2: Caso contrário, imprima "Sem novas mensagens. Verifique suas {lidas} mensagens lidas"
else:
    print(f'Sem novas mensagens. Verifique suas {lidas} mensagens lidas.')