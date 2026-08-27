# MIMO - 08 - Funções - Desafio 1
# Você está criando um aplicativo Web para um restaurante que calcula o preço total de um item após impostos.

# Tarefa 1: Complete a função calculate_tax que pega um preço específico e o atualiza com um imposto adicional de 10%.
def calculate_tax(price):
    price += price * 0.1
    return price

# Tarefa 2: Certifique-se de retornar o price atualizado após o cálculo.
print(calculate_tax(100))