# MIMO - 12 - Programação Orientada a objetos
# 12.1 - Encapsulamento - Encapsulando objetos

# Vamos aprender sobre os diferentes estilos de codificação usados pelos desenvolvedores. Exploraremos a programação funcional e a programação orientada a objetos.

# Diferentes estilos de codificação também são conhecidos como paradigmas. Um estilo comum é chamado de programação funcional, ou FP, para abreviar. Na programação funcional, usamos muitas funções e variáveis.

def get_total(a, b):
    # Define a função get_total que retorna a soma de dois valores
    return a + b


num1 = 2  # Declara a variável num1 e atribui o valor 2
num2 = 3  # Declara a variável num2 e atribui o valor 3
total = get_total(num1, num2)  # Chama a função get_total com os valores de num1 e num2 e atribui o resultado a total
print(total)  # Imprime o valor de total

# No estilo FP, mantemos os dados e as funcionalidades separados. Passamos dados para funções sempre que queremos alguma coisa.


def get_distance(mph, h):
    # Define a função getDistance que retorna a multiplicação de dois valores
    # Na programação funcional, as funções retornam novos valores e depois usam esses valores em algum lugar do código.
    return mph * h


mph = 60  # Declara a variável mph e atribui o valor 60
h = 2  # Declara a variável h e atribui o valor 2
distance = get_distance(mph, h)  # Chama a função getDistance com os valores de mph e h e atribui o resultado a distance

# Na programação orientada a objetos OOP, agrupamos dados e funcionalidades como propriedades e métodos dentro de objetos, como Virtual_Pet aqui.


class Virtual_Pet:
  # Define a classe Virtual_Pet com um construtor que inicializa as propriedades color e name
    def __init__(self, color, name):
        self.color = color  # Atribui o valor da variável color ao atributo color do objeto
        self.name = name  # Atribui o valor da variável name ao atributo name do objeto


rocky = Virtual_Pet("brown", "Rocky")  # Cria uma instância da classe Virtual_Pet chamada rocky
print(rocky.color)  # Imprime o valor do atributo color do objeto rocky
print(rocky.name)  # Imprime o valor do atributo name do objeto rocky

# OOP possibilita modelar objetos da realidade ou não. Objetos têm propriedades e métodos que tratamos como uma coisa só, como Car aqui.


class Car:
    mileage = 12000  # Atribui o valor 12000 ao atributo mileage da classe Car

    def drive(self, miles):
        # Define o método drive que atualiza o valor do atributo mileage com base no número de milhas percorridas
        self.mileage = self.mileage + miles


tesla = Car()  # Cria uma instância da classe Car chamada tesla
tesla.drive(100)  # Chama o método drive da instância tesla com o valor 100
print(tesla.mileage)  # Imprime o valor do atributo mileage da instância tesla

# Em OOP, usamos métodos para atualizar os valores existentes de um objeto, como aqui, onde usamos eat() para atualizar o valor de hungry()

class Dog:
    hungry = True  # Atribui o valor True ao atributo hungry da classe Dog

    def eat(self):
        # Define o método eat que atualiza o valor do atributo hungry para False
        self.hungry = False


# Vamos criar um cofrinho virtual com OOP. Primeiro, criamos uma nova classe chamada Piggy com uma propriedade value definida como 0.
class Piggy:
    value = 0  # Atribui o valor 0 ao atributo value da classe Piggy
    # A seguir, adicionamos um método chamado addMoney() que aceita um parâmetro chamado amount

    def addMoney(self, amount):
        # Define o método addMoney() que atualiza o valor com a soma do valor atual e amount de Piggy
        self.value = self.value + amount


# Vamos colocar R$ 100 em nosso cofrinho chamando o método addMoney() de Piggy com 100 como argumento.
myPiggy = Piggy()  # Cria uma instância da classe Piggy chamada myPiggy
myPiggy.addMoney(100)  # Chama o método addMoney() da instância myPiggy com o valor 100 como argumento

# Finalmente vamos imprimir o valor de Piggy para ver se o dinheiro foi adicionado.
print(myPiggy.value)  # Imprime o valor do atributo value da instância myPiggy


# Na OOP, agrupamos dados e funções relacionadas no mesmo objeto. Chamamos isso de encapsulamento.
# Com o encapsulamento, também temos métodos que utilizam as demais propriedades que pertencem ao objeto, como neste exemplo eat acessando a propriedade hungry.

class Dog:
    name = 'Fido'  # Atribui o valor 'Fido' ao atributo name da classe Dog
    hungry = False  # Atribui o valor False ao atributo hungry da classe Dog

    def eat(self):
        # Define o método eat que atualiza o valor do atributo hungry para True
        self.hungry = True


# No FP, o código não é encapsulado. Os dados e a função não são agrupados em um objeto.
def get_distance(mph, h):
  # Define a função getDistance que retorna a multiplicação de dois valores
  return mph * h

mph = 60  # Declara a variável mph e atribui o valor 60
h = 2  # Declara a variável h e atribui o valor 2


# Podemos detectar código que não está bem encapsulado se métodos e propriedades relacionados estiverem em objetos diferentes.
class Dog:
    name = 'Fido'  # Atribui o valor 'Fido' ao atributo name da classe Dog
    hungry = False  # Atribui o valor False ao atributo hungry da classe Dog


def eat():
  # Define a função eat que atualiza o valor da variável hungry para True
  hungry = True

# Na OOP identificamos quais métodos e propriedades pertencem reciprocamente e dever ser adicionados ao mesmo objeto.

class Cat:
  color = 'Orange'  # Atribui o valor 'Orange' ao atributo color da classe Cat

  def meow(self):
 # Define o método meow que imprime 'Meow!'
    print('Meow!')

class Car:
    color = 'Red'  # Atribui o valor 'Red' ao atributo color da classe Car

    def drive(self):
        # Define o método drive que imprime 'Vroom!'
        print('Vroom!')