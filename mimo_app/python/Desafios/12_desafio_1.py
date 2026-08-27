# MIMO - 12 - Programação Orientada a Objetos - Desafio 1

# Este elevador está avisando às pessoas que está se movendo, mas na realidade ele fica sempre no mesmo andar.

class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_to_floor(self, floor):
        if self.current_floor == floor:
            print(f"Elevator is in floor {floor}")
        else:
            print(f"Going to floor {floor}")

# # Atualize a propriedade atual do piso para que o elevador se mova sempre que for chamado para isso.

elevator = Elevator()
elevator.go_to_floor(3)
elevator.go_to_floor(3)