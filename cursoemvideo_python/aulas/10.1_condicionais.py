# MIMO - Declarações condicionais

# Declarações que dependem de condições são chamadas de condicionais.

# if (se): A decalaração if executa o código somente se o resultado for avaliado como True. Soa como "Se algo é verdade, faça isso"
algo = True
# MIMO - Declarações Condicionais

# Declarações que dependem de condições são chamadas de condicionais.

# if (se): A declaração if executa o código somente se a condição avaliada for True. Soa como "Se algo é verdade, faça isso."
algo = True
if algo:
    # Usamos um recuo de dois espaços para destacar os blocos de código. Todas as linhas com o mesmo recuo pertencem ao bloco de código.
    print('Avaliado como verdadeiro!')
    print('Essa instrução também faz parte do bloco de código condicional.')

# else (senão): O bloco de código em else é executado quando a condição do if não é avaliada como True. É como uma resposta padrão.
else:
    print('Essa linha seria exibida caso a condição do if não fosse atendida.')

print('Esta instrução não faz parte do bloco condicional e é exibida independentemente do resultado.')

# elif (senão se): Podemos usar elif para condições mais específicas. É usado quando há uma segunda condição a ser verificada quando a condição do if não for atendida. Podemos usar quantos elif quisermos.
if algo:
    # Usamos um recuo de dois espaços para destacar os blocos de código. Todas as linhas com o mesmo recuo pertencem ao bloco de código
    print('Avaliado como verdadeiro!')
    print('Essa instrução também faz parte do bloco de código condicional.')
# Podemos usar operadores de comparação em programas para verificar se algo está correto e se a resposta dada é igual a solução esperada.
else:  # Else vai sempre no final do código da instrução.
    # else (senão): Programas não decide somente oque fazer quando uma condição é true. Eles contam com um plano B caso a condição seja avaliada como False. Usamos a intrução else. Ela não precisa de uma condição própria pois trata dos casos em que a condição do if não é avaliada como True. É como uma resposta padrão
    print('Essa linha seria exibida caso a condição do if não fosse atendida.')
print('Já essa instrução não faz parte do bloco condicional e é exibida independente do resultado.')
# elif (senão se): Para condições mais específicas usamos elif. É usado quando há uma segunda condição a ser verificada quando a condição do if não for atendida. Contanto que venha antes de else, podemos usar quandos elif quisermos.
