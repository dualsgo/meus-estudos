# MIMO - 04 - Loops - Desafio 2
# Crie um programa que nos lembre três vezes de parar o bot

# Tarefa 1: Codifique um loop while que imprima "Reminder: Stop the bot!" quando reminder_count for menor que 3.
contagem = 0
while contagem < 3:
# Tarefa 2: Após a instrução print(), aumente o valor de reminder_count em 1
    contagem += 1
    print(f'Lembrete {contagem}: Pare o robô!')

