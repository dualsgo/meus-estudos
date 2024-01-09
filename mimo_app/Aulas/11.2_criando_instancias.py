# MIMO - 11 - Classes
# 11.2 - Criando instâncias de classe

class VirtualPet:
    color = "brown"
    legs = 4
    lives = "9"

# Quando queremos usar nosso modelo de classe para criar algo, começamos criando uma variável, como fluffy aqui.

fluffy = VirtualPet() # A seguir, adicionamos o nome da classe e parênteses para criá-la, como acontece aqui. Isso é chamado de instanciar a classe.

# Quando criamos variáveis a partir do modelo de classe, estamos criando instâncias da classe. fluffy é uma instância da classe VirtualPet.

# A classe VirtualPet que estamos usando para criar as variáveis fluffy é chamada de definição.
# VirtualPet é a definição, fluffy é a instância.

# Para acessar uma variável de classe, adicionamos o nome da instância, um ponto e o nome da variável que queremos

print(fluffy.color) # brown

# color é um atributo de fluffy pois é uma variável da classe VirtualPet e fluffy é uma instância da classe VirtualPet.
# Podemos acessar todas as variáveis da classe. Acessamos o valor da variável codificando o nome da instância, um ponto e o nome da variável.

# Se quiser alterar o valor de uma variável de classe, podemos fazer isso usando a notação de ponto. Se quisessemos mostrar fluffy com outros atributos, poderíamos fazer isso:

fluffy.color = "black"
fluffy.lives = "1"

# Outra forma seria colocar argumentos na classe VirtualPet, como fizemos com o método __init__ da classe Computer.

class VirtualPet:
    def __init__(self, color, lives): # O primeiro parâmetro de um método de classe é sempre self. Ele se refere ao objeto que está sendo criado. Os parâmetros restantes são os atributos do objeto.
        self.color = color # O atributo self.color é definido como o valor do parâmetro color.
        self.lives = lives # O atributo self.lives é definido como o valor do parâmetro lives.

# Agora, quando criamos uma instância da classe VirtualPet, precisamos passar os argumentos color e lives.

fluffy = VirtualPet("white", "9")

