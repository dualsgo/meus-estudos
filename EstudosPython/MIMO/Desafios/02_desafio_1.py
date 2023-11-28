# MIMO - 02 - Tipos e comparações - DESAFIO 1
# Sam tem 16 anos e quer saber se ela tem idade suficiente para dirigir. Complete os operadores que faltam para mostrar que qualquer pessoa com menos de 17 anos não está autorizada a dirigir.

idade_da_sam = 16
idade_para_dirigir = 18

# Tarefa 1: Termine a comparação muito_jovem para responder à pergunta no console com um boolean que diz que Sam é muito jovem para dirigir.

muito_jovem = idade_da_sam < idade_para_dirigir
pode_dirigir = idade_da_sam == idade_para_dirigir

# Tarefa 2: Conclua a comparação pode_dirigir para mostrar que ela não consegue dirigir.

print(f'Sam é muito nova para dirigir? {muito_jovem}.')
print(f'Sam pode dirigir um carro? {pode_dirigir}.')