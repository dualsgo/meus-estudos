# 2.5.1 Comentários - por que, quando e como?

# Uma observação inserida no programa, omitida em tempo de execução, é chamada de comentário. Em Python, um comentário é um pedaço de texto que começa com um sinal # (hash) e se estende até o final da linha.

# Se você deseja um comentário que se estenda por várias linhas, deve colocar um hash na frente de todas elas. Assim como aqui:

# Esse programa calcula a hipotenusa c.
# a e b são os tamanhos dos lados.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Nós usamos ** ao invés de raiz quadrada.
print("c =", c)


# 2.5.4 RESUMO DA SEÇÃO
"""Os comentários podem ser usados para deixar informações adicionais no código. Eles são omitidos em tempo de execução. As informações deixadas no código-fonte são endereçadas aos leitores humanos. Em Python, um comentário é um texto que começa com #. O comentário se estende até o final da linha.

Se você deseja colocar um comentário que abrange várias linhas, você precisa colocar # na frente de todas. Além disso, você pode usar um comentário para marcar um pedaço de código que não é necessário no momento (veja a última linha do snippet abaixo), por exemplo:

# Este programa imprime
# uma introdução à tela.
print("Olá!")  # Chamando a função print()
# print("Em Python.")

Sempre que possível e justificado, você deve fornecer nomes auto comentados a variáveis, por exemplo, se você estiver usando duas variáveis para armazenar o length e width de algo, podem ter uma escolha melhor que o myvar1 e o myvar2.

É importante usar comentários para facilitar a compreensão dos programas e usar nomes de variáveis legíveis e significativos no código. No entanto, é igualmente importante não usar nomes de variáveis que são confusos ou deixar comentários que contêm informações incorretas ou incorretas!

Os comentários podem ser importantes quando você está lendo seu próprio código depois de algum tempo (confie em nós, os desenvolvedores esquecem o que seu próprio código faz) e quando outros estão lendo seu código (eles podem ajudá-los a entender o que seus programas fazem e como eles fazem isso mais rapidamente)."""