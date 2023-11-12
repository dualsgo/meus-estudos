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

# Diferença if e elif - A escolha entre if e elif depende de como você deseja que o programa se comporte com relação às condições. O elif é útil quando você quer testar várias condições exclusivas, enquanto vários blocos if podem ser usados quando você deseja avaliar condições independentes.