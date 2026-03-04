# MIMO - 05 - Listas - Desafio 2
# É hora do torneio da sua liga de vôlei, mas muitos de seus companheiros de equipe estão fora da cidade durante o fim de semana prolongado. Parece que teremos que fazer algumas substituições.

players = ["Iliana", "Samuel", "Anders", "Teresa", "Gabriele", "Alejandro"]
print(f'Equipe: {players}')
# Tarefa 1: Use uma operação de lista para substituir "Iliana" por "Jack"
sub_1 = "Jack"
print(f'Sai: {players[0]}')

players[0] = sub_1
print(f'Entra: {players[0]}')

# Tarefa 2: Substitua "Anders" por "Celeste"
sub_2 = "Celeste"
print(f'Sai: {players[2]}')

players[2] = sub_2
print(f'Entra: {players[2]}')

# Tarefa 3: Substitua "Gabrielle" por "Mary"
sub_3 = "Mary"
print(f'Sai: {players[4]}')

players[4] = sub_3
print(f'Entra: {players[4]}')

print(f'Equipe atualizada: {players}')