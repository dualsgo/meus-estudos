# MIMO - 12 - Programação Orientada a Objetos - Desafio 2

# As máquinas de café podem produzir uma quantidade limitada de tipos de café.

class CoffeeMachine:
    def __init__(self):
        self.coffee_options = {"Capuccino", "Espresso"}
    
    # # Verifique se o coffee_type é válido para nossa máquina e armazene o resultado na variável is_valid_coffee_type.

    def make_coffee(self, coffee_type):
        is_valid_coffee_type = True
        if is_valid_coffee_type:
            return f"{coffee_type} made!"
        else:
            return f"{coffee_type} is not a valid option!"

machine = CoffeeMachine()
print(machine.make_coffee("Espresso"))
print(machine.make_coffee("Moka"))