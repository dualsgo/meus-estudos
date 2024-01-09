# MIMO - 11 - Classes
# 11.5 - Compreeendendo as classes  

# Semelhante à nomeação de variáveis e funções, existem algumas práticas comuns ao definir classes.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

teacher = Person("Ashley", 32)

# 1. Os nomes das classes geralmente têm a primeira letra maiúscula e o restante minúsculo. Como Person. Essa convenção é chamada de CamelCase.
# 2. Assim como variáveis e funções, tentamos nomear as classes de forma descritiva.
# 3. Devemos nomear as coisas de forma consistente e tomar cuidado com a capitalização

# 4. Assim como os métodos fora das classes, você pode usar as funções integradsa e os principais recursos do Python.
class Pie:
  def __init__(self, flavor, ingredients):
    # O argumento flavor nesse exemplo é uma string. Podemos acessar o valor do argumento usando self.flavor.
    self.flavor = flavor
    # o argumento ingredients é uma lista. Podemos acessar o valor do argumento usando self.ingredients.
    self.ingredients = ingredients
  # O método print_ingredients() imprime os ingredientes da torta usando um loop for.
  def print_ingredients(self):
    # O argumento ingredients é uma lista de ingredientes. Podemos iterar sobre a lista usando um loop for.
    for i in self.ingredients:    
      print(i)

applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])

applePie.print_ingredients()
