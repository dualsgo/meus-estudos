# MIMO - 07 - Operações com strings - Desafio 3
# Um professor deseja criar uma lista com os nomes de todos os alunos de sua turma. Ele recebeu uma longa string contendo todos os nomes, cada nome separado por vírgula. Ajude-o a criar uma lista_nomes que armazene os nomes individuais separados por vírgula. Em seguida, imprima a lista.

nomes_estudantes = "Samantha,Mcgrath,Peyton,Kerim,Nadia,Sandra,Sarah,Alex"

lista_nomes = nomes_estudantes.split(',')
print(lista_nomes)
