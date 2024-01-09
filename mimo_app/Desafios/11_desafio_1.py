# MIMO - 11 - Classes - Desafio 1

# Como voluntário em um festival, você acompanha as atrações que estão sendo instaladas. Temos uma classe chamada Ride que armazena o nome do passeio e a faixa etária adequada. Use instâncias dessa classe para rastrear as atrações instaladas hoje.
class Ride:
    def __init__(self, name, age_group):
        self.name = name
        self.age_group = age_group
        
# Crie uma nova instância da classe Ride chamada roller_coaster e especifique que seu nome é Roller coaster and an adults Ride.
roller_coaster = Ride("Roller coaster", "adults")

# Crie uma nova instância da classe Ride chamada ferris_wheel e especifique que seu nome é Ferris wheel and a kids ride.
ferris_wheel = Ride("Ferris wheel", "kids")

print(roller_coaster.age_group)
print(ferris_wheel.name)