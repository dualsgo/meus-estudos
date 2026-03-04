# MIMO - 06 - Operações com listas - Desafio 2
# Temos um torneio mensal e registramos o nome do campeão na lista champions.
campeoes = ["Miracle+", "Tooti3", "Orustat", "Emkay", "mizuhana", "CaptainSpark", "NichMercs", "mizuhana", "dabian", "Cyle",  "Tooti3", "Flaker"]
print(f'Lista atual: {campeoes}')

# Recentemente, descobrimos que um participante regular estava trapaceando. Temos que verificar se "Tooti3" ganhou algum torneio e removê-lo da lista. Descubra quantas vezes ele aparece na lista usando count()
print(f'Ele aparece {campeoes.count("Tooti3")} vezes.')

while "Tooti3" in campeoes:
    campeoes.remove("Tooti3")
print(f'Lista atualizada: {campeoes}')
