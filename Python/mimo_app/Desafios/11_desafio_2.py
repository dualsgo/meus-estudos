# MIMO - 11 - Classes - Desafio 2

# Há um café próximo que oferece uma nova variedade de bebidas todos os dias. Temos uma classe Beverage e duas instâncias: fruity e cocoa. Descubra o que há nas bebidas de hoje.
class Beverage:
    def __init__(self, name, is_alcoholic):
        self.name = name
        self.is_alcoholic = is_alcoholic

# Acesse a propriedade name da bebida fruity e imprima no console.
fruity = Beverage("Fruit punch", False)
print(fruity.name)

# Acesse a propriedade is_alcoholic da bebida cocoa e imprima no console.
cocoa = Beverage("Hot chocolate", False)
print(cocoa.is_alcoholic)


