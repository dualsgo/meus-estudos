# Projeto 01 - Organizador de Almoço: Neste projeto, você está codificando um programa para ajudá-lo a organizar um almoço para seus amigos.

# Tarefa 1: Você servirá pizza para os convidados da sua festa. Vamos criar uma variável e armazenar o item de menu dentro.
# Crie uma variável menu_item e atribua o valor de string "pizza"
menu_item = 'Pizza'

# Tarefa 2: 10 convidados confirmaram que estão vindo para sua festa. Vamos criar outra variável para acompanhar o número de convidados.
# Crie uma variável convidados e tribua o valor 10.
convidados = 10

# Tarefa 3: Antes dos convidados chegarem, vamos verificar o cardápio e o número de pessoas que vêm para ter certeza de que preparamos comida suficiente. Para exibir os valores armazenados nas variáveis que criamos, vamos usar instruções de impressão.

# Imprima a variável menu_item
print(menu_item)
# Imprima a variável convidados
print(convidados)

# Tarefa 4: Você acabou de receber uma ligação de um dos convidados e eles lhe disseram que eles são alérgicos a queijo! Para garantir a segurança de todos, vamos substituir o item do menu por biryani. Biryani é um delicioso prato feito com carne ou legumes, arroz e uma variedade de especiarias saborosas.

# Atualize o valor da variável menu_item para "biryani"
menu_item = 'biryani'

# Tarefa 5: Vamos nos certificar de que atualizamos o menu! Podemos usar uma declaração impressão para fazer isso.

# Imprima no console usando uma expressão. O resultado deve ser o seguinte: Item do menu atualizado é: biryani
print('Item do menu atualizado é: ' + menu_item )

# Tarefa 6: É hora de calcular quanto biryani você precisa para 10 convidados. Comece criando uma variável para armazenar a quantidade de biryani para uma única pessoa. Em seguida, calcule a quantidade de biryani que precisamos para 10 convidados.

# Crie uma variável biryani_por_pessoa e atribua-lhe um valor 1
biryani_por_pessoa = 1
# Crie uma variável biryani_necessario e atribua o valor da multiplicação de biryani_por_pessoa * convidados
biryani_necessario = biryani_por_pessoa * convidados

# Tarefa 7: Você pediu o biryani depois de calcular quanto biryani você vai precisar para 10 convidados e ele foi entregue em sua casa. Você contou o biryani que recebeu. Agora vamos armazenar o número de biryani que você acabou de contar em uma nova variável.

# Crie uma variável biryani_preparado e atribua-lhe um valor 10
biryani_preparado  = 10

# Tarefa 8: Vamos verificar se temos biryani suficiente usando o operador de igualdade.

# Crie uma variável biryani_suficiente e atribua o resultado da verificação de se biryani_preparado é igual a biryani_necessario
biryani_suficiente = biryani_preparado == biryani_necessario
print(biryani_suficiente)

# Tarefa 9: Os convidados começaram a chegar e você percebeu que um deles trouxe o irmão para a festa também. Vamos atualizar o número de convidados em nosso programa.

# Acrescentar 1 a convidados
convidados = convidados + 1

# Tarefa 9: Para garantir que todos recebam uma porção de biryani, vamos calcular quanto biryani precisamos para servir cada convidado.

# Crie uma variável biryani_por_convidado e defina igual a biryani_preparado dividido por convidados
biryani_por_convidado = biryani_preparado / convidados
# Use uma instrução de impressão para exibir no console biryani_por_convidado
print(biryani_por_convidado)

