# Curso Python #014 - Estrutura de repetição while
# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:

# c=1
# while c !=10:
#      print(c)
#      c+=1
# print('Acabou')

# Diferente da estrutura for que precisa de um limite definido, a estrutura while executa o código enquanto uma condição for verdadeira.

# Laço com for - O contador é atualizado automaticamente dentro do intervalo selecionado.

for c in range(1, 11):
    print(c)

# Mesmo laço com while - Precisamos de um contador e o atualizamos dentro do loop a cada repetição para usar seu valor como comparação

c = 1  # Inicializamos o contador fora do loop
while c < 11:  # Usamos o valor para criar uma estrutura condicional
    print(c)
    c += 1  # Incrementamos o contador