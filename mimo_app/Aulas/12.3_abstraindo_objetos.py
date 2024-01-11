# MIMO - 12 - Programação Orientada a objetos
# 12.3 - Abstraindo objetos

# Vamos tentar modelar um objeto complicado como um carro, usando OOP. Quando dirigimos um carro, não precisamos entender a mecânica interna dele.
# Da mesma forma, ao trabalhar com código, queremos compreender os métodos principais sem nos prender a detalhes.

# Um carro faz muitas coisas ao mesmo tempo. Por exemplo, um carro injeta e acende combustível milhares de vezes por minuto, apenas para continuar funcionando.

# Modelar um carro em Python funciona da mesma forma. No entanto, chamar métodos repetidamente pode dificultar a compreensão do código e o uso.

# Além disso, gerenciar cada chamada de método individual por nós mesmos, aumenta a chance de cometermos um erro e causar um bug.

# Os carros fazem toda essa funcionalidade de baixo nível para nós, e só precisamos ligá-lo e dirigir. Ocultar esses detalhes é chamado de abstração.

# Implementamos abstração em OOP escrevendo algumas funções principais que lidam com todo o trabalho de baixo nível para nós.

class Motor:
  def __init__(self):
    self.on = False
    
  def injectFuel(self):
    # Simula a injeção de combustível
    print('Injecting fuel')
      
  def igniteFuel(self):
    # Simula a ignição do combustível
    print('Igniting fuel')
      
  def startUp(self):
    # Inicia o motor simulando a injeção e ignição do combustível continuamente
    self.on = True
    while self.on:
      self.injectFuel()
      self.igniteFuel()

# A abstração permite que outros desenvolvedores usem uma classe sem precisar saber quais métodos de baixo nível ela possui ou como eles funcionam.

# Outros desenvolvedores podem criar um novo objeto a partir da nossa classe e usá-lo apenas chamando alguns métodos principais.
car = Motor()
car.startUp()  # Inicia o motor do carro simulando a injeção e ignição do combustível continuamente
plane = Motor()
plane.startUp()  # Inicia o motor do avião simulando a injeção e ignição do combustível continuamente
