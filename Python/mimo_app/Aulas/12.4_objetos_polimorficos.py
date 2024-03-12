# MIMO - 12 - Programação Orientada a objetos
# 12.4 - Objetos polimórficos

# Métodos representam comportamentos. Por exemplo, um método speak() exibe mensagem na tela

# Com herança, podemos estender a funcionalidade de uma classe filha. Mas e se quisermos implementar comportamentos de classe de maneira diferente?

class Feline:
  def speak(self):
    # Define o comportamento padrão para o método speak() na classe Feline
    print('Meow!')

class Cat(Feline):
  def lick(self):
    # Define um comportamento específico para o método lick() na classe Cat
    print('Licking paw')

# Aqui vemos o gato miando, o que é correto. Queremos que um comportamento diferente de speak() com base na classe. Isso é chamado de polimorfismo.
class Lion(Feline):
  def prey(self):
    # Define um comportamento específico para o método prey() na classe Lion
    print('Hunting for food')

  # Uma subclasse pode substituir os métodos que herda de sua superclasse. Simplesmente definimos o método com o mesmo nome na subclasse.
  def speak(self):
    # Define um comportamento específico para o método speak() na classe Lion
    print('Roar!')

cat = Cat()
cat.speak()  # Chama o método speak() da classe Feline na classe Cat

lion = Lion()
lion.speak()  # Chama o método speak() da classe Lion
