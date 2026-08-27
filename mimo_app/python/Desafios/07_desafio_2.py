# MIMO - 07 - Operações com strings - Desafio 2
# Você trabalha como desenvolvedor de software e decidiu usar um conjunto específico de tecnologias de programação para sua próxima aplicação. Em uma solicitação de última hora do cliente, você concordou em usar React em vez de Angular.
tech_stack = "Angular Node Mongo Express"
print(tech_stack.split())

# Tarefa 1: Atribua novamente tech_stack e use uma operação de string para substituir "Angular" por "React".
tech_stack = tech_stack.replace("Angular", "React")

# Tarefa 2: Crie uma variável tech_stack_list que armazene os nomes de tech_stack como uma lista.
tech_stack_list = tech_stack.split()

# Tarefa 3: Imprimir tech_stack_list
print(tech_stack_list)