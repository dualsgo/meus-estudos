# MIMO - 12 - Programação Orientada a Objetos - Desafio 3

#  Os castelos podem ser feitos de diversos materiais, ajude-nos a descrever a classe WoodCastle .

# Crie o método apropriado para descrever WoodCastle.

class Castle:
    def description(self):
        return "This is a generic castle."

class StoneCastle(Castle):
    def description(self):
        return "This is a stone castle."

class WoodCastle(Castle):
    stone_castle = StoneCastle()
    stone_castle_description = stone_castle.description()
    print(stone_castle_description)

wood_castle = WoodCastle()
wood_castle_description = wood_castle.description()
print(wood_castle_description)
