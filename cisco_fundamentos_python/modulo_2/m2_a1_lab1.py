# 2.1.5   LAB   Trabalhando com a função print()

# Cenário

"""O comando print(), que é uma das diretrizes mais fáceis em Python, simplesmente imprime uma linha na tela.

Em seu primeiro laboratório:"""

# Use a função de print() para imprimir a linha Olá, Python! na tela. Use aspas duplas ao redor da string.
print("Olá, Python!")

# Depois de fazer isso, use a função print() novamente, mas desta vez imprima seu primeiro nome.
print("Maycon")

# Remova as aspas duplas e execute o código. Assista à reação do Python. Que tipo de erro é gerado?
"""NameError: name 'Maycon' is not defined"""
# Ao fazer isso, você está dizendo ao Python que Maycon é uma variável. Como não existe uma variável com esse nome, o Python gera um erro.

# Em seguida, remova os parênteses, coloque aspas duplas e execute o código novamente. Que tipo de erro é gerado desta vez?
"""SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?"""
# Ao fazer isso, estamos ferindo a sintaxe da função print(). O Python espera que a função print() tenha parênteses, portanto, quando não os encontramos, o Python gera um erro.

# Experimente o máximo que puder. Altere aspas duplas para aspas simples, use várias funções print() na mesma linha e, em seguida, em linhas diferentes. Veja o que acontece.
"""Cada instrução print() é executada em uma linha diferente. Se você quiser imprimir várias linhas na tela, precisará usar várias instruções print(). É possível colocar várias instruções na mesma linha, separando umas das outras com vírgula, porém mesmo assim cada execução será exibida em sua própria linha."""
# O comportamento da função print() se deve ao fato dela possuir um argumento especial chamado end. As instruções no código são executadas na mesma ordem em que foram colocadas no arquivo fonte; nenhuma instrução subseqüente é executada até que a anterior seja concluída. Por padrão, o valor do argumento end é \n, que é um caractere de nova linha. Isso significa que, após a execução da função print(), o cursor será movido para a próxima linha. Você pode alterar esse comportamento, passando um novo valor para o argumento end. Por exemplo, se você quiser que o cursor permaneça na mesma linha após a execução da função print(), você pode passar um espaço em branco para o argumento end. Outro argumento da função print é o sep. Sep controla o caractere usado para separar os argumentos da função print(). Como sabemos, a função print aceita vários argumentos. Por padrão, esses argumentos são separados por um espaço em branco. Você pode alterar esse comportamento, passando um novo valor para o argumento sep. Por exemplo, se você quiser que os argumentos sejam separados por um caractere de nova linha, você pode passar \n para o argumento sep. 


