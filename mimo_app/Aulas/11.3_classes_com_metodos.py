# MIMO - 11 - Classes
# 11.3 - Classes com métodos

# As classes também podem ter funções, que são conhecidas como métodos quando estão dentro de uma classe. Como método bark() aqui.

class VirtualPet:
    color = "brown"
        
    def bark(self):
        print("Bark bark bark!")
    
    # self é uma palavra-chave especial que precisamos usar dentro de nossa definição de classe. Passamos self como o primeiro parâmetro para todos os métodos que adicionamos. Ele se refere ao objeto que está sendo criado. Sempre que criamos um método de classe, precisamos passar self como o primeiro parâmetro. O Python passa automaticamente o objeto que está sendo criado como o primeiro argumento para todos os métodos de classe.
    def display_color(self):
        print(self.color)
    # Usamos self como parâmetro nos métodos de classe para que possamos acessar as variáveis de classe como color e legs dentro dos métodos. Sem self, não poderíamos acessar as variáveis de classe. Dentro de display_color(), usamos self.color para acessar a variável de classe color = "brown".
    
    # Sem usar self não seríamos capazes de acessar as variáveis de classe pois elas são declaradas fora do escopo do método classe.
    
rocky = VirtualPet()

# Para usar um método de classe é o mesmo que usar uma variável de classe, exceto que precisamos adicionar parênteses. Como aqui com rocky.bark().
rocky.bark()





