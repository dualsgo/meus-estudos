# MIMO - 11 - Classes - Desafio 3

# Você adora animais de estimação e tem animais de estimação diferentes em casa. Seu irmão está visitando você e não consegue lembrar os nomes dos seus animais de estimação. Conclua a aula Pet para ajudar seu irmão a associar o nome de um animal de estimação às suas propriedades, como família ou cor.
class Pet:
    def __init__(self, name, family, animal_type, color):
        self.name = name
        self.family = family
        self.animal_type = animal_type
        self.color = color
    def display_pet(pet):
        print(f"{pet.name} is a {pet.color} colored {pet.family} {pet.animal_type}")
# Dentro da classe Pet , crie variáveis ​​de instância name , family , animal_type e color para armazenar as informações específicas recebidas nos parâmetros.
rio = Pet("Rio", "Macaw", "Parrot", "Blue")
coco = Pet("Coco", "Poodle", "Dog", "White")
bud = Pet("Bud", "Labrador", "Dog", "Brown")
daisy = Pet("Daisy", "Burmese", "Cat", "Grey")

# Exibindo os pets
rio.display_pet()


    