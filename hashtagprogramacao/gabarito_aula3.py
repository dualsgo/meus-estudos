# inputs
# email = input("Escreva seu e-mail: ")
# nome = input("Seu primeiro nome: ")

# print(nome, email)

# print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação")

# faturamento = float(input("Escreva o faturamento: "))

# imposto = faturamento * 0.1
# print(imposto)

# listas
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[5])

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

# produto_procurado = input("Pesquise pelo nome do produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)

# adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)

# remover um item
lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

# editar um item 
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5
print(precos)

# contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone", "ipad", "iphone"]

print(lista_produtos.count("apple watch"))

# ordenar uma lista
vendas.sort()
print(vendas)