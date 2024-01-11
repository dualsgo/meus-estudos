# MIMO - 11 - Classes
# 11.4 - Construtores

# Existe um método que podemos usar que é mais flexível ao criar diferentes instâncias de uma classe. É chamado de método construtor.

class VirtualPet:
    # O método construtor se parece com __init__() e nos permite definir valores exclusivos para as variáveis de classe quando criamos uma instância. Para adicionar essa flexibilidade às nossas classes, começamos adicionando a função de construção, que se parece com __init__().

    def __init__(self, color):
        # Assim como acontece com os métodos de classe regulares, precisamos adicionar self como o primeiro parâmetro método construtor. A seguir, adicionamos os parâmetros para os valores personalizados que queremos definir ao criar uma instância, como acontece com color aqui.

        self.color = color
        # Em seguida definimos o valor codificando self, um ponto e o nome do parâmetro e, em seguida, igualando-o ao valor do parâmetro novamente. Isso faz com que o valor do parâmetro seja atribuído à variável de classe color. O valor será diferente para cada instância que criarmos, sendo definido quando criamos a instância e passamos o valor do parâmetro.

    def display_color(self):
        # Podemos acessar os parâmetros de outros locais na definição da classe usando self. Aqui, usamos self.color para acessar o valor do parâmetro color.
        print(self.color)

    # Em vez de uma definição de classe que terá sempre a mesma cor, como:
    # color = "brown"
    # um método construtor nos permite especificar o que queremos ao criá-la

# Quando criamos uma instância a partir da definição de classe, podemos passar valores únicos entre parênteses, como acontece com rocky e benny aqui.


rocky = VirtualPet("brown")
benny = VirtualPet("black")

print(rocky.color)
print(benny.color)
rocky.display_color()