# Curso Python #013 - Estrutura de repetição for

# Laços, repetições ou iterações

# Laços de repetição com variável de controle realizam as instruções repetidamente, uma determinada quantidade de vezes.

# A sintaxe de um laço for é a seguinte:
#
for contador in range(1, 10):
    # O range é o intervalo e recebe os argumentos: início, fim e iteração
    print(f'Repita isso: {contador}')
    # A instrução será executada no intervalo indicado de 1 a 10 (excluindo o 10). Serão 9 repetições
print('Pare')

# Se adicionarmos a iteração no range() a contagem muda

for contador in range(1, 10, 2):
    # Após o primeiro, iremos pular a cada dois
    print(f'Repita isso iterando a cada 2: {contador}')
print('Pare')

# Podemos utilizar as estruturas condicionais aninhadas num loop usando a identação (recuo) para estruturar o código.

for contador in range(1, 10):
    print(f'Contagem: {contador}')
    # Aqui se o número for par ou ímpar, retorna o texto correspondente
    if contador % 2 == 0:
        print(f'{contador} é par.')
    else:
        print(f'{contador} é ímpar.')
print('Pare')

print('\n============ Parte prática ============\n')

# O laço inicia em zero e termina no número anterior ao argumento. Nesse exemplo finaliza no 5
for c in range(0, 6):
    print(c)

# Se quisermos fazer em contagem regressiva, devemos u/começar com o maior algarismo e terminar no menor além de usar a iteração negativa.
for c in range(6, 0, -1):
    print(c)
# Da mesma forma que antes, o algarismo do fim é desconsiderado

# Podemos entrar com os valores para o laço utilizando input() e usando as variáveis como valores dos argumentos para o range()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
iteracao = int(input('Iteração: '))

for c in range(inicio, fim, iteracao):
    print(f'Contando: {c}')
print('FIM!')
