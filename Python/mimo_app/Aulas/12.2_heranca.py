# MIMO - 12 - Programação Orientada a objetos
# 12.2 - Aplicando herança

# Como aprendemos anteriormente, OOP significa encapsular dados e funções relacionadas dentro de objetos
# Quando criamos objetos um por um, nos deparamos com o problema de ter código duplicado.

from typing import Any

class Person1:
  # Define a classe Person1
  name = 'John'
  def greet(self):
    # Define o método greet que imprime uma saudação usando o atributo name
    print(f'Hello, my name is {self.name}')
class Person2:
  # Define a classe Person2
  name = 'Mike'
  def greet(self):
    # Define o método greet que imprime uma saudação usando o atributo name
    print(f'Hello, my name is {self.name}')
class Person3:
  # Define a classe Person3
  name = 'Jane'
  def greet(self):
    # Define o método greet que imprime uma saudação usando o atributo name
    print(f'Hello, my name is {self.name}')

# Usamos herança para tornar nosso código eficiente. Através de herança, as classes recebem métodos de outras classes.
class Parent:
  # Define a classe Parent
  def __init__(self):
    # Define o construtor da classe Parent que inicializa o atributo eyes
    self.eyes = 'brown'

# Aqui vemos que a classe Child está herdando a classe Parent porque está entre parênteses após a definição da classe.
class Child(Parent):
  # Define a classe Child que herda da classe Parent
  def __init__(self):
    # Chama o construtor da classe Parent usando super() e inicializa o atributo age
    super().__init__()
    self.age = 7

child = Child()
print(child.eyes)  # Imprime o valor do atributo eyes herdado da classe Parent
print(child.age)  # Imprime o valor do atributo age da classe Child

# Vejamos como uma classe pode herdar métodos de outra. Ao definir a classe, adicionamos parênteses à classe que herdamos.
class Greetings():
  # Define a classe Greetings
  def greet(self):
    # Define o método greet que imprime 'Hello!'
    print('Hello!')
# A classe Person agora pode usar métodos da Saudação como os seus.
class Person(Greetings):
  # Define a classe Person que herda da classe Greetings
  name = 'George'

p = Person()
p.greet()  # Chama o método greet herdado da classe Greetings

# Podemos atualizar o funcionamento das classes definindo métodos diretamente na classe.
class Car:
  # Define a classe Car
  def start_car(self):
    # Define o método start_car que imprime 'Starting the car'
    print('Starting the car')
class Hybrid(Car):
  # Define a classe Hybrid que herda da classe Car
  def charge(self):
    # Define o método charge que imprime 'Charging the battery'
    print('Charging the battery')
class Electric(Car):
  # Define a classe Electric que herda da classe Car
  def fuel(self):
    # Define o método fuel que imprime 'No fuel needed'
    print('No fuel needed')

prius = Hybrid()
electric = Electric()
prius.start_car()  # Chama o método start_car da classe Car herdado pela classe Hybrid
electric.start_car()  # Chama o método start_car da classe Car herdado pela classe Electric
prius.charge()  # Chama o método charge da classe Hybrid
electric.fuel()  # Chama o método fuel da classe Electric

# As classes contêm um método chamado construtor que define as propriedades de novos objetos, conhecidos como instâncias.
class Person:
  # Define a classe Person
  def __init__(self, name, age):
    # Define o construtor da classe Person que inicializa os atributos name e age
    self.name = name
    self.age = age

sam = Person('Sam', 7)
print(sam.name, sam.age)  # Imprime os valores dos atributos name e age da instância sam

# Podemos usar o conceito de herança para reutilizar partes de código em nossas classes, tornando nosso código mais eficiente.
class Person:
  # Define a classe Person
  def __init__(self, name, age):
    # Define o construtor da classe Person que inicializa os atributos name e age
    self.name = name
    self.age = age
  def greet(self):
    # Define o método greet que imprime 'Hello!'
    print('Hello!')

class Nurse(Person):
  # Define a classe Nurse que herda da classe Person
  def __init__(self, name, age):
    # Chama o construtor da classe Person usando super() e inicializa o atributo name
    super().__init__('Nurse '+ name, age)
  def intro(self):
    # Define o método intro que imprime uma introdução
    print("Hi, I'm Nurse " + self.name)

Person1 = Person('John', 36)
Person2 = Nurse('Jane', 32)
Person1.greet()  # Chama o método greet da classe Person
Person2.intro()  # Chama o método intro da classe Nurse

# Ao trabalhar com classes, temos que pensar um pouco em como aplicar herança. Suponha que queríamos modelar uma classe student em nosso código.

# Queremos que Student funcione como Person, exceto que tenha um major. Se criarmos uma nova classe Student, acabaremos com código duplicado.

# Em vez disso faz, faz mais sentido, neste caso, criar uma subclasse que herde o método greet() da classe Person, codificando (Person) após Student.

class Student(Person):
  # Define a classe Student que herda da classe Person
  def __init__(self, name, age, major):
    # Chama o construtor da classe Person usando super() e inicializa o atributo major
    super().__init__(name, age)
    self.major = major
  def intro(self):
    # Define o método intro que imprime uma introdução personalizada para Student
    print(f'Hi, I am {self.name} and I study {self.major}')