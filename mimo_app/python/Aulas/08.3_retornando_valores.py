# MIMO - 08 - Funções
# 08.3 - Retornando valores

# Uma função pode retornar um valor ao código que a chamou.
# Funções são escritas para realizar tarefas e às vezes podemos precisar do resultado das tarefas. Isso pode ser feito via return
# Adicionamos a palavra-chave return, seguida do valor a ser retornado. O valor pode ser de qualquer tipo e o chamamos de saída da função.
# Podemos usar o valor de retorno de uma função como qualquer valor chamando a função.

# Por exemplo, podemos criar uma função que verifica a idade de uma pessoa e retorna se ela é maior ou menor de idade.

def maior_idade(idade):
    # O parâmetro receberá o valor que passarmos quando chamarmos a função
    texto = f'Com {idade} anos você é '
    if idade >= 18:
        texto = texto + 'maior de idade.'
    else:
        texto = texto + 'menor de idade.'

    return texto # Se não incluirmos a instrução return, a função retornará o valor None

# Também podemos armazenar o valor de retorno em uma variável
resultado = maior_idade(int(input('Digite a sua idade: '))) # O valor de retorno será armazenado na variável resultado. O valor do parâmetro será o que o usuário digitar

print(resultado)


# Mesmo sem parâmetros, se o código após return for funcional, ao chamar a função ele será exibido

def teste():
    # Nesse programa o return é simplesmente uma expressão matemática que não depende de nenhum parâmetro
    return 1 + 1  # O valor de retorno será 2 sempre que a função for chamada

print(teste())
