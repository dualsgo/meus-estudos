# Programação Orientada a Objetos (Classes)

## EXPLICAÇÃO

A POO ajuda a organizar o código modelando entidades do mundo real em **Classes** (moldes) e **Objetos** (instâncias).

1. **Classe**: O projeto ou molde (ex: Classe `Carro`).
2. **Objeto**: A peça física criada a partir do molde (ex: `meu_fusca`).
3. **Método `__init__` (Construtor)**: Executado automaticamente quando o objeto nasce. Define os atributos iniciais.
4. **`self`**: Representa a própria instância. É obrigatório como primeiro parâmetro de métodos da classe.
5. **Pilares Básicos**:
   * **Encapsulamento**: Proteger dados (usando `__` para tornar privado).
   * **Herança**: Uma classe "filha" herda características da "pai".
   * **Polimorfismo**: Filhos podem agir de formas diferentes para o mesmo comando (sobrescrita de métodos).

## EXEMPLO PRÁTICO

```python
# Definição do Molde
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass # Será definido pelos filhos

# Herança e Polimorfismo
class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Miau!"

# Instanciando Objetos
dog = Cachorro("Rex")
cat = Gato("Fofo")

print(dog.emitir_som())
print(cat.emitir_som())

# Encapsulamento Simples
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo # Privado
    
    def ver_saldo(self):
        return f"Saldo: R$ {self.__saldo}"

minha_conta = Conta(1000)
print(minha_conta.ver_saldo())
```
