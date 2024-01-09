# MIMO - 11 - Classes
# 11.1 - Usando classes

# À medida que construímos programas, muitas vezes precisaremos criar muitos objetos semelhantes, mas distintos. Como várias configurações diferentes de um computador.

# Criar novas variáveis para cada uma das diferentes configurações de um computador levaria muito tempo e poderia levar a erros. Para nos ajudar a agrupar dados e funcionalidades, criamos uma classe. Uma classe é um modelo que usamos para criar muitas coisas semelhantes, mas distintas.

computer1_size = "15"
computer1_storage = "1TB"

computer2_size = "13"
computer2_storage = "256GB"

print("Computer1 display size: " + computer1_size)
print("Computer1 storage: " + computer1_storage)

print("Computer2 display size: " + computer2_size)
print("Computer2 storage: " + computer2_storage)

# A sintaxe é a seguinte: 
# class NomeDaClasse:
    # código da classe

# Usamos recuos para indicar que o código abaixo da linha de definição da classe pertence à classe. O recuo é de quatro espaços por convenção.
# O nome da classe deve começar com uma letra maiúscula. Por convenção, usamos CamelCase para nomes de classes.


class Computer: # A classe Computer é um modelo para criar computadores. Ela não é um computador real, mas um modelo para criar computadores.
  
    # O método __init__ é chamado quando criamos um novo objeto da classe. Ele nos permite definir os atributos do objeto.
    
    def __init__(self, size, storage): # O primeiro parâmetro de um método de classe é sempre self. Ele se refere ao objeto que está sendo criado. Os parâmetros restantes são os atributos do objeto.
      
        self.size = size # O atributo self.size é definido como o valor do parâmetro size.
        
        self.storage = storage # O atributo self.storage é definido como o valor do parâmetro storage.
        
        
    # O método print_specs imprime os atributos do objeto.
    # O primeiro parâmetro de um método de classe é sempre self. Ele se refere ao objeto que está sendo criado. Os parâmetros restantes são os atributos do objeto.
    
    def print_specs(self):
        print("Display size: " + self.size)
        print("Storage: " + self.storage)
    # Métodos em classes são semelhantes a funções, mas são chamados usando a notação de ponto. São opcionais e podem ser omitidos.   
        
        
# Resumindo o que fizemos até agora: criamos uma classe Computer que é um modelo para criar computadores. A classe Computer tem dois atributos: size e storage. Também criamos um método print_specs que imprime os atributos do objeto.

# Ao usar um modelo, podemos criar configurações diferentes sem ter que criar variáveis individuais como size e storage a cada vez.

low_spec = Computer("13", "256GB") # Criamos um novo objeto da classe Computer e o atribuímos à variável low_spec. Os valores dos atributos são passados para o método __init__. O parâmetro self é passado automaticamente e não precisamos passá-lo.
high_spec = Computer("15", "1TB")

print("Low spec Computer:")
low_spec.print_specs() # Chamamos o método print_specs no objeto low_spec.

# Criamos um método para facilitar a impressão dos atributos do objeto. Chamamos o método print_specs no objeto low_spec. Mas poderíamos executar os prints diretamente. Assim:

print("Low spec Computer:")
print("Display size: " + low_spec.size)

# Vamos fazer passoa a passo:

# Para começar a criar o modelo, adicionamos a palavra-chave class seguida de um nome e dois pontos. Aqui, criaremos a class, chamada Person:.

class Person:
  # Para adicionar código à classe, recuamos da palavra-chave class como a instrução print() aqui.
    print('Inside the class')
  # Criar variáveis dentro de uma classe funciona exatamente como criar variáveis normais. Ele precisa ser recuado corretamente e receber um valor.
    nationality = 'Brazilian'
  # Podemos adicionar quantas variáveis quisermos dentro de uma classe, como acontece com a variável hobby com o valor "Cooking" aqui.
    hobby = 'Cooking'
    
  # Se quisermos adicionar uma funcionalidade à classe, podemos criar uma função dentro dela. Aqui, criamos uma função chamada say_hello() que imprime "Hello, world!".
    def say_hello(self):
        print('Hello, world!')
        print('My hobby is ' + self.hobby)
        # Para a funcionalidade acessar as variáveis da classe, precisamos usar a palavra-chave self. antes do nome da variável. Aqui, usamos self.hobby para acessar a variável hobby.